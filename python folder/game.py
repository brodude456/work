import pygame

red = (255, 0, 0)
orange = (255, 127, 0)
yellow = (255, 255, 0)
green: (0, 255, 0)
blue = (0, 0, 255)
violet = (127, 0, 255)
brown = (102, 51, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# screen globals
screen_width = 600
screen_height = 400

game_screen = pygame.display.set_mode((screen_width, screen_height))

class Spaceship():
    def init(pos_x,pos_y,couler,width,height):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.couler=couler
        self.width=width
        self.height=height
    
    def move_to_right(self):
        self.pos_x+=10
    
    def move_to_left(self):
        self.pos_x-=10
    
you=Spaceship(screen_width//2,350,red,100,50)

while True:
    game_screen.fill(black)
    paddle_1 = pygame.draw.rect(game_screen,you.couler,(you.pos_x,you.pos_y,you.width,you.height), 0)

    pressed = pygame.key.get_pressed()
    if pressed==pressed[pygame.K_w]:
        you.move_to_left
   
    elif pressed[pygame.K_s]:
        you.move_to_righth
