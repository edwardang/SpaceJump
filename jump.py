#########RUN GAME ON THIS FILE############

from animation import Animation
from tkinter import *
import random
import os
from module import Module
from module import Projectile
from module import MainMenuModule
from module import Computer
from module import Finish
from platforms import Platforms
from enemies import Alien
from enemies import EnemyAircraft
from enemies import EnemyProjectile
from powerups import PowerUp
from powerups import Fuel
from powerups import Protection

class JumpGame(Animation):

    def getplatforms(num,L,L2,width1,width2,height1,height2):
        count,ok,newlist = 0,True,L2
        while count < num:
            check = Platforms(random.randint(width1,width2),\
                random.randint(height1,height2))
            for platform in L:
                if platform.checkoverlap(check.x,check.y):
                    ok = False
                    break
            if ok == True:
                for platform in L2:
                    if platform.checkoverlap(check.x,check.y):
                        ok = False
                        break
            if ok:
                newlist.append(check)
                count+=1
            ok = True
        return newlist

    def latergetplatforms(L,L2,width1,width2,height):
        count,ok,newlist = 0,True,L2
        while count < 1:
            check = Platforms(random.randint(width1,width2),\
                height)
            for platform in L:
                if platform.checkoverlap(check.x,check.y):
                    ok = False
                    break
            if ok == True:
                for platform in L2:
                    if platform.checkoverlap(check.x,check.y):
                        ok = False
                        break
            if ok:
                newlist.append(check)
                count+=1
            ok = True
        return newlist

    def init(self):
        self.mode = "mainmenu"

        self.module = Module(self.width//2,self.height//2+10)
        self.essentialplatforms = [Platforms(self.width//2,self.height-20),\
        Platforms(random.randint(0,350),self.height-80),\
        Platforms(random.randint(0,350),self.height-140),\
        Platforms(random.randint(0,350),self.height-200),\
        Platforms(random.randint(0,350),self.height-260),\
        Platforms(random.randint(0,350),self.height-320),\
        Platforms(random.randint(0,350),self.height-380)]
        self.platforms = []
        self.platforms = JumpGame.getplatforms(10,self.essentialplatforms,\
            self.platforms,0,350,20,370)
        self.aliens = []
        self.projectiles = []
        self.enemyaircraft = []
        self.enemyprojectiles = []
        self.powerups = []

        self.startmodule = MainMenuModule(self.width//2+self.width//4+7,\
            self.height//2+50)
        self.startplatform = Platforms(self.width//2+self.width//4-10,\
            self.height - 30)

        self.instructionsmodule = MainMenuModule(self.width//10,105)
        self.instructionsalien = Alien(self.width//18,160)

        self.instructionsaircraft = EnemyAircraft(self.width//15+30,100)

        self.ground = 350

        self.maxplatforms = 10
        self.maxaliens = 2
        self.maxenemyaircrafts = 1
        self.maxenemyprojectiles = 7
        self.maxpowerups = 2
        self.deployable = True
        self.hitcount = 5
        self.aircrafthit = False


        self.movejump = True
        self.storage = None
        self.background = \
        PhotoImage(\
        file=os.getcwd() + "/Images/background1.gif")
        #https://media.giphy.com/media/8xK1CusSFTI0U/giphy.gif
        self.score = 0
        self.once = False #for updating aliens
        self.gameover = False
        self.fuel = False
        self.fuelscore = None
        self.protection = False
        self.protectionscore = None
        self.fuelprotection = False
        self.donespeed = None
        self.extrajumps = 3
        self.extrajumpscore = 0
        self.canshoot = True
        self.canshoottime = 0
        self.oldcanshoottime = 0
        self.ringcolor = "gold"

        self.dx = 0
        self.dy = -10

        ###RACE
        self.computer = Computer(self.width//2,self.height//2+10)
        self.currentplatform = None
        self.targetplatform = None
        self.oldtargetplatform = None
        self.movement = None
        self.first = False
        self.stopmoving = False
        self.racescore = 0
        self.youwin = False
        self.youlose = False
        self.finishline = True
        self.finish = []


####################################
# mode dispatcher
####################################


    def mousePressed(self,event):
        if (self.mode == "mainmenu"):
            JumpGame.mainmenuMousePressed(self,event)
        elif (self.mode == "spacejump"):
            JumpGame.spacejumpMousePressed(self,event)
        elif (self.mode == "instructions"):
            JumpGame.instructionsMousePressed(self,event)
        elif (self.mode == "instructionstwo"):
            JumpGame.instructionstwoMousePressed(self,event)
        elif(self.mode == "training"):
            JumpGame.trainingMousePressed(self,event)
        elif(self.mode == "race"):
            JumpGame.raceMousePressed(self,event)


    def keyPressed(self,event):
        if (self.mode == "mainmenu"):
            JumpGame.mainmenuKeyPressed(self,event)
        elif (self.mode == "spacejump"):
            JumpGame.spacejumpKeyPressed(self,event)
        elif (self.mode == "instructions"):
            JumpGame.instructionsKeyPressed(self,event)
        elif (self.mode == "instructions2:"):
            JumpGame.instructionstwoKeyPressed(self,event)
        elif (self.mode == "training"):
            JumpGame.trainingKeyPressed(self,event)
        elif(self.mode=="race"):
            JumpGame.raceKeyPressed(self,event)

    def timerFired(self):
        if (self.mode == "mainmenu"):
            JumpGame.mainmenuTimerFired(self)
        elif (self.mode == "spacejump"):
            JumpGame.spacejumpTimerFired(self)
        elif (self.mode == "instructions"):
            JumpGame.instructionsTimerFired(self)
        elif (self.mode == "instructionstwo"):
            JumpGame.instructionstwoTimerFired(self)
        elif (self.mode == "training"):
            JumpGame.trainingTimerFired(self)
        elif (self.mode == "race"):
            JumpGame.raceTimerFired(self)

    def redrawAll(self):
        if (self.mode == "mainmenu"):
            JumpGame.mainmenuRedrawAll(self)
        elif (self.mode == "spacejump"):
            JumpGame.spacejumpRedrawAll(self)
        elif (self.mode == "instructions"):
            JumpGame.instructionsRedrawAll(self)
        elif (self.mode == "instructionstwo"):
            JumpGame.instructionstwoRedrawAll(self)
        elif (self.mode == "training"):
            JumpGame.trainingRedrawAll(self)
        elif (self.mode == "race"):
            JumpGame.raceRedrawAll(self)

###### main menu ######


    def mainmenuMousePressed(self,event):
        if event.x > self.width//2-30 and event.x < self.width//2+30 and\
        event.y > self.height//2-15 and event.y < self.height//2+15:
            self.mode = "spacejump"
        elif event.x > self.width//2-45 and event.x < self.width//2+45 and\
        event.y>self.height//2+30 and event.y<self.height//2+60:
            self.mode = "instructions"
        elif event.x >= self.width//2-40 and event.x <= self.width//2+40 and\
        event.y>=self.height//2+75 and event.y<=self.height//2+105:
            self.mode = "training"
        elif event.x >= self.width//2-30 and event.x <= self.width//2+30 and\
        event.y>=self.height//2+120 and event.y<=self.height//2+150:
            self.mode = "race"


    def mainmenuKeyPressed(self,event):
        pass

    def mainmenuTimerFired(self):
        if self.startplatform.collide(self.startmodule.x,self.startmodule.x\
            +self.startmodule.width,self.startmodule.y+self.startmodule.height):
            self.startmodule.jump(self.startmodule.y+self.startmodule.height)
        self.startmodule.update(self.width,self.height)


    def mainmenuRedrawAll(self):
        self.canvas.create_image(0,0,anchor="nw",image=self.background)
        self.canvas.create_text(self.width//2,75,text="Space Jump",font=\
            "Arial 54",fill="white")
        self.canvas.create_rectangle(self.width//2-30,self.height//2-15,\
            self.width//2+30,self.height//2+15,fill="brown")
        self.canvas.create_text(self.width//2,self.height//2,text="Play")
        self.canvas.create_rectangle(self.width//2-45,self.height//2+30,\
            self.width//2+45,self.height//2+60,fill="brown")
        self.canvas.create_text(self.width//2,self.height//2+45,text=\
            "Instructions")
        self.canvas.create_rectangle(self.width//2-40,self.height//2+75,\
            self.width//2+40,self.height//2+105,fill="brown")
        self.canvas.create_text(self.width//2,self.height//2+90,\
            text="Training")
        self.canvas.create_rectangle(self.width//2-30,self.height//2+120,\
            self.width//2+30,self.height//2+150,fill="brown")
        self.canvas.create_text(self.width//2,self.height//2+135,\
            text="Race")
        self.startplatform.draw(self.canvas)
        self.startmodule.draw(self.canvas)
        


####### SPACE JUMP ##########
    def spacejumpMousePressed(self,event):
        #calculate slope
        x1 = event.x
        y1 = event.y
        x2 = self.module.x+self.module.width//4+8
        y2 = self.module.y-10

        dx = (x1-x2)/20
        dy = -10

        if y1 < self.module.y - 10:
            self.dx = dx
            self.dy = dy
            



    def spacejumpKeyPressed(self,event):
        if event.keysym == "Left":
            if self.module.speed > 0:
                self.module.speed = -1
            if self.module.speed >= -self.module.maxspeed:
                self.module.speed -= 2
        elif event.keysym == "Right":
            if self.module.speed < 0:
                self.module.speed = 1
            if self.module.speed <= self.module.maxspeed:
                self.module.speed += 2
        elif event.keysym == "Up":
            if not self.gameover and self.canshoot:
                self.projectiles.append(Projectile(self.module.x+\
                    self.module.width//4+8,self.module.y-10,self.dx,\
                    self.dy))
                self.canshoot = False
                self.oldcanshoottime = 0
                self.canshoottime = 0
        elif event.keysym == "Down":
            if self.module.upspeed > 0 and self.extrajumps > 0:
                self.module.jump(self.module.y)
                self.extrajumps -= 1
        if event.keysym == "b":
            
            JumpGame.init(self)

    def spacejumpTimerFired(self):
        if self.module.y+self.module.height>=self.height+12:
            self.gameover = True
        self.once = False
        if not self.gameover:
            if self.fuel and self.score-self.fuelscore >= 450:
                self.fuel = False
                self.ringcolor = "white"
                self.donespeed = self.module.upspeed
            if self.fuelprotection and not self.fuel and self.module.upspeed>=0:
                self.fuelprotection = False
                self.ringcolor = "gold"
            if self.protection and self.score-self.protectionscore>=1500:
                self.ringcolor="white"
            if self.protection and self.score-self.protectionscore>=2000:
                self.protection = False
                self.ringcolor = "gold"
            
            negatupspeed = -self.module.upspeed

            for eplatform in self.essentialplatforms:
                if eplatform.collide(self.module.x,self.module.x+\
                    self.module.width,self.module.y+self.module.height):
                    if self.module.upspeed>0:
                        self.module.jump(self.module.y+self.module.height)
                if eplatform.y >= self.height + 15:
                    self.essentialplatforms.remove(eplatform)
                    
                    self.essentialplatforms = JumpGame.latergetplatforms(\
                        self.platforms,self.essentialplatforms,0,350,-15)

            for platform in self.platforms:
                if platform.collide(self.module.x,self.module.x+\
                    self.module.width,self.module.y+self.module.height):
                    if self.module.upspeed > 0:
                        self.module.jump(self.module.y+self.module.height)

                #movement of platforms

            
                if platform.y >= self.height-15:
                    self.platforms.remove(platform)
                    if len(self.platforms) < self.maxplatforms:
                        self.platforms = JumpGame.latergetplatforms(\
                            self.essentialplatforms,self.platforms\
                            ,0,350,-15)

            if self.module.tempy<=self.height//2 and self.module.upspeed<0:
                for eplatform in self.essentialplatforms:
                    eplatform.y += negatupspeed
                    self.score+=1
                for platform in self.platforms:
                    platform.y += negatupspeed
                    
                for powerup in self.powerups:
                    powerup.y += negatupspeed
                    if powerup.y+powerup.height >= self.height:
                        self.powerups.remove(powerup)
                if self.aliens != [] and not self.once:
                    for alien in self.aliens:
                        alien.y += negatupspeed
                        if alien.y >= self.height:
                            self.aliens.remove(alien)
                    self.once = True

            #regarding aliens, jump on aliens/die from alien
            for alien in self.aliens:
                if alien.topcollide(self.module.x,self.module.x+self.module.\
                    width,self.module.y) and not self.protection and not \
                    self.fuelprotection:
                    self.gameover = True
                if alien.bottomcollide(self.module.x,self.module.x+self.module.\
                    width,self.module.y+self.module.height):
                    if self.module.upspeed > 0:
                        self.module.jump(self.module.y+self.module.height)
                        self.aliens.remove(alien)


            #projectiles
            for projectile in self.projectiles:
                projectile.x += projectile.dx
                projectile.y += projectile.dy
                if projectile.y <= 0 or projectile.x <= 0 or \
                projectile.x >= self.width:
                    self.projectiles.remove(projectile)

            for projectile in self.projectiles:
                for alien in self.aliens:
                    if alien.topcollide(projectile.x-projectile.r,projectile.x\
                        +projectile.r,projectile.y-projectile.r):
                        self.aliens.remove(alien)
                        self.projectiles.remove(projectile)
###THIS LINE ADDED IN
            for projectile in self.projectiles:
            #### double remove projectiles. FIX THIS
                if self.enemyaircraft != []:
                    if self.enemyaircraft[0].collide(projectile.x-\
                        projectile.r,projectile.x+projectile.r,\
                        projectile.y-projectile.r):
                        self.hitcount -= 1
                        self.aircrafthit = True
                        self.projectiles.remove(projectile)
                        if self.hitcount == 0:
                            self.enemyaircraft.pop()
                            self.hitcount = 10

            #powerups
            for powerup in self.powerups:
                if powerup.collide(self.module.x,self.module.x+\
                    self.module.width,self.module.y) or powerup.collide(\
                    self.module.x,self.module.x+self.module.width,\
                    self.module.y + self.module.height) and not \
                    self.fuelprotection:
                    self.powerups.remove(powerup)
                    self.ringcolor="gold"
                    if powerup.kind == "fuel":
                        self.fuelscore = self.score
                        self.fuelprotection = True
                        self.fuel = True
                    if powerup.kind == "protection":
                        
                        self.protectionscore = self.score
                        self.protection = True

            #enemy aircraft and it's projectiles
            if self.enemyaircraft != []:
                if abs(self.enemyaircraft[0].x+self.enemyaircraft[0].width//2\
                    -self.module.x+self.module.width//2) < 3:
                    self.enemyaircraft[0].dx = 0
                elif self.enemyaircraft[0].x+self.enemyaircraft[0].width//2<\
                self.module.x+self.module.width//2:
                    self.enemyaircraft[0].dx = 5
                elif self.enemyaircraft[0].x+self.enemyaircraft[0].width//2>=\
                self.module.x+self.module.width//2:
                    self.enemyaircraft[0].dx = -5
                self.enemyaircraft[0].x += self.enemyaircraft[0].dx
                
                self.enemyaircraft[0].adjust(self.width)

            if self.enemyaircraft != [] and\
            len(self.enemyprojectiles) < self.maxenemyprojectiles and \
            random.randint(1,15)==6:
                self.enemyprojectiles.append(EnemyProjectile(\
                    self.enemyaircraft[0].x+self.enemyaircraft[0].width//2,\
                    self.enemyaircraft[0].y+self.enemyaircraft[0].height))
            #eprojectile collide
            for eprojectile in self.enemyprojectiles:
                eprojectile.y += eprojectile.dy
                if self.module.collide(eprojectile.x,eprojectile.x+\
                    eprojectile.width,eprojectile.y+eprojectile.height) and \
                    not self.protection and not self.fuelprotection:
                    self.enemyprojectiles.remove(eprojectile)
                    self.gameover = True
                if eprojectile.y >= self.height:
                    self.enemyprojectiles.remove(eprojectile)

            #HIGHER YOU GO, MORE EXTRA JUMPS
            if self.score - self.extrajumpscore >= 3000:
                self.extrajumps += 1
                self.extrajumpscore = self.score

            #ADD aliens
            if self.score > 300 and len(self.aliens) < self.maxaliens and\
            random.randint(1,50) == 5:
                self.aliens.append(Alien(random.randint(0,self.width-30),\
                    -15))

            #CONTROL PROJECTILE SPAM
            self.module.update(self.width,self.height,self.fuel,\
                self.fuelprotection)
            self.canshoottime += 1
            if self.canshoottime - self.oldcanshoottime >= 4:
                self.canshoot = True

            #ADD ENEMY AIRCRAFT
            if self.score > 300 and len(self.enemyaircraft) <\
             self.maxenemyaircrafts and random.randint(1,250)==24:
                self.enemyaircraft.append(EnemyAircraft(10,10))
                #self.deployable = False

            #ADD POWERUP
            if self.score > 300 and len(self.powerups) <\
            self.maxpowerups and random.randint(1,100)==2:
                kind = random.randint(1,10)#random.choice(["fuel","protection"])
                if kind > 3:
                    self.powerups.append(Protection(random.randint(0,350),-15,\
                        "protection"))
                elif kind <=3:
                    self.powerups.append(Fuel(random.randint(0,350),-15,"fuel"))

            if self.score > 1000 and self.score < 2000:
                self.maxplatforms = 9

            if self.score >=2000 and self.score <4000:
                self.maxplatforms = 8

            if self.score >= 4000 and self.score<5000:
                self.maxplatforms = 6

            if self.score>=5000 and self.score<6000:
                self.maxplatforms=4

            if self.score>=6000 and self.score<7000:
                self.maxplatforms=2

            if self.score>=7000:
                self.maxplatforms=0

    def spacejumpRedrawAll(self):
        self.canvas.create_rectangle(-5,-5,500,500,fill="black")
        self.canvas.create_image(0,0,anchor="nw",image=self.background)
        for eplatform in self.essentialplatforms:
            eplatform.draw(self.canvas)
        for platform in self.platforms:
            platform.draw(self.canvas)
        for powerup in self.powerups:
            powerup.draw(self.canvas)
        for alien in self.aliens:
            alien.draw(self.canvas)
        for projectile in self.projectiles:
            projectile.draw(self.canvas)
        if not self.aircrafthit:
            for aircraft in self.enemyaircraft:
                aircraft.draw(self.canvas)
        self.aircrafthit = False
        for eprojectile in self.enemyprojectiles:
            eprojectile.draw(self.canvas)
        if self.protection or self.fuelprotection:
            self.canvas.create_oval(self.module.x-15,self.module.y-15,\
                self.module.x+self.module.width+15,self.module.y+\
                self.module.height+15,outline=self.ringcolor,width=7)
        self.module.draw(self.canvas)
        self.canvas.create_rectangle(0,0,self.width+20,30,fill="black")
        self.canvas.create_line(0,27,self.width+20,27,fill="white",\
            width = 3)
        self.canvas.create_text(5,5,anchor="nw",text="Score : "+\
            str(self.score),fill="white")
        self.canvas.create_text(100,5,anchor="nw",text="Extra Jumps: " + \
            str(self.extrajumps),fill="white")
        if self.gameover:
            self.canvas.create_image(self.module.x-5,self.module.y-55,\
                anchor="nw",image=self.module.deadphoto)
            self.canvas.create_rectangle(self.width//2-100,30,self.width//2+\
                100,130,fill="black",outline="white",width=3)

            self.canvas.create_text(self.width//2,70,\
                text="GAME OVER",fill="red",font="Arial 26")

            self.canvas.create_text(self.width//2,100,\
                text="Press (b) to escape",fill="white",\
                font="Arial 16")
            

### INSTRUCTIONS1 ###

    def instructionsMousePressed(self,event):
        
        if event.x>=340 and event.x<=385 and event.y>=360 and event.y<=385:
            self.mode="instructionstwo"

    def instructionsKeyPressed(self,event):
        if event.keysym == "b":
            JumpGame.init(self)

    def instructionsTimerFired(self):
        pass

    def instructionsRedrawAll(self):
        self.canvas.create_image(0,0,anchor="nw",image=self.background)
        self.canvas.create_text(10,10,anchor="nw",\
            text="You're out in space \n\t and you've ran out of fuel......",\
            fill="white",font="Arial 18")
        self.canvas.create_text(self.width//2,60,anchor="n",\
            text="How to Play",fill="white",font="Arial 28")
        
        self.canvas.create_line(10,95,10,390,fill="white")
        self.canvas.create_line(10,95,390,95,fill="white")
        self.canvas.create_line(390,95,390,390,fill="white")
        self.canvas.create_line(10,390,390,390,fill="white")
        self.instructionsmodule.draw(self.canvas)
        self.canvas.create_text(self.width//4,105,anchor="nw",text=\
            "That's you, press left and right arrow keys\nto set direction",\
            fill="white")
        self.instructionsalien.draw(self.canvas)
        self.canvas.create_text(self.width//4,160,anchor="nw",text=\
            "Avoid aliens at all costs,\nunless you are able to jump on them",\
            fill="white")
        self.canvas.create_rectangle(self.width//14,240,self.width//14+50,255,\
        fill="gray")
        self.canvas.create_text(self.width//4,240,anchor="nw",\
            text="Jump on these to survive",fill="white")



        self.canvas.create_rectangle(self.width//10,290,self.width//10+25,290+\
            25,fill="cyan")
        self.canvas.create_oval(self.width//10,290,self.width//10+25,290+\
            25,fill="green")
        self.canvas.create_text(self.width//10+12,290+12,\
            text="P")

        self.canvas.create_rectangle(self.width//10,320,self.width//10+25,320+\
            25,fill="brown")
        self.canvas.create_oval(self.width//10,320,self.width//10+25,320+\
            25,fill="green")
        self.canvas.create_text(self.width//10+12,320+12,\
            text="F")
        self.canvas.create_text(self.width//4,300,text=\
"These are powerups. Try to get them.\nThey will help you \
stay alive\nor increase your score",\
        anchor="nw",fill="white")

        self.canvas.create_rectangle(340,360,385,385,fill="white",\
            outline="white")
        self.canvas.create_text(362,372,text="Next")

        

####INSTRUCTIONS TWO####

    def instructionstwoMousePressed(self,event):
        if event.x>=10 and event.x<=55 and event.y>=355 and event.y<=390:
            self.mode = "instructions"
        if event.x>=340 and event.x<=385 and event.y>=360 and event.y<=385:
            JumpGame.init(self)

    def instructionstwpKeyPressed(self,event):
        if event.keysym == "b":
            JumpGame.init(self)

    def instructionstwoTimerFired(self):
        pass

    def instructionstwoRedrawAll(self):
        self.canvas.create_image(0,0,anchor="nw",image=self.background)
        self.canvas.create_text(10,10,anchor="nw",\
            text="You're out in space \n\t and you've ran out of fuel......",\
            fill="white",font="Arial 18")
        self.canvas.create_text(self.width//2,60,anchor="n",\
            text="How to Play",fill="white",font="Arial 28")
        self.canvas.create_line(10,95,10,390,fill="white")
        self.canvas.create_line(10,95,390,95,fill="white")
        self.canvas.create_line(390,95,390,390,fill="white")
        self.canvas.create_line(10,390,390,390,fill="white")
        
        self.instructionsaircraft.draw(self.canvas)
        self.canvas.create_text(self.width//2,140,\
            text="Be careful of the spaceships.\nThey will shoot at you.",\
            fill = "white",anchor="nw")

        self.canvas.create_text(self.width//2+4,260,text=\
    "To shoot, press the up key. You can control the\
    \ndirection of your shot by clicking in\nthe direction you prefer.",\
    fill="white")
        self.canvas.create_text(self.width//2+5,319,text=\
            "Your score increases the higher you go.",fill="white",\
            font="Arial 14")
        self.canvas.create_text(self.width//2+5,350,\
            text="Good luck!",fill="white",font="Arial 20")
        


        self.canvas.create_rectangle(15,360,60,385,fill="white",\
            outline="white")
        self.canvas.create_text(37,372,text="Back")

        self.canvas.create_rectangle(340,360,385,385,fill="white",\
            outline="white")
        self.canvas.create_text(362,372,text="Menu")




#### TRAINING MODE #######

    def trainingMousePressed(self,event):
        pass

    def trainingKeyPressed(self,event):
        if event.keysym == "Left":
            if self.module.speed > 0:
                self.module.speed = -1
            if self.module.speed >= -self.module.maxspeed:
                self.module.speed -= 2
        elif event.keysym == "Right":
            if self.module.speed < 0:
                self.module.speed = 1
            if self.module.speed <= self.module.maxspeed:
                self.module.speed += 2
        elif event.keysym == "Down":
            if self.module.upspeed > 0 and self.extrajumps > 0:
                self.module.jump(self.module.y)
                self.extrajumps -= 1
        if event.keysym == "b":
            JumpGame.init(self)
        

    def trainingTimerFired(self):
        if self.module.y+self.module.height>=self.height+12:
            self.gameover = True
        self.once = False
        if not self.gameover:
            negatupspeed = -self.module.upspeed

            for eplatform in self.essentialplatforms:
                if eplatform.collide(self.module.x,self.module.x+\
                    self.module.width,self.module.y+self.module.height):
                    if self.module.upspeed>0:
                        self.module.jump(self.module.y+self.module.height)
                if eplatform.y >= self.height + 15:
                    self.essentialplatforms.remove(eplatform)
                    self.essentialplatforms = JumpGame.latergetplatforms(\
                        self.platforms,self.essentialplatforms,0,350,-15)

            for platform in self.platforms:
                if platform.collide(self.module.x,self.module.x+\
                    self.module.width,self.module.y+self.module.height):
                    if self.module.upspeed > 0:
                        self.module.jump(self.module.y+self.module.height)


                    
            
                if platform.y >= self.height+15:
                    self.platforms.remove(platform)
                    if len(self.platforms) < self.maxplatforms:
                        self.platforms = JumpGame.latergetplatforms(\
                            self.essentialplatforms,self.platforms\
                            ,0,350,-15)

            
            if self.module.tempy<=self.height//2 and self.module.upspeed<0:
                for eplatform in self.essentialplatforms:
                    eplatform.y += negatupspeed
                    self.score += 1
                for platform in self.platforms:
                    platform.y += negatupspeed
                    

            self.module.update(self.width,self.height,False,False)


            if self.score > 200 and self.score < 400:
                self.maxplatforms = 9

            if self.score >=400 and self.score <600:
                self.maxplatforms = 7

            if self.score >= 600 and self.score<800:
                self.maxplatforms = 5

            if self.score>=800 and self.score<1000:
                self.maxplatforms=4

            if self.score>=1000 and self.score<1200:
                self.maxplatforms=3

            if self.score>=1200 and self.score<1400:
                self.maxplatforms=2

            if self.score>=1400:
                self.maxplatforms=0
        

    def trainingRedrawAll(self):
        self.canvas.create_rectangle(-5,-5,500,500,fill="black")
        self.canvas.create_image(0,0,anchor="nw",image=self.background)
        for platform in self.platforms:
            platform.draw(self.canvas)
        for eplatform in self.essentialplatforms:
            eplatform.draw(self.canvas)
        self.module.draw(self.canvas)#,self.gameover)
        self.canvas.create_rectangle(0,0,self.width+20,30,fill="black")
        self.canvas.create_line(0,27,self.width+20,27,fill="white",\
            width = 3)
        self.canvas.create_text(5,5,anchor="nw",text="Score : "+\
            str(self.score),fill="white")
        self.canvas.create_text(100,5,anchor="nw",text="Extra Jumps: " + \
            str(self.extrajumps),fill="white")
        if self.gameover:
            self.canvas.create_image(self.module.x-5,self.module.y-55,\
                anchor="nw",image=self.module.deadphoto)
            self.canvas.create_rectangle(self.width//2-100,30,self.width//2+\
                100,130,fill="black",outline="white",width=3)

            self.canvas.create_text(self.width//2,70,\
                text="GAME OVER",fill="red",font="Arial 26")

            self.canvas.create_text(self.width//2,100,\
                text="Press (b) to escape",fill="white",\
                font="Arial 16")

###RACING MODE

    def raceMousePressed(self,event):
        pass

    def raceKeyPressed(self,event):
        if event.keysym == "Left":
            if self.module.speed > 0:
                self.module.speed = -1
            if self.module.speed >= -self.module.maxspeed:
                self.module.speed -= 2
        elif event.keysym == "Right":
            if self.module.speed < 0:
                self.module.speed = 1
            if self.module.speed <= self.module.maxspeed:
                self.module.speed += 2
        elif event.keysym == "Down":
            if self.module.upspeed > 0 and self.extrajumps > 0:
                self.module.jump(self.module.y)
                self.extrajumps -= 1
        if event.keysym == "b":
            JumpGame.init(self)

    def raceTimerFired(self):
        if self.module.y+self.module.height>=self.height+12:
            self.gameover = True
            self.youlose = True
        if self.score >= 1800 and self.finishline:
            self.finish.append(Finish(0,-200,self.width))
            self.finishline = False
        if self.finish != []:
            if self.module.y <= self.finish[0].y:
                self.gameover = True
                self.youwin = True
            elif self.computer.y <= self.finish[0].y:
                self.gameover = True
                self.youlose = True

        

        if self.racescore>=4000:
            self.gameover = True
            self.youlose = True
        
        if not self.gameover:
            negatupspeed = -self.module.upspeed

            for eplatform in self.essentialplatforms:
                if eplatform.collide(self.module.x,self.module.x+\
                    self.module.width,self.module.y+self.module.height):
                    if self.module.upspeed>0:
                        self.module.jump(self.module.y+self.module.height)

                if eplatform.collide(self.computer.x,self.computer.x+\
                    self.computer.width,self.computer.y+self.computer.height):
                    if self.computer.upspeed > 0:
                        self.computer.jump(self.computer.y+self.computer.height)
                        self.currentplatform=eplatform
                        self.first,self.stopmoving = True,False
                        self.computer.speed = 0
                        for eplatform in self.essentialplatforms:
                            
                            if eplatform.y<self.currentplatform.y and \
                            self.currentplatform.y-eplatform.y<=200:
                                self.targetplatform = eplatform
                                break

                       
                if eplatform.y >= self.height + 15:
                    self.essentialplatforms.remove(eplatform)
                    self.essentialplatforms = JumpGame.latergetplatforms(\
                        self.platforms,self.essentialplatforms,0,350,-15)

            for platform in self.platforms:
                if platform.collide(self.module.x,self.module.x+\
                    self.module.width,self.module.y+self.module.height):
                    if self.module.upspeed > 0:
                        self.module.jump(self.module.y+self.module.height)
                if platform.collide(self.computer.x,self.computer.x+\
                    self.computer.width,self.computer.y+self.computer.height):
                    if self.computer.upspeed > 0:
                        self.computer.jump(self.computer.y+self.computer.height)
                        self.currentplatform = platform
                        self.first,self.stopmoving = True,False
                        self.computer.speed = 0
                        for eplatform in self.essentialplatforms:
                            if eplatform.y<self.currentplatform.y and \
                            self.currentplatform.y-eplatform.y<=200:
                                self.targetplatform = eplatform
                                break
                        
            
                if platform.y >= self.height+15:
                    self.platforms.remove(platform)
                    if len(self.platforms) < self.maxplatforms:
                        self.platforms = JumpGame.latergetplatforms(\
                            self.essentialplatforms,self.platforms\
                            ,0,350,-15)

            if self.computer.y>=self.height+self.width//2:
                if random.randint(1,10)<11:
                    self.computer.x = random.randint(0,375)
                    self.computer.y = self.height+160
                    self.computer.jump(self.computer.y+self.computer.height)
                    for eplatform in self.essentialplatforms:
                        if eplatform.y<self.computer.y+self.computer.height and\
                         self.computer.y+self.computer.height<=400:
                            self.targetplatform = eplatform
                            break


            if self.module.tempy<=self.height//2 and self.module.upspeed<0:
                if self.finish != []:
                    self.finish[0].y += negatupspeed
                for eplatform in self.essentialplatforms:
                    eplatform.y += negatupspeed
                    self.score += 1
                for platform in self.platforms:
                    platform.y += negatupspeed
                self.computer.y += negatupspeed

            if self.computer.y+self.computer.height<25:
                self.racescore += 5
            if self.computer.upspeed<0:
                self.racescore += 4
            if self.computer.y<self.module.y and \
            self.module.y-self.computer.y<225:
                self.racescore = self.score + 100
            elif self.computer.y>self.module.y and \
            self.computer.y-self.module.y<300:
                self.racescore = self.score - 100

            if self.first:

                if self.targetplatform != None and \
                self.targetplatform.x > self.currentplatform.x:
                    distance1 = self.targetplatform.x - self.currentplatform.x
                    distance2 = (self.width-self.targetplatform.x)+\
                    self.currentplatform.x
                    
                    
                elif self.targetplatform != None and self.targetplatform.x <=\
                 self.currentplatform.x:
                    distance1 = (self.width-self.currentplatform.x)+\
                    self.targetplatform.x
                    distance2 = self.currentplatform.x-self.targetplatform.x

                if distance1 <= distance2:
                    self.movement = "right"

                elif distance2 < distance1:
                    self.movement = "left"


                if self.movement == "right" and not self.stopmoving:
                    if self.computer.speed <= 0:
                        self.computer.speed = 4
                    if self.computer.speed <= self.computer.maxspeed:
                        self.computer.speed += 2

                if self.movement == "left" and not self.stopmoving:
                    if self.computer.speed > 0:
                        self.computer.speed = -4
                    if self.computer.speed >= -self.module.maxspeed:
                        self.computer.speed -= 2

                if  self.targetplatform != None and self.computer.x+\
                    self.computer.width//2>=self.targetplatform.x and\
                    self.computer.x+self.computer.width//2<=\
                    self.targetplatform.x+self.targetplatform.width\
                    and self.computer.y<=self.targetplatform.y:
                    
                    self.computer.speed = 0
                    



            self.computer.update(self.width,self.height,False,False)
            self.module.update(self.width,self.height,False,False)


            if self.score > -1 and self.score < 300:
                self.maxplatforms = 9

            if self.score >=300 and self.score <600:
                self.maxplatforms = 8

            if self.score >= 600 and self.score<900:
                self.maxplatforms = 7

            if self.score>=900 and self.score<1200:
                self.maxplatforms=6

            if self.score>=1200 and self.score<1500:
                self.maxplatforms=5

            if self.score>=1500:
                self.maxplatforms=4


    def raceRedrawAll(self):
        self.canvas.create_rectangle(-5,-5,500,500,fill="black")
        self.canvas.create_image(0,0,anchor="nw",image=self.background)
        if self.finish != []:
            self.finish[0].draw(self.canvas)
        for platform in self.platforms:
            platform.draw(self.canvas)
        for eplatform in self.essentialplatforms:
            eplatform.draw(self.canvas)
        self.computer.draw(self.canvas)
        self.module.draw(self.canvas)
        self.canvas.create_rectangle(0,0,self.width+20,30,fill="black")
        self.canvas.create_line(0,27,self.width+20,27,fill="white",\
            width = 3)
        self.canvas.create_text(5,5,anchor="nw",text="Score : "+\
            str(self.score),fill="white")
        self.canvas.create_text(100,5,anchor="nw",text="Extra Jumps: " + \
            str(self.extrajumps),fill="white")
        if self.gameover and self.youwin:
            #self.canvas.create_image(self.module.x-5,self.module.y-55,\
            #    anchor="nw",image=self.module.deadphoto)
            self.canvas.create_rectangle(self.width//2-100,30,self.width//2+\
                100,130,fill="black",outline="white",width=3)

            self.canvas.create_text(self.width//2,70,\
                text="YOU WIN",fill="green",font="Arial 26")

            self.canvas.create_text(self.width//2,100,\
                text="Press (b) to escape",fill="white",\
                font="Arial 16")

        if self.gameover and self.youlose:
            self.canvas.create_image(self.module.x-5,self.module.y-55,\
                anchor="nw",image=self.module.deadphoto)
            self.canvas.create_rectangle(self.width//2-100,30,self.width//2+\
                100,130,fill="black",outline="white",width=3)

            self.canvas.create_text(self.width//2,70,\
                text="YOU LOSE",fill="red",font="Arial 26")

            self.canvas.create_text(self.width//2,100,\
                text="Press (b) to escape",fill="white",\
                font="Arial 16")
        

game1 = JumpGame()
game1.run(400,400)