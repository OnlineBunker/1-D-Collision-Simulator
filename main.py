#Imports
import pygame
import math

#Inputs
m1 = int(input('Mass of object 1: '))
m2 = int(input('Mass of object 2: '))
v1 = int(input('Initial velocity of object 1: '))
v2 = int(input('Initial velocity of object 2: '))

#Screen
pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1-D Collision Simulation")

#Size of the Squares
size = 30
s1 = size+(m1*3)
s2 = size+(m2*3)

#Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#Initial Positions
x1 = 100
x2 = 700
y_pos_1 = HEIGHT // 2 - s1 // 2
y_pos_2 = HEIGHT // 2 - s2 // 2

#FPS
clock = pygame.time.Clock()

#Collision Physics
def el_calculate_collision(v1, m1, v2, m2):
    v1_final = (v1 * (m1 - m2) + 2 * m2 * v2) / (m1 + m2)
    v2_final = (v2 * (m2 - m1) + 2 * m1 * v1) / (m1 + m2)
    return v1_final, v2_final

# def in_calculate_collision(v1, m1, v2, m2):
#     v_final = (m1 * v1 + m2 * v2) / (m1 + m2)  
#     return v_final, v_final 


#Game Loop
running = True
while running:
    clock.tick(120)
    screen.fill(WHITE)

    #moving the squares
    x1 += v1
    x2 += v2

    #Collision Detection
    if abs(x1- x2) <= (s1 + s2) / 2:
        v1, v2 = el_calculate_collision(v1, m1, v2, m2)
    
    #Wall Collision Detection
    if x1 <= 0 or x1 + s1 >= WIDTH:
        v1 = -v1
    if x2 <= 0 or x2 + s2 >= WIDTH:
        v2 = -v2

    #Drawing the squares
    pygame.draw.rect(screen, RED, (x1, y_pos_1, s1, s1))
    pygame.draw.rect(screen, BLUE, (x2, y_pos_2, s2, s2))


    #Extra
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()