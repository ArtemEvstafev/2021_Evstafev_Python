import pygame
from math import sin
from math import pi

pygame.init()
FPS = 30
screen = pygame.display.set_mode((1500, 780), pygame.SRCALPHA)

counter = 0  # счетчик тиков
day = True  # день ли в арктике?


def landscape():
    """
    Функция отображает пейзаж на фоне
    :return: рисунок
    """
    sun = pygame.Surface((600, 350))  # поверхность солнца
    sun.set_alpha(150)
    sun.set_colorkey('BLACK')
    if day:
        skycolor = (154, 252, 248)
    else:
        skycolor = (72, 23, 87)
    pygame.draw.rect(screen, skycolor, (0, 0, 1500, 390), 0)  # небо
    pygame.draw.rect(screen, (255, 255, 255), (0, 390, 1500, 390), 0)  # лед
    pygame.draw.ellipse(sun, (253, 255, 219), (0, 0, 360, 330), 30)  # отрисовка круга солнца
    pygame.draw.line(sun, (253, 255, 219), (0, 165), (360, 165), 25)  # отрисовка креста солнца
    pygame.draw.line(sun, (253, 255, 219), (180, 0), (180, 330), 25)  # отрисовка креста солнца
    # отрисовка кружков в центре и пересечениях креста с кругом
    pygame.draw.circle(sun, (255, 255, 100), (180, 10), 15)
    pygame.draw.circle(sun, (255, 255, 100), (180, 320), 15)
    pygame.draw.circle(sun, (255, 255, 100), (20, 160), 15)
    pygame.draw.circle(sun, (255, 255, 100), (350, 160), 15)
    pygame.draw.circle(sun, (255, 255, 100), (180, 170), 25, 0)
    if day:
        screen.blit(sun, (850, 10))


def cloud(x0, y0, surface):
    """
    Функция описывает отрисовку облака на экране
    :param x0: координата левого верхнего угла поверхности облака по оХ
    :param y0: координата левого верхнего угла поверхности облака по оУ
    :param surface: поверхность, на которой отриссовывается облако
    :return:
    """
    # определение цвета облака
    if day:
        cloudcolor = 'white'
    else:
        cloudcolor = (3, 10, 75)
    # опишем круги, из которых состоит облако
    pygame.draw.circle(surface, cloudcolor, (x0 + 20, y0 + 30), 20)
    pygame.draw.circle(surface, cloudcolor, (x0 + 55, y0 + 35), 35)
    pygame.draw.circle(surface, cloudcolor, (x0 + 75, y0 + 45), 25)
    pygame.draw.circle(surface, cloudcolor, (x0 + 80, y0 + 20), 20)
    pygame.draw.circle(surface, cloudcolor, (x0 + 25, y0 + 50), 15)


def move_cloud(counter_, speed):
    """
    Функция отвечает за перемещение облака
    :param counter_: счетчик тиков
    :param speed: скорость движения облака
    :return: плывущее облачко
    """
    cloud_ = pygame.Surface((100, 80))
    cloud_.set_colorkey('black')
    cloud(0, 0, cloud_)
    screen.blit(cloud_, (counter_ * speed, 50 - 20 * sin(counter_ / 20)))


def right_bear(size, x, y, fish):
    """
    Функция рисует медведя на экране, смотрящего вправо
    :param size: размер медведя по вертикали
    :param x: начальная координата медведя по оХ
    :param y: начальная координата медведя по оУ
    :param fish: определяем ориентацию и положение рыбы
    :return: рисунок
    """
    # body
    pygame.draw.ellipse(screen, (255, 255, 255), (x, y + size / 8, size * 3 / 8, size * 0.75), 0)
    pygame.draw.ellipse(screen, (0, 0, 0), (x, y + size / 8, size * 3 / 8, size * 0.75), 1)
    # head
    pygame.draw.ellipse(screen, (255, 255, 255), (x + size / 8, y, size * 3 / 8, 3 * size / 16), 0)
    pygame.draw.ellipse(screen, (0, 0, 0), (x + size / 8, y, size * 3 / 8, 3 * size / 16), 1)
    # leg
    pygame.draw.ellipse(screen, (255, 255, 255), (x + size / 8, y + size * (1 - 5 / 16), 5 * size / 16, 5 * size / 16),
                        0)
    pygame.draw.ellipse(screen, (0, 0, 0), (x + size / 8, y + size * (1 - 5 / 16), 5 * size / 16, 5 * size / 16), 1)
    # feet
    pygame.draw.ellipse(screen, (255, 255, 255),
                        (x + size * (1 / 4 + 1 / 16), y + size * (1 - 3 / 32), 7 * size / 32, 3 * size / 32),
                        0)
    pygame.draw.ellipse(screen, (0, 0, 0),
                        (x + size * (1 / 4 + 1 / 16), y + size * (1 - 3 / 32), 7 * size / 32, 3 * size / 32), 1)
    # fishing rod
    pygame.draw.line(screen, (0, 0, 0), (x + size * 3 / 8, y + size / 2), (x + size * 3 / 4, y),
                     int(5 * size / 500))
    # arm
    pygame.draw.ellipse(screen, (255, 255, 255),
                        (x + size * (1 / 4 + 1 / 16), y + size * 0.4, 7 * size / 32, 3 * size / 32), 0)
    pygame.draw.ellipse(screen, (0, 0, 0), (x + size * (1 / 4 + 1 / 16), y + size * 0.4, 7 * size / 32, 3 * size / 32),
                        1)
    # hole
    pygame.draw.ellipse(screen, (169, 169, 169), (x + size / 2, y + size * (1 - 4 / 16), size / 2, 4 * size / 16),
                        0)
    pygame.draw.ellipse(screen, (0, 0, 0), (x + size / 2, y + size * (1 - 4 / 16), size / 2, 4 * size / 16), 1)
    # water in the hole
    pygame.draw.ellipse(screen, (0, 0, 102), (
        x + size * (17 / 32), y + size * (13/ 16), 7 * size / 16, 3 * size / 16),
                        0)
    pygame.draw.ellipse(screen, (0, 0, 0), (
        x + size * (17 / 32), y + size * (13/ 16), 7 * size / 16, 3 * size / 16),
                        1)
    draw_fish(x +size * (18 / 32), y + size * (27/ 32), size/6, screen)
    # spinning
    pygame.draw.line(screen, (0, 0, 0), (x + size * 3 / 4, y), (x + size * 3 / 4, y + size * (1 - 1 / 8)),
                     1)
    # mouth
    pygame.draw.line(screen, (0, 0, 0), (x + size * 5 / 16, y + 9 / 64 * size), (x + size * 15 / 32, y + 9 / 64 * size),
                     2)
    # nose
    pygame.draw.circle(screen, (0, 0, 0), (x + size * 16 / 32, y + 5 / 64 * size), 7 * size / 600, 0)
    # eye
    pygame.draw.circle(screen, (0, 0, 0), (x + size * 10 / 32, y + 4 / 64 * size), 9 * size / 600, 0)
    # ear
    pygame.draw.circle(screen, (255, 255, 255), (x + size * 5 / 32, y + 2 / 64 * size), 18 * size / 600, 0)
    pygame.draw.circle(screen, (0, 0, 0), (x + size * 5 / 32, y + 2 / 64 * size), 18 * size / 600, 1)
    right_fish = pygame.Surface((200 / 166 * size, 120 / 166 * size))
    right_fish.set_colorkey('black')
    if fish == 'R':
        draw_fish(x, y + size, size / 4, right_fish)
        screen.blit(right_fish, (x, y + size))
        # draw_fish(x, y + size, size / 2)
    else:
        draw_fish(x, y + size, size / 3, pygame.transform.flip(right_fish, True, False))
        screen.blit(pygame.transform.flip(right_fish, True, False), (x, y + size))


def left_bear(size, x, y, fish):
    """
        Функция рисует медведя на экране, смотрящего влево
        :param size: размер медведя по вертикали
        :param x: начальная координата медведя по оХ
        :param y: начальная координата медведя по оУ
        :param fish: определяем ориентацию и положение рыбы
        :return: рисунок
    """
    # body
    pygame.draw.ellipse(screen, (255, 255, 255), (x + size * (1 - 3 / 8), y + size / 8, size * 3 / 8, size * 0.75),
                        0)
    pygame.draw.ellipse(screen, (0, 0, 0), (x + size * (1 - 3 / 8), y + size / 8, size * 3 / 8, size * 0.75), 1)
    # head
    pygame.draw.ellipse(screen, (255, 255, 255), (x + size * (1 - 1 / 2), y, size * 3 / 8, 3 * size / 16), 0)
    pygame.draw.ellipse(screen, (0, 0, 0), (x + size * (1 - 1 / 2), y, size * 3 / 8, 3 * size / 16), 1)
    # leg
    pygame.draw.ellipse(screen, (255, 255, 255),
                        (x + size * (1 - 1 / 8 - 5 / 16), y + size * (1 - 5 / 16), 5 * size / 16, 5 * size / 16),
                        0)
    pygame.draw.ellipse(screen, (0, 0, 0),
                        (x + size * (1 - 1 / 8 - 5 / 16), y + size * (1 - 5 / 16), 5 * size / 16, 5 * size / 16), 1)
    # feet
    pygame.draw.ellipse(screen, (255, 255, 255),
                        (x + size * (1 - 5 / 16 - 7 / 32), y + size * (1 - 3 / 32), 7 * size / 32, 3 * size / 32),
                        0)
    pygame.draw.ellipse(screen, (0, 0, 0),
                        (x + size * (1 - 5 / 16 - 7 / 32), y + size * (1 - 3 / 32), 7 * size / 32, 3 * size / 32), 1)
    # fishing rod
    pygame.draw.line(screen, (0, 0, 0), (x + size * (1 - 3 / 8), y + size / 2), (x + size * 1 / 4, y),
                     int(5 * size / 500))
    # arm
    pygame.draw.ellipse(screen, (255, 255, 255),
                        (x + size * (1 - 5 / 16 - 7 / 32), y + size * 0.4, 7 * size / 32, 3 * size / 32), 0)
    pygame.draw.ellipse(screen, (0, 0, 0),
                        (x + size * (1 - 5 / 16 - 7 / 32), y + size * 0.4, 7 * size / 32, 3 * size / 32), 1)
    # hole
    pygame.draw.ellipse(screen, (169, 169, 169), (x, y + size * (1 - 4 / 16), size / 2, 4 * size / 16), 0)
    pygame.draw.ellipse(screen, (0, 0, 0), (x, y + size * (1 - 4 / 16), size / 2, 4 * size / 16), 1)
    # water
    pygame.draw.ellipse(screen, (0, 0, 102),
                        (x + size * ((1 / 2 - 7 / 16) / 2), y + size * (1 - 3 / 16), 7 * size / 16, 3 * size / 16),
                        0)
    pygame.draw.ellipse(screen, (0, 0, 0),
                        (x + size * ((1 / 2 - 7 / 16) / 2), y + size * (1 - 3 / 16), 7 * size / 16, 3 * size / 16), 1)
    # spinning
    pygame.draw.line(screen, (0, 0, 0), (x + size * 1 / 4, y), (x + size * 1 / 4, y + size * (1 - 1 / 8)),
                     1)
    # mouth
    pygame.draw.line(screen, (0, 0, 0), (x + size * (1 - 5 / 16), y + 9 / 64 * size),
                     (x + size * (1 - 15 / 32), y + 9 / 64 * size),
                     2)
    # nose
    pygame.draw.circle(screen, (0, 0, 0), (x + size * (1 - 16 / 32), y + 5 / 64 * size), 7 * size / 600, 0)
    # eye
    pygame.draw.circle(screen, (0, 0, 0), (x + size * (1 - 10 / 32), y + 4 / 64 * size), 9 * size / 600, 0)
    # ear
    pygame.draw.circle(screen, (255, 255, 255), (x + size * (1 - 5 / 32), y + 2 / 64 * size), 18 * size / 600, 0)
    pygame.draw.circle(screen, (0, 0, 0), (x + size * (1 - 5 / 32), y + 2 / 64 * size), 18 * size / 600, 1)
    right_fish = pygame.Surface((200/166*size, 120/166*size))
    right_fish.set_colorkey('black')

    if fish == 'R':
        draw_fish(x, y + size, size/2, right_fish)
        screen.blit(right_fish, (x, y+size))
        #draw_fish(x, y + size, size / 2)
    else:
        draw_fish(x, y + size, size / 2, pygame.transform.flip(right_fish, True, False))
        screen.blit(pygame.transform.flip(right_fish, True, False), (x, y+size))

def draw_fish(x, y, size, surface):
    """
    Функция рисует на экране рыбку.
    :param x: координата верхнего левого угла рыбки по оХ
    :param y: координата верхнего левого угла рыбки по оУ
    :param size: зависимость размера рыбки от размера медведя
    :return: рисунок.
    """
    # тело рыбки
    cords = [[x + 41 / 166 * size, y + 68 / 166 * size], [x + 76 / 166 * size, y + 41 / 166 * size],
             [x + 110 / 166 * size, y + 23 / 166 * size], [x + 149 / 166 * size, y + 18 / 166 * size],
             [x + 189 / 166 * size, y + 30 / 166 * size],
             [x + 164 / 166 * size, y + 54 / 166 * size], [x + 136 / 166 * size, y + 67 / 166 * size],
             [x + 81 / 166 * size, y + 72 / 166 * size]]
    pygame.draw.polygon(screen, 'GRAY', cords)
    pygame.draw.lines(screen, 'BLACK', True, cords, 1)
    # хвост рыбки
    cords = [[x + 42 / 166 * size, y + 67 / 166 * size], [x, y + 116 / 166 * size],
             [x + 1 / 166 * size, y + 75 / 166 * size]]
    pygame.draw.polygon(screen, 'GRAY', cords)
    pygame.draw.lines(screen, 'BLACK', True, cords, 1)
    # верхний плавник
    cords = [[x + 141 / 166 * size, y + 19 / 166 * size], [x + 130 / 166 * size, y],
             [x + 59 / 166 * size, y + 13 / 166 * size], [x + 104 / 166 * size, y + 26 / 166 * size]]
    pygame.draw.polygon(screen, 'RED', cords)
    pygame.draw.lines(screen, 'BLACK', False, cords, 1)
    # нижние плавники
    cords = [[x + 141 / 166 * size, y + 65 / 166 * size], [x + 157 / 166 * size, y + 93 / 166 * size],
             [x + 179 / 166 * size, y + 65 / 166 * size], [x + 147 / 166 * size, y + 61 / 166 * size]]
    pygame.draw.polygon(screen, 'RED', cords)
    pygame.draw.lines(screen, 'BLACK', False, cords, 1)
    cords = [[x + 77 / 166 * size, y + 73 / 166 * size], [x + 69 / 166 * size, y + 95 / 166 * size],
             [x + 101 / 166 * size, y + 91 / 166 * size], [x + 94 / 166 * size, y + 71 / 166 * size]]
    pygame.draw.polygon(screen, 'RED', cords)
    pygame.draw.lines(screen, 'BLACK', False, cords, 1)

    pygame.draw.circle(screen, 'BLUE', (x + 150/166*size, y + 35/166*size), 10/166*size)
    pygame.draw.circle(screen, 'BLACK', (x + 145/166*size, y + 35/166*size), 5/166*size)
    pygame.draw.circle(screen, 'WHITE', (x + 145/166*size, y + 38/166*size), 1/166*size)




pygame.display.update()
clock = pygame.time.Clock()
clock.tick(FPS)
finished = False

while not finished:
    clock.tick(FPS)
    counter += 1
    landscape()
    right_bear(400, 100, 160, 'R')
    left_bear(100, 1400, 400, 'R')
    right_bear(100, 1250, 400, 'L')
    left_bear(333, 750, 400, 'L')
    move_cloud(counter, 1)
    move_cloud(counter - 100, 4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            day = not day
    pygame.display.update()

pygame.quit()
