import pygame
import math
import random

pygame.init()
clock = pygame.time.Clock()

width = 1000
height = 1000

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Circular Pong!")

run = True

direction = [-1,1]
speed = [1,2,3,4]

ball_x = width/2.0
ball_y = height/2.0
ball_vx = random.choice(speed)*random.choice(direction)
ball_vy = random.choice(speed)*random.choice(direction)

radius = 450

white = (255,255,255)
black = (0,0,0)

t = random.uniform(0,360)
epsilon = 250

score = 0

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(str(score), True, white,black)

def arena():
    global radius

    theta_i = 0
    dtheta = 0.1

    screen.blit(text,(width/2.0,height/2.0))
    
    while theta_i < 2*math.pi:
        theta_f = theta_i + dtheta
        pygame.draw.arc(screen,white,(width/2.0 - radius, height/2.0 - radius, 2*radius,2*radius),theta_i, theta_f,2)
        theta_i = theta_f + dtheta
        
while run:
    screen.fill(black)
    arena()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        t += 0.05
    if keys[pygame.K_RIGHT]:
        t -= 0.05
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.draw.circle(screen,white,(ball_x,ball_y),5)
    ball_rect  = pygame.Rect(ball_x-5,ball_y-5,10,10)
    
    paddle_length = 75
    paddle_width = 15
    
    px = width/2.0 + radius*math.cos(t)
    py = height/2.0 + radius*math.sin(t)

    perp_angle = t + math.pi/2.0
    dx = (paddle_length/2)*math.cos(perp_angle)
    dy = (paddle_length/2)*math.sin(perp_angle)

    x1 = px - dx
    y1 = py - dy
    x2 = px + dx
    y2 = py + dy
    
    pygame.draw.line(screen,(255,0,0),(x1,y1),(x2,y2),paddle_width)
    paddle_rect = pygame.Rect(min(x1,x2)-paddle_width/2.0,min(y1,y2)-paddle_width/2.0,abs(x2-x1)+paddle_width,abs(y2-y1)+paddle_width)

    if paddle_rect.colliderect(ball_rect):
        score += 1
        text = font.render(str(score), True, white,black)
        rx = ball_x - width/2.0
        ry = ball_y - height/2.0

        r = math.sqrt(rx**2+ry**2)
        nx = rx/r
        ny = ry/r

        dot_prod = ball_vx*nx+ball_vy*ny
        ball_vx -= 2*dot_prod*nx*random.uniform(1,2)
        ball_vy -= 2*dot_prod*ny*random.uniform(1,2)

        speed = math.sqrt(ball_vx**2+ball_vy**2)

        ball_vx /= 0.5*speed
        ball_vy /= 0.5*speed
        
        if abs(ball_vx) > 5:
            ball_vx = 2

        if abs(ball_vy) > 5:
            ball_vy = 2
        
    if ((ball_x-width/2.0)**2+(ball_y-height/2.0)**2) > radius**2 + epsilon:
        run = False
    
    ball_x += 1.1*ball_vx
    ball_y += 1.1*ball_vy
    
    pygame.display.flip()
    clock.tick(60)    
