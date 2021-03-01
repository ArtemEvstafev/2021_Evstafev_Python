import pygame
import pygame.draw as draw
from random import randint
from random import choice

pygame.init()

Score = 0
FPS = 50
screen = pygame.display.set_mode((1300, 700))
SPEED = 5
x_delta = SPEED
y_delta = SPEED
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]
finished = False


def new_ball(x_delta, y_delta):
    '''
    Функция создает новйы шарик, если передать 0.0, возвращая картэж из (+-1,+-1)
    При других значения дельта рисует новый шарик в дельта окрестности
    :param x_delta: смщенеие по x
    :param y_delta: смещение по y
    :return: при x_delta = y_delta = 0 случайным образом меняет направления смещения
    '''
    if x_delta == 0 and y_delta == 0:
        global x, y, r, color
        x = randint(100, 1200)
        y = randint(100, 600)
        r = randint(10, 100)
        color = COLORS[randint(0, 6)]
        draw.circle(screen, color, (x, y), r)
        number = [-SPEED, SPEED]
        return [choice(number), choice(number)]
    else:  # тут происходит анимация
        x += x_delta
        y += y_delta
        draw.circle(screen, color, (x, y), r)


def move_direction(x, y, r):
    '''

    :param x: x координата шара
    :param y: y координата шара
    :param r: радиус шара
    :return:
    '''
    global x_delta, y_delta
    if (y + r > 700 or y - r < 0):
        y_delta *= -1
    if (x + r > 1300 or x - r < 0):
        x_delta *= -1


pygame.display.update()
clock = pygame.time.Clock()

font = pygame.font.Font(None, 50)  #
text = font.render("Your Score is " + str(Score), True, WHITE)  #
text_miss = font.render("MISS!", True, WHITE)  # Создает текст сверху
screen.blit(text, [500, 0])  #

new_ball(0, 0)  # первый шарик
new_ball(0, 0) #второй шарик
pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # print('Click')
            event.x, event.y = event.pos
            if (((event.x - x) ** 2 + (event.y - y) ** 2) ** 0.5 < r):
                Score += 1
                print('Your Score is: ', Score)
                x_delta, y_delta = new_ball(0, 0)  # для случайного направления после появления
                pygame.display.update()
            else:
                # print('Miss')
                screen.blit(text_miss, [800, 0])
                Score = 0
    move_direction(x, y, r)
    new_ball(x_delta, y_delta)
    text = font.render("Your Score is: " + str(Score), True, WHITE)
    screen.blit(text, [500, 0])
    pygame.display.update()
    screen.fill(BLACK)  # для исчезания прошлого рисунка

pygame.quit()
