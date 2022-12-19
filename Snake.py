
Gameover = False
x=50 ;  y = 50
running = 0
running2 = 0
import  random
snakesize = 10
snakelist = [(50,50)]

import pygame


foodinteger = random.choice(list(range(200,900)))
score = 0
class Snake:
    global snakelist; global snakesize
    x = 50
    y= 50

    Over = False
    Display = pygame.display.set_mode((1920,1000))

    def __init__(self):
        pygame.display.set_caption("Snake Game")

    def music(self, song):
        import pygame
        pygame.mixer.init()

        pygame.mixer.music.load(song)
        pygame.mixer.music.play()


    @staticmethod
    def plot_snake(gamewindow,color,snakelist,snakesize):
        for x,y in snakelist:
            print(' : ' ,snakelist)
            pygame.draw.rect(gamewindow,color,[x,y,snakesize,snakesize])
    @staticmethod
    def food(surface,Color,x_size,y_size,foodsize):
        global snakesize
        global  foodinteger
        global score
        if abs(Snake.x - foodinteger)<20  and abs(Snake.y - foodinteger )<20:
            Snake().music(r"C:\Users\mahen\Downloads\snake (1).mp3")


            foodinteger = random.choice(list(range(200,900,10)))
            pygame.draw.rect(surface,Color,[x_size,y_size,foodsize,foodsize])
            snakesize+= 3
            score += 10
        else:
            pygame.draw.rect(surface, Color, [x_size, x_size, foodsize,foodsize])
    @staticmethod
    def MovementControl(event):
        global running,running2
        if event.key == pygame.K_UP:

            running2 = 0
            running  = -23
        if event.key == pygame.K_DOWN:

            running2 = 0
            running = +23
        if event.key  == pygame.K_LEFT:

            running = 0
            running2 = -23

        if event.key == pygame.K_RIGHT:
            running = 0
            running2  = 23


    def run(self):
        import pygame
        clock = pygame.time.Clock()

        global x,y
        global snakesize
        global snakelist
        global  running,running2
        pygame.font.init()

        var = 0

        while not Snake.Over:
            if var%240==0:
                self.music(r"C:\Users\mahen\Downloads\loco_contigo.mp3")

            var+= 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Snake.Over = True
                if event.type == pygame.KEYDOWN:
                    self.MovementControl(event= event)

            a = pygame.font.Font(r"C:\Users\mahen\bitepy\yes\yes\photos\BrusselsCityPersonalUsed-L3Lon.otf",22)
            Snake.x+= running2
            Snake.y += running
            b =  a.render(f'Score : {score}',True,'brown')
            Snake.Display.fill('white')
            Snake.Display.blit(b, (1920/2-100, 0))



            if Snake.x <0 or Snake.x > 1920 or Snake.y <0 or 1000<Snake.y:
                snakelist.clear()
                if Snake.x<0:
                    Snake.x = 1900;Snake.y = Snake.y
                    snakelist.append([Snake.x,Snake.y])

                elif Snake.y<0:
                    snakelist.clear()
                    if Snake.y < 0:
                        Snake.x = Snake.x
                        Snake.y = 1000
                        snakelist.append([Snake.x, Snake.y])

                elif Snake.x>1920:
                    snakelist.clear()
                    if Snake.x > 1920:
                        Snake.x = 0
                        Snake.y = Snake.y
                        snakelist.append([Snake.x, Snake.y])

                elif Snake.y>1000:

                    Snake.x = Snake.x
                    Snake.y = 0
                    snakelist.append([Snake.x, Snake.y])


            if len(snakelist)>snakesize:
                del snakelist[0:10]
            # if len(set((snakelist)))>1:
            #     if list(set(snakelist))[-1] in list(set(snakelist))[:len(snakelist)-1]:
            #         print(set(snakelist))
            #         Snake.Over = True

            row = 0
            for x,y in snakelist:


                if row==len(snakelist)-1:
                    pygame.draw.rect(Snake.Display,'blue',[x,y,20,20])
                else:

                    pygame.draw.rect(Snake.Display, 'green',[x, y, 20, 20])
                row += 1


            Snake.food(Snake.Display,'dark blue',foodinteger,foodinteger,20)
            pygame.time.set_timer(50,100)


            clock.tick(30)

            if (50,50) not in snakelist and (Snake.x,Snake.y) in snakelist:
                over = False
                import time
                while not over:

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            over = True
                            Snake.Over = True

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                over = True
                                continue



                    a = pygame.font.Font(r"C:\Users\mahen\bitepy\yes\yes\photos\BrusselsCityPersonalUsed-L3Lon.otf", 22)
                    b = a.render(f'Game Over',True,'Black')
                    Snake.Display.fill('White')
                    Snake.Display.blit(b,(1920//2-150,400))
                    c = a.render('Enter To Play Press Enter',True,'Black')
                    Snake.Display.blit(c, (1920 //2-150, 425))
                    pygame.display.update()
                    print(event)
                    time.sleep(1)

            snakelist.append((Snake.x,Snake.y))


            pygame.display.update()


a = Snake()
a.run()