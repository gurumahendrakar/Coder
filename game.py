import os

from PIL import Image
import pygame
import itertools
import pprint
import PIL
import math
import time

class game:

    def __init__(self):
        self.display = pygame.display.set_mode((1280,720))
        pygame.display.set_caption('Paradox')
        pygame.display.set_icon(pygame.image.load('S:/pygame/icon.webp'))
        self.bg = pygame.image.load('S:/pygame/bg.jpg')
        self.top = self.display.get_height()-140
        self.x = 0



        self.fps = 60
        self.a,self.b = 1280,0


    def key_pressed(self,event):
        print('---')

        if event.key== pygame.K_LEFT:
            self.x = self.x-30

        elif event.key== pygame.K_RIGHT:
            self.display.blit(pygame.image.load(r"S:/pygame/walkingimage.png"),(0,0))
            pygame.display.update()
            self.x = self.x+30

        elif event.key== pygame.K_UP:
            self.top = self.top-50

        elif event.key==pygame.K_DOWN:
            if self.top<self.display.get_height()-140:  self.top = self.top+50


    def _mainloop(self):

        while True:

            def _backbackground():
                if self.a == 0:
                    print('Entered')
                    self.a = 1280

                self.a -= 5

                self.display.fill('white')
                self.display.blit(self.bg, (-(self.bg.get_width() - self.a),0))
                self.display.blit(self.bg, (self.a, 0))

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    self.key_pressed(event)


            pygame.time.Clock().tick(self.fps)
            _backbackground()


            self.display.blit(pygame.image.load('S:\pygame\R (3).png'), (self.x, self.top))
            self.display.blit(pygame.image.load(r"S:\pygame\aid1348298-v4-728px-Get-Green-Grass-Step-6-removebg-preview.png"),
                              (0,self.display.get_height()-40))
            pygame.display.update()



game_ = game()
game_._mainloop()
# C:\Users\mahen\OneDrive\Pictures\28-12-2022 01_56_59.png