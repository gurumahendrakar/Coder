import os

from PIL import Image
import pygame
import itertools
import pprint
import PIL
import math
import time
import numpy

class game:

    def __init__(self):
        #234 % 30
        self.display = pygame.display.set_mode((1280,720))
        self.random1 = [numpy.random.randint(low=700,high=800),numpy.random.randint(300,400)]

        print(self.random1)
        self.random2 = numpy.random.randint(400, 500, size=2)
        self.entered = False
        print('Random1 --- ',self.random1,'Random2 --- ',self.random2,pygame.image.load('S:/pygame/stairs.png').get_width())


        self.last_movement = 0
        pygame.display.set_caption('Paradox')
        pygame.display.set_icon(pygame.image.load('S:/pygame/icon.webp'))

        self.bg = pygame.image.load('S:/pygame/bg.jpg')
        self.top = self.display.get_height()-140
        self.x = 0

        self.stand_ = dict(left='S:/pygame/standleft.png', right='S:/pygame/standright.png')
        self.sitting_value  = 'right'
        self.sittingImage = {'left':'S:/pygame/standleft.png','right':'S:/pygame/standright.png'}



        self.fps = 60
        self.a,self.b = 1280,0


    def _mainloop(self):

        while True:

            def _backbackground():
                if self.a == 0:
                    self.a = 1280

                self.a -= 5

                self.display.fill('white')
                self.display.blit(self.bg, (-(self.bg.get_width() - self.a),0))
                self.display.blit(self.bg, (self.a, 0))

            for event in pygame.event.get():
                self.eventt = event
                if event.type==pygame.QUIT:
                    exit()


            _backbackground()

            if self.eventt.type!= pygame.KEYDOWN:

                self.display.blit(pygame.image.load(self.sittingImage[self.sitting_value]), (self.x, self.top))
            else:
                if self.eventt.key == pygame.K_RIGHT:
                    if self.x < self.display.get_width()-100:
                        self.x+=10

                    self.sitting_value = 'right'
                    self.display.blit(pygame.image.load(r'S:/pygame/rightwalking.png'), (self.x, self.top))


                elif self.eventt.key==pygame.K_UP:
                    if 0<self.top:
                        self.top = self.top-20

                    self.display.blit(pygame.image.load(self.stand_[self.sitting_value]), (self.x + 10, self.top))

                #338
                elif self.eventt.key == pygame.K_DOWN:

                    if self.top<self.display.get_height()-140:

                        self.top  = self.top+5
                    self.display.blit(pygame.image.load(self.stand_[self.sitting_value]), (self.x + 10, self.top))

                elif self.eventt.key == pygame.K_LEFT:
                    if self.x>=0:
                        self.x  = self.x-10
                    self.sitting_value = 'left'
                    self.display.blit(pygame.image.load(r'S:/pygame/leftwalking.png'), (self.x + 10, self.top))


            self.display.blit(pygame.image.load(r"S:\pygame\aid1348298-v4-728px-Get-Green-Grass-Step-6-removebg-preview.png"),
                              (0,self.display.get_height()-40))

            #x---> 561,561+300 y----> 590---->


            #sliders ko left right karneka hai
            if self.x>self.last_movement:
                def stair_completeing_Check():

                    if self.random1[0]< -310:
                        self.random1 =self.random1 = numpy.random.randint(500,600,size=2)
                    elif self.random2[0]< - 310:
                        self.random2 = numpy.random.randint(300, 400, size=2)


                self.last_movement = self.x
                self.random1[0]-= 10
                self.random2[0]-= 10
                stair_completeing_Check()

            #automatic niche aana ka hai
            if self.top<self.display.get_height()-120:
                if not self.entered:
                    self.top+=5

            if self.x>self.random1[0]-50 and self.x<self.random1[0]+312 and self.top<self.random1[1]-100 :
                print('----Random 1 -----')
                self.entered = True
                if self.top<self.random1[1]-120 and not self.x>self.random1[0] and self.x<self.random1[1]:
                    self.top+=5
            else:
                self.entered = False


            if self.x>self.random2[0]-50 and self.x<self.random2[0]+312 and self.top<self.random2[1]-100:
                print('---------Random 2 Range---------')
                self.entered = True
                if self.top<self.random2[1]-120:
                    self.top+=10
            else:
                self.entered = False



            self.display.blit(pygame.image.load(r'S:/pygame/stairs.png'),self.random1)
            self.display.blit(pygame.image.load(r'S:/pygame/stairs.png'), self.random2)
            pygame.display.update()

game_ = game()
game_._mainloop()
# C:\Users\mahen\OneDrive\Pictures\28-12-2022 01_56_59.png