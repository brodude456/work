red = (255, 0, 0)
orange = (255, 127, 0)
yellow = (255, 255, 0)
green= (0, 255, 0)
blue = (0, 0, 255)
violet = (127, 0, 255)
brown = (102, 51, 0)
black = (0, 0, 0)
white = (255, 255, 255)

game_screen = pygame.display.set_mode((screen_width, screen_height))

import pygame
import time

screen_width = 600
screen_height = 400

game_screen = pygame.display.set_mode((screen_width, screen_height))

counter=0

pygame.display.set_caption("Tiny Tennis")



class Dionasor():

    def __init__(self,pos_x,pos_y,couler,radius,speed):

        self.pos_x=pos_x
        self.pos_y=pos_y

        self.couler=couler
        self.radius=radius

        self.speed=speed*-1
        self.starting_speed=speed
        self.starting_pos_y=pos_y

        self.starting_pos_x=pos_x
        self.score=0

    def game_over(self,obstacle):

        self.pos_y=self.starting_pos_y
        self.score=0
        self.speed=self.starting_speed
        obstacle.restart()

    def jump(self,obstacle):

        while True:

            game_screen = pygame.display.set_mode((screen_width, screen_height))
            pygame.display.set_caption("Tiny Tennis")

            game_screen.fill(white)

            paddle_1 = pygame.draw.rect(game_screen,obstacle1.couler, (obstacle1.pos_x, obstacle1.pos_y, obstacle1.withh,obstacle1.hight), 0)
            ball = pygame.draw.circle(game_screen, red, (doinosur1.pos_x, doinosur1.pos_y),doinosur1.radius,0)

            #score_text = font.render(str(doinosur1.score) )
            #game_screen.blit(score_text, (screen_width / 2 - score_text.get_width() / 2, 10))

            pygame.display.update()
            time.sleep(0.016666667)

            self.pos_y=self.pos_y+self.speed
            obstacle.make_it_move()

            if self.pos_y<=obstacle.pos_y-self.radius-1 and obstacle1.pos_x<self.pos_x+obstacle1.speed:

                self.speed*=-1

            elif self.pos_y>=self.starting_pos_y:

                self.pos_y=self.starting_pos_y
                game_screen = pygame.display.set_mode((screen_width, screen_height))
                pygame.display.set_caption("Tiny Tennis")

                game_screen.fill(white)

                paddle_1 = pygame.draw.rect(game_screen,obstacle1.couler, (obstacle1.pos_x, obstacle1.pos_y, obstacle1.withh,obstacle1.hight), 0)
                ball = pygame.draw.circle(game_screen, red, (doinosur1.pos_x, doinosur1.pos_y),doinosur1.radius,0)

                #score_text = font.render(str(doinosur1.score) )
                #game_screen.blit(score_text, (screen_width / 2 - score_text.get_width() / 2, 10))

                pygame.display.update()
                time.sleep(0.016666667)
                self.score+=1

                break

            elif self.pos_y>obstacle.pos_y-self.radius and self.pos_x>=obstacle.pos_x and self.speed<0:

                self.game_over(obstacle)
                break

            if self.speed<-2:
                self.speed+=2

class Obstacle():

    def __init__(self,pos_x,pos_y,couler,speed,speed_ader,withh,hight):

        self.pos_x_starting=pos_x
        self.pos_x=pos_x

        self.pos_y=pos_y
        self.couler=couler

        self.speed=speed
        self.starting_speed=speed

        self.speed_add_smh=speed_ader
        self.speed_add=speed_ader

        self.withh=withh
        self.hight=hight

    def restart(self):

        self.pos_x=self.pos_x_starting
        self.speed=self.starting_speed
        self.speed_add=self.speed_add_smh

    def make_it_move(self):

        self.pos_x-=self.speed

    def make_it_go_fater(self):

        self.speed+=self.speed_add
        self.speed_add=self.speed_add//2

obstacle1=Obstacle(550,240,black,10,10,30,60)
doinosur1=Dionasor(100,280,red,20,15)

#font = pygame.font.SysFont(None, 75)

while True:


    pygame.display.set_caption("Tiny Tennis")

    game_screen.fill(white)

    paddle_1 = pygame.draw.rect(game_screen,obstacle1.couler, (obstacle1.pos_x, obstacle1.pos_y, obstacle1.withh,obstacle1.hight), 0)
    ball = pygame.draw.circle(game_screen, red, (doinosur1.pos_x, doinosur1.pos_y),doinosur1.radius,0)

    #score_text = font.render(str(doinosur1.score) )
    #game_screen.blit(score_text, (screen_width / 2 - score_text.get_width() / 2, 10))

    pygame.display.update()
    time.sleep(0.016666667)


    pressed = pygame.key.get_pressed()
    pygame.key.set_repeat()

    if pressed[pygame.K_w]:

        doinosur1.jump(obstacle1)

    elif doinosur1.pos_x>=obstacle1.pos_x-doinosur1.radius:

        doinosur1.game_over(obstacle1)

    elif obstacle1.pos_x<doinosur1.pos_x-(doinosur1.pos_x-50):

        obstacle1.restart()
        obstacle1.make_it_go_fater()

    if pressed[pygame.K_ESCAPE]:
        pygame.quit()
        break

    else:
        obstacle1.make_it_move()

