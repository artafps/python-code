import sqlite3
from random import randrange


# ایمپورت کردن sql
import datetime

# وصل کردن دیتابیس 
con = sqlite3.connect("sql.db")
cur = con.cursor()

#cur.execute("CREATE TABLE movie(id text, username text, password text, stars text, coin text, numplay text, logindate text)")

class db:
    def __init__(self,db):
        self._alluser = db
    def getAlldata(self):
        res = self._alluser
        return res.fetchall()
    def searchByname(self,username):
        res = self.getAlldata()
        for i in res:
            if(i[1]==username):
                return [True,i]
        return [False]
    def searchByID(self,id):
        res = self.getAlldata()
        for i in res:
            if(i[0]==id):
                return [True,i]
        return [False]
    def loginUser(self,username,password):
        res = self.getAlldata()
        for i in res:
            if(i[1]==username and i[2]==password):
                return True           
        return False 
    def createUser(self,username):
        date =  str(datetime.datetime.now()).split(" ")[0]
        if(self.searchByname(username)[0]):
            return False
        
        boolean = True 
        Id=""
        while boolean:
            Id = self.createId() 
            if(not self.searchByID(Id)[0]):
                boolean = False
        infoUser=(Id, username,randrange(1000000), '0','0', '0', date)
        string1="""INSERT INTO movie VALUES """
        datastr = string1+str(infoUser)
        cur.execute(datastr)
        con.commit()
        return True
    
    def setStars(self,Id):
        stars = int(cur.execute("SELECT stars FROM movie WHERE id=" + f"'{Id}'").fetchall()[0][0]) + 1
        if stars:
            cur.execute("UPDATE movie SET stars = "+ f"'{stars}'" +" WHERE id = "+f"'{Id}'")
            con.commit()
            return True
        else:
            return False
    def setCoin(self,Id,num):
        coin = int(cur.execute("SELECT coin FROM movie WHERE id=" + f"'{Id}'").fetchall()[0][0]) + int(num)
        if(coin):
            cur.execute("UPDATE movie SET coin = "+ f"'{coin}'" +" WHERE id = "+f"'{Id}'")
            con.commit()
            return True
        else:
            return False
    def setnumplay(self,Id):
        num = int(cur.execute("SELECT numplay FROM movie WHERE id=" + f"'{Id}'").fetchall()[0][0]) + 1
        if(num):
            cur.execute("UPDATE movie SET numplay = "+ f"'{num}'" +" WHERE id = "+f"'{Id}'")
            con.commit()
            return True
        else:
            return False
    def getPassword(self,username,id,stars):
        info = cur.execute("SELECT * FROM movie WHERE username=" + f"'{username}'").fetchall()
        print(info)
        if info:
            if(info[0][0]==id or info[0][3]==stars):
                return info[0][2]
            else:
                return 0
        return 0
    def createId(self):
            boolean = True 
            Id=0
            while boolean:
                Id = randrange(1000000)
                if(100000<Id<1000000):
                    boolean = False
            return 'ID'+str(Id)

dataB = db(cur.execute("SELECT * FROM movie"))
def getDatabase():
    return dataB
