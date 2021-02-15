import pygame
import pygame.draw as d
pygame.init()
FPS = 30
screen = pygame.display.set_mode((1500, 780))#инициализация экрана
def medved(size, x, y):
    d.rect(screen, (0, 0, 0), (x, y, size ,size ), 1)

#d.rect(screen, (red, green, blue), (x_topleft, y_topleft,ширина ,высота ), width)
#d.polygon(screen, (red, green, blue), [(x1, y1), (x2, y2),(x3, y3), (x4, y4)], width)
#d.circle(screen, (red, green, blue), (x, y), R, width)
#d.ellipse(screen, (red, green, blue), (x_topleft, y_topleft,ширина ,высота ), width)

d.rect(screen, (0, 190, 240), (0, 0,1500 ,390 ), 0)#небо
d.rect(screen, (255, 255, 255), (0, 390,1500 ,390 ), 0)#лед
medved(600, 300,160)


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
