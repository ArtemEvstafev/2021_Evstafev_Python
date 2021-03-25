from random import randrange as rnd, choice
import math
import time
import pygame
import pygame.draw as draw



TARGETS_NUMBER = 1
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]

pygame.init()
FPS = 30
screen = pygame.display.set_mode( (800, 600))
screen.fill(WHITE)

class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.a = 1
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown', 'black'])
        draw.circle(screen, self.color, (self.x, self.y), self.r)
        self.live = 30

    def set_coords(self):
        draw.circle(screen, self.color, (self.x, self.y), self.r)


    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        if ((self.x + self.r >= 800 or self.x - self.r <= 0) and self.vx > 0):
            self.vx *= -0.8
        if ((self.y + self.r >= 590 - 2 * self.r or self.y - self.r <= 0) and self.vy > 0):
            self.vy *= -0.8
        if ((self.y + self.r >= 600)):
            self.vy = 0
            self.a = 0
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
        # FIXME
        if (((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5 <= self.r + obj.r):
            return True
        else:
            return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = pygame.draw.line(screen, (0, 0, 0), (20, 450), (50, 420), 7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        event.x, event.y = event.pos
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        event.x, event.y = event.pos

        self.an = math.atan((event.y - 450) / (event.x - 20))
        pygame.draw.line(screen, (0, 0, 0), (20, 450),
                         (20 + max(self.f2_power, 20) * math.cos(self.an),
                          450 + max(self.f2_power, 20) * math.sin(self.an)), 7)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1



class target():
    def __init__(self):
        # self.points = 0
        global points
        self.live = 1
        #self.id = draw.circle(screen, (255, 255, 255), (0, 0), 0)
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        self.a = choice([1, -1, 2, -2, 3, -3])
        self.color = RED
        draw.circle(screen, self.color, (self.x, self.y), self.r)

    def hit(self):
        """Попадание шарика в цель."""
        global points
        #draw.circle(screen, (255, 255, 255), (-10, -10), 0)
        points += 1
        #canv.itemconfig(self.id_points, text=points)

    def move(self):
        """Переместить мишегь по прошествии единицы времени.
        """
        if ((self.y - self.r) >= 600):
            self.y = 0 + self.r
        if (self.y + self.r <= 0):
            self.y = 600 + self.y
        self.y += self.a

    def set_coords(self):
        x = self.x
        y = self.y
        r = self.r
        draw.circle(screen, (255, 0, 0), (x, y), r)

points = 0
targets = []  # массив мишеней
for t in range(0, TARGETS_NUMBER):
    targets.append(target())

#screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []
lives = 1  # важная вещь для проверки на стлокновение
#текст
font = pygame.font.Font(None, 27)
text = font.render("Вы уничтожили цель за: " + str(bullet) + " выстрелов", True, BLACK)  # обновление счета после попадания


pygame.display.update()
clock = pygame.time.Clock()

def new_game(event=''):  # основной цикл
    global targets, lives, balls, bullet, FPS, clock  # t1

    for t in targets:  # создаем новые цели в игре
        t.new_target()
        t.live = 1
    lives = 1
    bullet = 0
    balls = []
    z = 3
    while(lives == 1 or balls):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                g1.fire2_start(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                g1.fire2_end(event)
            elif event.type == pygame.MOUSEMOTION:
                g1.targetting(event)
        for t in targets:
            t.move()
            t.set_coords()
        for b in balls:  # для движения мячей нужен данный цикл
            b.move()
            b.set_coords()
            for t in targets:
                if b.hittest(t) and t.live:  # данное условие выполняется при столкновении
                    screen.fill(WHITE)
                    pygame.display.update()
                    text = font.render("Вы уничтожили цель за: " + str(bullet) + " выстрелов", True, BLACK)
                    screen.blit(text, [250, 300])
                    balls = []
                    lives = 0
                    t.hit()  # мяч попал, поэтому нужно сделать вот это
                    pygame.display.update()
        pygame.display.update()
        g1.power_up()
        screen.fill(WHITE)# для исчезания прошлого рисунка
    time.sleep(5)
    new_game()
new_game()
pygame.quit()
