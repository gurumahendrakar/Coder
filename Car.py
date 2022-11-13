# #not completed
# from re import X
# from turtle import right, width
# import pygame
# window = pygame.display.set_mode((700,900))
# pygame.display.set_caption("Car Game")
# Falser = True
# pygame.init()
# P = True
# x=200
# y = 300
# z = 400
# zz = 500
# right_move = 800
# car_increase_y = 0 
# car_increase_x = 0
# car_increase_z = 0
# car_increase_zz = 0
# class Car:
    
#     @staticmethod
#     def multiple_cars(width : int , height: int):
#         global car_increase_y
#         import random
#         image = pygame.image.load(r"C:\Users\mahen\bitepy\yes\yes\photos\OIP__1_-removebg-preview.png")
#         image = pygame.transform.scale(image,(100,100))
#         window.blit(image,(width,height))
        

   
#     def Car_Move(self):
#         import random
#         global car_increase_y
#         global car_increase_x,car_increase_z,car_increase_zz
#         global i
#         image = pygame.image.load(r"C:\Users\mahen\bitepy\road.jpeg")
#         Gameover = False
#         left_move = 305
#         global right_move
#         while not Gameover:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     Gameover = True
                
#                 if event.type==pygame.KEYDOWN:
#                     if event.key==pygame.K_RIGHT:
#                         if left_move>540:
#                             left_move = 540
#                         else:
#                             left_move+=30

                    
#                     if event.key==pygame.K_LEFT:
#                         if left_move<68:
#                             left_move = 60
#                         else:
#                             left_move-=30
            

          
#             road_image = pygame.transform.scale(image, (600,1000))
#             window.blit(road_image,(57,0))
#             car_image = pygame.image.load(r"C:\Users\mahen\bitepy\yes\yes\photos\a6rBl.png")
#             car_image = pygame.transform.scale(car_image,(100,100))
#             window.blit(car_image,(left_move,right_move))
            
#             if car_increase_y==780 :
#                 import random
#                 global x,y,z,zz
#                 car_increase_y= 0
#                 y = random.randint(75,530)

#             if car_increase_x==780:
#                 car_increase_x = 0
#                 x = random.randint(75,530)

#             if car_increase_z ==783:
#                 import random
#                 car_increase_z= 0
#                 z = random.randint(75,530)

#             if car_increase_zz==768:
#                 car_increase_zz = 0
#                 zz = random.randint(75,530)
                

#             self.multiple_cars(x,car_increase_x)
#             self.multiple_cars(y,car_increase_y)
#             self.multiple_cars(z,car_increase_z)
#             self.multiple_cars(zz,car_increase_zz)
           
#             pygame.time.delay(50)
#             pygame.display.update()
#             car_increase_y+=15
#             car_increase_z+=27
#             car_increase_x+=39
#             car_increase_zz+=32
            
            
# c = Car()
# c.Car_Move()



