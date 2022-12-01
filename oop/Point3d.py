import math

class point3d:
    #start constractor
    def __init__(self, a, b, c):
        self.x=a
        self.y=b
        self.z=c
    #end constractor
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    def __add__(selp, p):
        return point3d(self.x+p.x,self.y+p.y,self.z+p.z)
    def __mul__(self, p):
        return point3d(self.x-p.x,self.y-p.y,self.z-p.z)
    def distanceForm(self,p): 
        return math.sqrt((self.x-p.x)**2+(self.y-p.y)**2+(self.z-p.z)**2) 
   
