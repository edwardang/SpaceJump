
#########RUN GAME ON jump.py FILE############

class Platforms(object):
    taken = dict()
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 50
        self.height=15
        self.maxnum = 20
        
    def __eq__(self,other):
        return (isinstance(other,Platforms) and self.x==other.x)

    def collide(self,x1,x2,y):
        if (x1 >= self.x and x1 < self.x+self.width and y<=self.y+self.height\
        and y>self.y-10) or (x2 >= self.x and x2 < self.x+self.width and \
        y<=self.y+self.height and y>self.y-10):
            return True
        return False
    def draw(self,canvas):
        canvas.create_rectangle(self.x,self.y,self.x+self.width,self.y+\
            self.height, fill="gray")

    def checkoverlap(self,x,y):
        if (x>=self.x and x<=self.x+self.width and y>=self.y and y<=self.y\
        +self.height) or (x+self.width>=self.x and x+self.width<=\
        self.x+self.width and y>=self.y and y<=self.y\
        +self.height) or (x>=self.x and x<=self.x+self.width and \
        y+self.height>=self.y and y+self.height<=self.y\
        +self.height) or (x+self.width>=self.x and x+self.width<=\
        self.x+self.width and y+self.height>=self.y and y+self.height<=self.y\
        +self.height):
            return True
        return False
