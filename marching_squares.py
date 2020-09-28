import pygame
import random

pygame.font.init()

# display variables
width = 600
height = 600
grey = (128, 128, 128)

display = pygame.display.set_mode((width, height))
display.fill(grey)
pygame.display.set_caption('Marching Squares')

# 2D array that keeps track of the points
field = []

rez = 10

# returns the value of the four points if treated as bits
def state(a, b, c, d):
    return a * 8 + b * 4 + c * 2 + d * 1

# the func. that draws the isolines
def line(a, b):
    pygame.draw.line(display, (255, 255, 255), a, b, 1)

run = True
rows = width // rez
cols = height // rez


for i in range(rows + 1):
    field.append([])
    for j in range(cols + 1):
        n = random.randint(0, 1)
        color = (n*255, n*255, n*255)
        pygame.draw.circle(display, color, (i*rez, j*rez), 2)
        field[i].append(n)

for i in range(rows):
    for j in range(cols):
        x = i * rez
        y = j * rez
        a = (x + rez * 0.5, y)
        b = (x + rez, y + rez * 0.5)
        c = (x + rez * 0.5, y + rez)
        d = (x, y + rez * 0.5)
        case = state(field[i][j], field[i + 1][j], field[i + 1][j + 1], field[i][j + 1])

        # checks every case to draw the respective isolines
        if case == 0:
            pass
        elif case == 1:
            line(c, d)
        elif case == 2:
            line(b, c)
        elif case == 3:
            line(b, d)
        elif case == 4:
            line(a, b)
        elif case == 5:
            line(d, a)
            line(b, c)
        elif case == 6:
            line(a, c)
        elif case == 7:
            line(d, a)
        elif case == 8:
            line(d, a)
        elif case == 9:
            line(a, c)
        elif case == 10:
            line(a, b)
            line(c, d)
        elif case == 11:
            line(a, b)
        elif case == 12:
            line(b, d)
        elif case == 13:
            line(b, c)
        elif case == 14:
            line(c, d)
        elif case == 15:
            pass

pygame.display.flip()

# quit program
while run:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            run = False
