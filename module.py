from tkinter import *
import os

#########RUN GAME ON jump.py FILE############


class Module(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tempy = y
        self.width = 32 
        self.height = 30
        self.up = False
        self.actualup = False
        self.down = True
        self.upspeed = 10
        self.speed = 0
        self.maxspeed = 20
        self.max = 70
        self.collidey=350
        self.amtmoved = 0
        self.photo = PhotoImage(file=\
            os.getcwd() + "/Images/spacebot.gif").zoom(1,1)
#https://static.maplewiki.net/b/b0/Small_Spaceship.gif
        self.label = Label(image=self.photo)
        self.deadphoto = PhotoImage(\
            file=os.getcwd() + "/Images/explosion.gif")
#http://myzone.kayakmorris.netdna-cdn.com/wp-content/uploads/2014/12/
        self.label2 = Label(image=self.deadphoto)

    def draw(self,canvas):
        canvas.create_image(self.x,self.y,anchor="nw",image=self.photo)

    def jump(self,y):
        self.up,self.actualup,self.down = True,True,False
        self.collidey = y
        self.upspeed = -10
        
    def collide(self,x1,x2,y):
        if (x1 >= self.x and x1 < self.x+self.width and y<=self.y+self.height\
        and y>self.y-10) or (x2 >= self.x and x2 < self.x+self.width and \
        y<=self.y+self.height and y>self.y-10):
            return True
        return False

    def update(self,width,height,fuel,fuelprotection):
        if not fuel:
            if fuelprotection:
                self.y = height//2
            if self.up and not self.down:
                self.upspeed -= 2

            if self.tempy <= self.collidey-self.max:
                self.up,self.down = False,True

            if self.down and not self.up:
                self.upspeed += 2
            if self.x <= 0:
                self.x = width - self.width
            elif self.x >= width:
                self.x = 0
            self.x += self.speed
            self.tempy += self.upspeed
            if (self.y >= height//2 or self.upspeed > 0) and not fuelprotection:
                self.y += self.upspeed
                self.tempy = self.y

        elif fuel and fuelprotection:
            self.upspeed = -55
            self.tempy += self.upspeed
            self.y = height//2
            if self.x <= 0:
                self.x = width - self.width
            elif self.x >= width:
                self.x = 0
            self.x += self.speed
        


class MainMenuModule(Module):
    def __init__(self,x,y):
        super().__init__(x,y)
    def draw(self,canvas):
        super().draw(canvas)
    def jump(self,y):
        super().jump(y)
    def update(self,width,height):
        super().update(width,height,False,False)

class Projectile(object):
    def __init__(self,x,y,dx,dy):
        self.x = x
        self.y = y
        self.r = 4
        self.dx = dx
        self.dy = dy
    def draw(self,canvas):
        canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y\
            +self.r,fill="white")


class Computer(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tempy = y
        self.width = 32 
        self.height = 30 
        self.up = False
        self.actualup = False
        self.down = True
        self.upspeed = 10
        self.speed = 0
        self.maxspeed = 12
        self.max = 70
        self.collidey=350
        self.amtmoved = 0
        self.photo = PhotoImage(file=\
            os.getcwd() + "/Images/weirdalien.gif").zoom(1,1)
        #http://pixeljoint.com/files/icons/paxship_05.gif
        self.label = Label(image=self.photo)
        self.deadphoto = PhotoImage(\
            file=os.getcwd() + "/Images/explosion.gif")
    #http://myzone.kayakmorris.netdna-cdn.com/wp-content/uploads/2014/12/
    #explosion2_e0_5jmx.gif
        self.label2 = Label(image=self.deadphoto)
    def draw(self,canvas):

        #canvas.create_rectangle(self.x,self.y,self.x+self.width,self.y\
        #    +self.height,fill = "cyan")
        canvas.create_image(self.x-15,self.y-33,anchor="nw",image=self.photo)
        
    def jump(self,y):
        self.up,self.actualup,self.down = True,True,False
        self.collidey = y
        self.upspeed = -10
        
    def collide(self,x1,x2,y):
        if (x1 >= self.x and x1 < self.x+self.width and y<=self.y+self.height\
        and y>self.y-10) or (x2 >= self.x and x2 < self.x+self.width and \
        y<=self.y+self.height and y>self.y-10):
            return True
        return False

    def update(self,width,height,fuel,fuelprotection):

        if not fuel:

            if self.up and not self.down:
                self.upspeed -= 2

        
            if self.tempy <= self.collidey-self.max:
                self.up,self.down = False,True

            if self.down and not self.up:
                self.tempy = self.y
                self.upspeed += 2
            if self.x <= 0:
                self.x = width - self.width
            elif self.x >= width:
                self.x = 0
            self.x += self.speed
            self.tempy += self.upspeed
            self.y += self.upspeed
            

class Finish(object):
    def __init__(self,x,y,width):
        self.x = x
        self.y = y
        self.width = width
        self.height = 50
    def draw(self,canvas):
        canvas.create_rectangle(self.x,self.y,self.x+self.width,self.y+\
            self.height,fill="gold")
        canvas.create_text(self.x+self.width//2,self.y+self.height//2,\
            text="FINISH",font="Arial 36")


