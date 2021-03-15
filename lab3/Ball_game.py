import pygame
import pygame.draw as draw
from random import randint
from random import choice

pygame.init()

Score = 0
SCORES = [0, 0, 0, 0, 0]
NAMES = ['-', '-', '-', '-', '-']
FPS = 60
screen = pygame.display.set_mode((1300, 700))
SPEED = 5
x_delta = SPEED
y_delta = SPEED
SPEED_SQR = SPEED + 4
x_delta_sqr = SPEED_SQR
y_delta_sqr = SPEED_SQR
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


def new_square(x_delta_sqr, y_delta_sqr):
    '''
    Функция создает новйы квадратикик, если передать 0.0, возвращая картэж из (+-1,+-1)
    При других значения дельта рисует новый шарик в дельта окрестности
    :param x_delta_sqr:
    :param y_delta_sqr:
    :return: квадратик
    '''
    if x_delta_sqr == 0 and y_delta_sqr == 0:
        global x_sqr, y_sqr, r_sqr, color_sqr
        x_sqr = randint(100, 1200)
        y_sqr = randint(100, 600)
        r_sqr = 20
        color_sqr = COLORS[randint(0, 6)]
        draw.rect(screen, color_sqr,
                  (x_sqr - int(20 / 2 ** 0.5), y_sqr - int(20 / 2 ** 0.5), int(40 / 2 ** 0.5), int(40 / 2 ** 0.5)), 0)
        # draw.circle(screen, color_sqr, (x_sqr, y_sqr), r_sqr, 1)
        number = [-SPEED_SQR, SPEED_SQR]
        return [choice(number), choice(number)]
    else:  # тут происходит анимация
        x_sqr += x_delta_sqr
        y_sqr += y_delta_sqr
        draw.rect(screen, color_sqr,
                  (x_sqr - int(20 / 2 ** 0.5), y_sqr - int(20 / 2 ** 0.5), int(40 / 2 ** 0.5), int(40 / 2 ** 0.5)), 0)
        # draw.circle(screen, color_sqr, (x_sqr, y_sqr), r_sqr, 1)


def move_direction(x, y, r, x_sqr, y_sqr, r_sqr):
    '''
    функция изменяет направление шара при ударе о стенку или о друг друга
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
    global x_delta_sqr, y_delta_sqr
    if (y_sqr + r_sqr > 700 or y_sqr - r_sqr < 0):
        y_delta_sqr *= -1
    if (x_sqr + r_sqr > 1300 or x_sqr - r_sqr < 0):
        x_delta_sqr *= -1
    if (((x - x_sqr) ** 2 + (y - y_sqr) ** 2) ** 0.5 <= r + r_sqr):
        y_delta_sqr *= -1
        x_delta_sqr *= -1
        x_delta *= -1
        y_delta *= -1


def score_saving():
    '''
    сохраняет в файл таблицу из дучших игроков
    :return:
    '''
    file = open('PLAYERS.txt', 'w')
    for i in range(0, 5):
        print(i + 1, '. ', NAMES[i], ': ', SCORES[i], '\n', sep='', file=file)
    file.close()


pygame.display.update()
clock = pygame.time.Clock()

font = pygame.font.Font(None, 50)  #
text = font.render("Your Score is " + str(Score), True, WHITE)  #
text_miss = font.render("MISS!", True, WHITE)  # Создает текст сверху
screen.blit(text, [500, 0])  #

new_ball(0, 0)  # первый шарик
new_square(0, 0)  # первый квадратик
pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            score_saving()
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # print('Click')
            event.x, event.y = event.pos
            if (((event.x - x) ** 2 + (event.y - y) ** 2) ** 0.5 < r):
                Score += 1
                print('Your Score is: ', Score)
                x_delta, y_delta = new_ball(0, 0)  # для случайного направления после появления
                pygame.display.update()
            elif (((event.x - x_sqr) ** 2 + (event.y - y_sqr) ** 2) ** 0.5 < r_sqr):
                Score += 3
                print('Your Score is: ', Score)
                x_delta_sqr, y_delta_sqr = new_square(0, 0)  # для случайного направления после появления
                pygame.display.update()
            else:
                # print('Miss')
                screen.blit(text_miss, [800, 0])
                for i in range(0, 5):
                    if Score > SCORES[i]:
                        SCORES.insert(i, Score)
                        SCORES.pop()
                        name = input()
                        NAMES.insert(i, name)
                        NAMES.pop()
                        break
                Score = 0
                print(SCORES)
                print(NAMES)
    move_direction(x, y, r, x_sqr, y_sqr, r_sqr)
    new_ball(x_delta, y_delta)
    new_square(x_delta_sqr, y_delta_sqr)
    text = font.render("Your Score is: " + str(Score), True, WHITE)  # обновление счета после попадания
    screen.blit(text, [500, 0])
    pygame.display.update()
    screen.fill(BLACK)  # для исчезания прошлого рисунка

pygame.quit()
