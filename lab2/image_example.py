import pygame
import pygame.draw as d
pygame.init()
FPS = 30
def shtrih():#пример штриховки
    x1 = 100; y1 = 100
    x2 = 300; y2 = 200
    N = 10
    color = (255, 255, 255)
    d.rect(screen, color, (x1, y1, x2 - x1, y2 - y1), 2)
    h = (x2 - x1) // (N + 1)
    x = x1 + h
    for i in range(N):
        d.line(screen, color, (x, y1), (x, y2))
        x += h
screen = pygame.display.set_mode((400, 400))#инициализация экрана

d.rect(screen, (255, 0, 255), (100, 100, 200, 200))
d.rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
d.polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               (300,100), (100,100)])
d.polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               (300,100), (100,100)], 5)
d.circle(screen, (0, 255, 0), (200, 175), 50)
d.circle(screen, (255, 255, 255), (200, 175), 50, 5)

pygame.display.update()#бновление экрана для отображения картинок
clock = pygame.time.Clock()#добавление FPS в экран
clock.tick(FPS)            #--
finish = False             #--

while not finish: #это выход из программы
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
pygame.quit()
