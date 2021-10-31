
import pygame, sys
pygame.init()
red=(255,0,0)
screen = pygame.display.set_mode((600, 600))
color = (0, 100, 100)
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
mouse=(72,72,72)
a=100
b=350
c=300
z=350
gameon=True
while True:
    for h in range (0,8,1):
        z=z-0.25
        if z<50:
            z=350
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        key=pygame.key.get_pressed()
        if key[pygame.K_UP]:
            b=b-50
        if key[pygame.K_DOWN]:
            b = b + 50
        if key[pygame.K_RIGHT]:
            a = a + 50
        if key[pygame.K_LEFT]:
            a = a - 50
    if a==c and b==z : #losing if cat touches mouse
        a = 100
        b = 350
    if a == 400 and b == 200: # winning
        pygame.display.set_mode((800, 800))
    elif b==0 or a==0 or b==400  or a==400: #lose scenario if he touches water
        a=100
        b=350
    for x in range(0, 400, 50):
        pygame.draw.rect(screen, color,(x,0,50,50) )
    for x in range(0, 400, 50):
        pygame.draw.rect(screen, color, (x, 400, 50, 50))
    for y in range(0, 400, 50):
        pygame.draw.rect(screen, color, (0, y, 50, 50))
    for y in range(0, 450, 50):
         pygame.draw.rect(screen, color, (400, y, 50, 50))
         y=0
    for i in range(0,7,1):
        y=y+50
        for x in range(50, 400, 50):
            pygame.draw.rect(screen, white, (x,y, 50, 50))
            x=50
    for x in range(0, 500, 50):
        pygame.draw.line(screen, black, (1, x), (600, x), 2)
        pygame.draw.line(screen, black, (x, 1), (x, 600), 2)
    pygame.draw.rect(screen,green , (400, 200, 50, 50))
    pygame.draw.rect(screen, red, (c, z , 50, 50))
    pygame.draw.rect(screen,mouse, (a, b, 50, 50))
    pygame.display.update()