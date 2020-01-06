from tkinter import *

class PowerUp(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
    def draw(self,canvas,color="red",text="blah"):
        canvas.create_rectangle(self.x,self.y,self.x+self.width,self.y+\
            self.height,fill=color)
        canvas.create_oval(self.x,self.y,self.x+self.width,self.y+self.height,\
            fill="green")
        canvas.create_text(self.x+self.width//2,self.y+self.height//2,\
            text=text)
    def collide(self,x1,x2,y):
        if (x1 >= self.x and x1 < self.x+self.width and y<=self.y+self.height\
        and y>self.y-10) or (x2 >= self.x and x2 < self.x+self.width and \
        y<=self.y+self.height and y>self.y-10):
            return True
        return False

class Fuel(PowerUp):
    def __init__(self,x,y,kind):
        super().__init__(x,y)
        self.kind = kind
    def draw(self,canvas,color="brown",text="F"):
        super().draw(canvas,"brown","F")

class Protection(PowerUp):
    def __init__(self,x,y,kind):
        super().__init__(x,y)
        self.kind = kind
    def draw(self,canvas,color="cyan",text="P"):
        super().draw(canvas,"cyan","P")
