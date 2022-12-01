
import math
class point:
    #constractor
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def __str__ (self):
        return f"({self.x},{self.y})"
    def __add__ (self,point):
        return point(self.x+point.x,self.y+point.y)
    def __mul__ (self,point):
        x_1, x_2 =self.x , point.x
        y_1, y_2 =self.y , point.y
        a_1,a_2=self.x , point.x
        b_1,b_2=self.y , point.y
        if(x_1<x_2):
            a_1 = x_2
            a_2 = x_1
        if(y_1< y_2):
            b_1 = y_2
            b_2 = y_1
        return  point(a_1-a_2,b_1-b_2)  
    def distanceForm(self,p):
        return math.sqrt((self.x-p.x)**2+(self.y-p.y)**2)
    def whithArea(self):
        a = self.x
        b = self.y
        if a>0 and b>0:
            return "1"
        if a>0 and b<0:
            return "4"
        if a<0 and b<0:
            return "3"
        if a<0 and b>0:
            return "2"
        if a == 0 and b>0:
            return  "2|1"
        if a == 0 and b<0:
            return  "3|4"  
        if a>0 and b == 0:
            return "1\n-\n4"  
        if a<0 and b == 0:
            return "2\n-\n3"
        else : return "1|2\n-*-\n3|4"
