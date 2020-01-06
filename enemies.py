from tkinter import *
import os

#########RUN GAME ON jump.py FILE############

class Alien(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 60
        self.height = 40
        self.maxnum = 2
        self.photo = PhotoImage(file=\
            os.getcwd() + "/Images/alien1.gif")
#http://www.webdevils.com/wp-content/uploads/2011/12/Alien-32-Red_Default.gif
        self.label = Label(image = self.photo)
    def draw(self,canvas):
        canvas.create_image(self.x,self.y,anchor="nw",image=self.photo)
    def topcollide(self,x1,x2,y):
        if (x1 >= self.x and x1 < self.x+self.width and y<=self.y+self.height\
        and y>self.y-10) or (x2 >= self.x and x2 < self.x+self.width and \
        y<=self.y+self.height and y>self.y-10):
            return True
        return False
    def bottomcollide(self,x1,x2,y):
        if (x1 >= self.x and x1 < self.x+self.width and y<=self.y+self.height\
        and y>self.y-10) or (x2 >= self.x and x2 < self.x+self.width and \
        y<=self.y+self.height and y>self.y-10):
            return True
        return False

class EnemyAircraft(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 90
        self.height = 120
        self.dx = 5
        self.photo = PhotoImage(file=\
            os.getcwd() + "/Images/enemyaiircraft.gif")
#http://www.hedfiles.net/pixel/pirateA.gif
        self.label = Label(image=self.photo)
    def draw(self,canvas):
        canvas.create_image(self.x-85,self.y-65,anchor="nw",image=self.photo)
    def adjust(self,width):
        if self.x <= 0:
            self.dx = -self.dx
        elif self.x+self.width >= width:
            self.dx = -self.dx
    def collide(self,x1,x2,y):
        if (x1 >= self.x and x1 < self.x+self.width and y<=self.y+self.height\
        and y>self.y-10) or (x2 >= self.x and x2 < self.x+self.width and \
        y<=self.y+self.height and y>self.y-10):
            return True
        return False


class EnemyProjectile(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 3
        self.height = 20
        self.dy = 10
    def draw(self,canvas):
        canvas.create_rectangle(self.x,self.y,self.x+self.width,self.y+\
            self.height,fill="white")







