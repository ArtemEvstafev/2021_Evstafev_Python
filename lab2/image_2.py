import pygame
import pygame.draw as d
pygame.init()
FPS = 30
screen = pygame.display.set_mode((1500, 780))#инициализация экрана
def medved(size, x, y):
    d.rect(screen, (0, 0, 0), (x, y, size ,size ), 1)
    N = size
    d.ellipse(screen, (255, 255, 255), (x,y+N/8 ,N*3/8 ,N*0.75 ), 0)#body
    d.ellipse(screen, (0, 0, 0), (x,y+N/8 ,N*3/8 ,N*0.75 ), 1)

    d.ellipse(screen, (255, 255, 255), (x+ N/8, y , N * 3 / 8, 3*N /16), 0)#head
    d.ellipse(screen, (0, 0, 0), (x+ N/8, y, N * 3 / 8, 3*N /16), 1)

    d.ellipse(screen, (255, 255, 255), (x + N / 8, y+N*(1-5/16), 5 * N / 16, 5 * N / 16), 0)  # leg
    d.ellipse(screen, (0, 0, 0), (x + N / 8, y+N*(1-5/16), 5 * N / 16, 5 * N / 16), 1)

    d.ellipse(screen, (255, 255, 255), (x + N*( 1/4+1/16), y + N * (1 - 3 / 32), 7 * N / 32, 3 * N / 32), 0)  # feet
    d.ellipse(screen, (0, 0, 0), (x + N *(1/ 4+1/16), y + N * (1 - 3 / 32), 7 * N / 32, 3 * N / 32), 1)

    d.line(screen,(0, 0, 0), (x+N*3/8, y+N/2), (x+N*3/4, y), 5)#fishing rod

    d.ellipse(screen, (255, 255, 255), (x + N * (1 / 4 + 1 / 16), y + N * 0.4, 7 * N / 32, 3 * N / 32), 0)  # arm
    d.ellipse(screen, (0, 0, 0), (x + N * (1 / 4 + 1 / 16), y + N * 0.4, 7 * N / 32, 3 * N / 32), 1)

    d.ellipse(screen, (169, 169, 169), (x + N / 2, y + N * (1 - 4 / 16),  N / 2, 4 * N / 16), 0)  # proryb
    d.ellipse(screen, (0, 0, 0), (x + N / 2, y + N * (1 - 4 / 16),  N / 2, 4 * N / 16), 1)

    d.ellipse(screen, (0, 0, 102), (x + N*(0.5+(1 / 2-7/16)/2), y + N * (1 - 3 / 16), 7* N / 16, 3 * N / 16), 0)  # water
    d.ellipse(screen, (0, 0, 0), (x + N*(0.5+(1 / 2-7/16)/2), y + N * (1 - 3 / 16), 7* N / 16, 3 * N / 16), 1)

    d.line(screen, (0, 0, 0), (x+N*3/4, y), (x + N * 3 / 4, y+N*(1-1/8), 2)#spinning

#d.rect(screen, (red, green, blue), (x_topleft, y_topleft,ширина ,высота ), width)
#d.polygon(screen, (red, green, blue), [(x1, y1), (x2, y2),(x3, y3), (x4, y4)], width)
#d.circle(screen, (red, green, blue), (x, y), R, width)
#d.ellipse(screen, (red, green, blue), (x_topleft, y_topleft,ширина ,высота ), width)

d.rect(screen, (0, 190, 240), (0, 0,1500 ,390 ), 0) #небо
d.rect(screen, (255, 255, 255), (0, 390,1500 ,390 ), 0) #лед
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
