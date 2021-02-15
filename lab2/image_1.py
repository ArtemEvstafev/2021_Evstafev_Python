import pygame
import pygame.draw as d
pygame.init()
FPS = 30
screen = pygame.display.set_mode((600, 600))#инициализация экрана

#d.rect(screen, (red, green, blue), (x_topleft, y_topleft,ширина ,высота ), width)
#d.polygon(screen, (red, green, blue), [(x1, y1), (x2, y2),(x3, y3), (x4, y4)], width)
#d.circle(screen, (red, green, blue), (x, y), R, width)

d.rect(screen, (255, 255, 255), (0, 0,600 ,600 ), 0)

d.circle(screen, (255, 255, 0), (300, 300), 200)#body

d.circle(screen, (255, 0, 0), (400, 240), 40)#right eye
d.circle(screen, (0, 0, 0), (400, 240), 20)

d.circle(screen, (255, 0, 0), (200, 240), 45)#left eye
d.circle(screen, (0, 0, 0), (200, 240), 25)

d.rect(screen, (0, 0, 0), (200, 360,200 ,40 ), 0)#mouth

d.polygon(screen, (0, 0, 0), [(245, 215), (260, 200),(60, 110), (45, 120)], 0) #left eyebrow
d.polygon(screen, (0, 0, 0), [(345, 225), (330, 210),(530, 120), (540, 135)], 0) #right eyebrow

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
