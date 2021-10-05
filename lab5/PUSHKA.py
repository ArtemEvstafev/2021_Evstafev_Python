from random import randrange as rnd, choice
import math
import time
import pygame
import pygame.draw as draw
import numpy

# КОНСТАНТЫ
TARGETS_NUMBER = 3
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (1, 51, 33)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
FPS = 30
points = 0
zleep = 3

pygame.init()
screen = pygame.display.set_mode((1500, 780))  # 800, 600
screen.fill(WHITE)


class ball():
    def __init__(self, x=0, y=0):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.a = 1
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.color = choice(COLORS)
        draw.circle(screen, self.color, (self.x, self.y), self.r)

    def set_coords(self):
        '''
        метод меняет положения мяча
        :return:
        '''
        draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 1500х780).
        """

        if ((self.x + self.r >= 1500 and self.vx > 0) or (self.x - self.r <= 0 and self.vx < 0)):
            self.vx *= -0.8
        if ((self.y + self.r >= 780 and self.vy > 0) or (self.y - self.r <= 0 and self.vy < 0)):  # - 2 * self.r
            self.vy *= -0.8
        # if ((self.y + self.r >= 780)):
        #     self.vy = 0
        #     self.a = 0
        self.vy += self.a  # 0.08*abs(self.vy)
        self.vx -= 0.01 * self.vx
        self.x += self.vx
        self.y += self.vy

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5 <= self.r + obj.r):
            return True
        else:
            return False


class small_ball(ball):
    '''
    класс для нового типа снарядов, чтобы зарядить их зажмите 'z'
    '''

    def __init__(self, x=0, y=0):
        '''
        коструктор класса, x и y начальные координаты
        :param x:
        :param y:
        '''
        self.x = x
        self.y = y
        self.a = 1
        self.r = 5
        self.vx = 0
        self.vy = 0
        self.color = (0, 255, 255)
        draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение снаряда за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy
        """

        self.x += self.vx
        self.y += self.vy


class gun():
    '''
    класс Танка
    '''

    def __init__(self):
        '''
        коструктор для класса танка
        '''
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x = rnd(50, 1450)
        self.y = rnd(50, 730)
        self.x_gun = 0
        self.y_gun = 0
        self.speed = 3

    def fire2_start(self, event):
        '''
        начало стрельбы
        :return:
        '''
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        x, y = event.pos
        bullet += 1
        if (pygame.key.get_pressed()[pygame.K_z]):
            new_ball = small_ball(self.x_gun, self.y_gun)
        else:
            new_ball = ball(self.x_gun, self.y_gun)
        if (x - new_ball.x == 0):
            self.an = math.pi/2
        else:
            self.an = math.atan(abs(y - new_ball.y) / abs(x - new_ball.x))
        new_ball.vx = numpy.sign(x - self.x) * self.f2_power * math.cos(self.an)
        new_ball.vy = numpy.sign(y - self.y) * self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self):
        """Прицеливание. Зависит от положения мыши."""

        x, y = pygame.mouse.get_pos()
        if (x - self.x == 0):
            self.an = math.pi/2
        else:
            self.an = math.atan(abs(y - self.y) / abs(x - self.x))
        self.x_gun = self.x + numpy.sign(x - self.x) * max(self.f2_power, 20) * math.cos(self.an)
        self.y_gun = self.y + numpy.sign(y - self.y) * max(self.f2_power, 20) * math.sin(self.an)
        pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x_gun, self.y_gun), 7)

    def power_up(self):
        '''
        усиление пушки спустя время
        :return:
        '''
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1

    def gun_move(self):
        '''
        передвижение танка
        :return:
        '''
        if (pygame.key.get_pressed()[pygame.K_w]):
            g1.y += -self.speed
        else:
            if (pygame.key.get_pressed()[pygame.K_s]):
                g1.y += self.speed
        if (pygame.key.get_pressed()[pygame.K_a]):
            g1.x += -self.speed
        else:
            if (pygame.key.get_pressed()[pygame.K_d]):
                g1.x += self.speed
        draw.rect(screen, GREEN, (self.x - 20, self.y - 10, 40, 20))
        draw.circle(screen, DARK_GREEN, (self.x, self.y), 7)


class target():
    '''
    класс мишени - красного круго
    '''

    def __init__(self):
        '''
        коструктор вызывает метод, чтобы можно было в дальнейшем вызывать метод на уже существующий объект
        '''
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(50, 1450)
        y = self.y = rnd(50, 730)
        r = self.r = rnd(2, 50)
        self.a = choice([1, -1]) * rnd(1, 10)
        draw.circle(screen, RED, (self.x, self.y), self.r)

    def move(self):
        """Переместить мишегь по прошествии единицы времени.
        """
        if ((self.y - self.r) >= 780):
            self.y = 0 + self.r
        if (self.y + self.r <= 0):
            self.y = 780 + self.y
        self.y += self.a

    def set_coords(self):
        '''
        отрисовывеет мишень в новом месте
        :return:
        '''
        draw.circle(screen, RED, (self.x, self.y), self.r)


class square_t(target):
    '''
    класс мишени - черный квадрат
    '''

    def new_target(self):
        x = self.x = rnd(50, 1450)
        y = self.y = rnd(50, 730)
        r = self.r = rnd(2, 50)
        self.a = choice([1, -1]) * rnd(1, 15)
        draw.rect(screen, BLACK, (self.x - self.r, self.y - self.r, 2 * self.r, 2 * self.r))

    def set_coords(self):
        '''
        отрисовка квадратика
        :return:
        '''
        draw.rect(screen, BLACK, (self.x - self.r, self.y - self.r, 2 * self.r, 2 * self.r))

    def move(self):
        '''
        метод отвечает за движение квадрата спустя время
        :return:
        '''
        if ((self.x - self.r) >= 1500):
            self.x = 0 + self.r
        if (self.x + self.r < 0):
            self.x = 1500 - self.r
        self.x += self.a


def hit_happens():
    '''
    функция вызывается при столкновении снаряда и мишени
    :return:
    '''
    global bullet, lives, points, balls, targets, squares
    if targets:
        pass
    else:
        if squares:
            pass
        else:
            screen.fill(WHITE)
            text = font.render("Вы уничтожили цели за: " + str(bullet) + " выстрелов", True, BLACK)
            screen.blit(text, [250 + 180, 300])
            pygame.display.update()
            balls = []
            lives = 0
            points += 1


def new_targets_for_new_game():
    '''
    функция вызывается когда нужны новые цели для новой игры
    :return:
    '''
    global targets, squares, TARGETS_NUMBER
    for t in range(0, TARGETS_NUMBER):
        targets.append(target())
    for s in range(0, TARGETS_NUMBER):
        squares.append(square_t())


targets = []  # массив мишеней
squares = []

g1 = gun()
bullet = 0
balls = []
lives = 1  # важная вещь для проверки на стлокновение
font = pygame.font.Font(None, 50)
pygame.display.update()
clock = pygame.time.Clock()


def new_game():
    '''
    основной цикл программы
    :param event:
    :return:
    '''
    global targets, lives, balls, bullet, FPS, clock, points, zleep, g1  # t1

    for t in targets:  # создаем новые цели в игре
        t.new_target()
    for s in squares:  # создаем новые цели в игре
        s.new_target()
    new_targets_for_new_game()
    lives = 1
    g1 = gun()
    bullet = 0
    balls = []
    while (lives == 1 or balls):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                g1.fire2_start(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                g1.fire2_end(event)

        g1.gun_move()
        g1.targetting()
        for t in targets:
            t.move()
            t.set_coords()
        for s in squares:
            s.move()
            s.set_coords()
        for b in balls:  # для движения мячей нужен данный цикл
            b.move()
            b.set_coords()
            for t in targets:
                if b.hittest(t):  # данное условие выполняется при столкновении
                    balls.remove(b)
                    targets.remove(t)
                    hit_happens()
            for s in squares:
                if b.hittest(s):  # данное условие выполняется при столкновении
                    balls.remove(b)
                    squares.remove(s)
                    hit_happens()
        text_score = font.render(str(points), True, BLACK)
        screen.blit(text_score, [30, 30])
        pygame.display.update()
        g1.power_up()
        screen.fill(WHITE)  # для исчезания прошлого рисунка
    time.sleep(zleep)
    new_game()


new_game()
