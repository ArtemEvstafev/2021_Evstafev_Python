import pygame
import pygame.draw as d

pygame.init()
FPS = 30
screen = pygame.display.set_mode((1500, 780), pygame.SRCALPHA)  # инициализация экрана
surface1 = screen.convert_alpha()
surface1.fill([0,0,0,0])

def medvedR(size, x, y):
    #d.rect(screen, (0, 0, 0), (x, y, size, size), 1)
    N = size
    d.ellipse(screen, (255, 255, 255), (x, y + N / 8, N * 3 / 8, N * 0.75), 0)  # body
    d.ellipse(screen, (0, 0, 0), (x, y + N / 8, N * 3 / 8, N * 0.75), 1)

    d.ellipse(screen, (255, 255, 255), (x + N / 8, y, N * 3 / 8, 3 * N / 16), 0)  # head
    d.ellipse(screen, (0, 0, 0), (x + N / 8, y, N * 3 / 8, 3 * N / 16), 1)

    d.ellipse(screen, (255, 255, 255), (x + N / 8, y + N * (1 - 5 / 16), 5 * N / 16, 5 * N / 16), 0)  # leg
    d.ellipse(screen, (0, 0, 0), (x + N / 8, y + N * (1 - 5 / 16), 5 * N / 16, 5 * N / 16), 1)

    d.ellipse(screen, (255, 255, 255), (x + N * (1 / 4 + 1 / 16), y + N * (1 - 3 / 32), 7 * N / 32, 3 * N / 32),
              0)  # feet
    d.ellipse(screen, (0, 0, 0), (x + N * (1 / 4 + 1 / 16), y + N * (1 - 3 / 32), 7 * N / 32, 3 * N / 32), 1)

    d.line(screen, (0, 0, 0), (x + N * 3 / 8, y + N / 2), (x + N * 3 / 4, y), 5)  # fishing rod

    d.ellipse(screen, (255, 255, 255), (x + N * (1 / 4 + 1 / 16), y + N * 0.4, 7 * N / 32, 3 * N / 32), 0)  # arm
    d.ellipse(screen, (0, 0, 0), (x + N * (1 / 4 + 1 / 16), y + N * 0.4, 7 * N / 32, 3 * N / 32), 1)

    d.ellipse(screen, (169, 169, 169), (x + N / 2, y + N * (1 - 4 / 16), N / 2, 4 * N / 16), 0)  # proryb
    d.ellipse(screen, (0, 0, 0), (x + N / 2, y + N * (1 - 4 / 16), N / 2, 4 * N / 16), 1)

    d.ellipse(screen, (0, 0, 102), (x + N * (0.5 + (1 / 2 - 7 / 16) / 2), y + N * (1 - 3 / 16), 7 * N / 16, 3 * N / 16),0)  # water
    d.ellipse(screen, (0, 0, 0), (x + N * (0.5 + (1 / 2 - 7 / 16) / 2), y + N * (1 - 3 / 16), 7 * N / 16, 3 * N / 16),1)

    d.line(screen, (0, 0, 0), (x + N * 3 / 4, y), (x + N * 3 / 4, y + N * (1 - 1 / 8)), 2)  # spinning

    d.line(screen, (0, 0, 0), (x + N * 5 / 16, y + 9 / 64 * N), (x + N * 15 / 32, y + 9 / 64 * N), 2)  # mouth

    d.circle(screen, (0, 0, 0), (x + N * 16 / 32, y + 5 / 64 * N), 7*N/600, 0)  # nose

    d.circle(screen, (0, 0, 0), (x + N * 10 / 32, y + 4 / 64 * N), 9*N/600, 0)  # eye

    d.circle(screen, (255, 255, 255), (x + N * 5 / 32, y + 2 / 64 * N), 18*N/600, 0)  # ear
    d.circle(screen, (0, 0, 0), (x + N * 5 / 32, y + 2 / 64 * N), 18*N/600, 1)
def landscape():
    d.rect(screen, (0, 190, 240), (0, 0, 1500, 390), 0)  # небо
    d.rect(screen, (255, 255, 255), (0, 390, 1500, 390), 0)  # лед
    d.circle(surface1, (255, 255, 255, 150), (1125, 150), 150, 25)  # the Sun
    d.line(surface1, (255, 255, 255, 150), (975, 150), (1275, 150), 25)
    d.line(surface1, (255, 255, 255, 150), (1125, 300), (1125, 0), 25)
    d.circle(surface1, (255, 255, 255, 200), (1125, 150), 15, 0)
    d.circle(surface1, (255, 255, 255, 200), (1275, 150), 15, 0)
    d.circle(surface1, (255, 255, 255, 200), (975, 150), 15, 0)
    d.circle(surface1, (255, 255, 255, 200), (1125, 300), 15, 0)
    d.circle(surface1, (255, 255, 255, 200), (1125, 0), 15, 0)
def medvedL(size, x, y):
    d.rect(screen, (0, 0, 0), (x, y, size, size), 1)
    N = size
    d.ellipse(screen, (255, 255, 255), (x+N*(1-3/8), y + N / 8, N * 3 / 8, N * 0.75), 0)  # body
    d.ellipse(screen, (0, 0, 0), (x+N*(1-3/8), y + N / 8, N * 3 / 8, N * 0.75), 1)

    d.ellipse(screen, (255, 255, 255), (x + N*(1-1/2), y, N * 3 / 8, 3 * N / 16), 0)  # head
    d.ellipse(screen, (0, 0, 0), (x + N*(1-1/2), y, N * 3 / 8, 3 * N / 16), 1)

    d.ellipse(screen, (255, 255, 255), (x + N*(1-1/8-5/16), y + N * (1 - 5 / 16), 5 * N / 16, 5 * N / 16), 0)  # leg
    d.ellipse(screen, (0, 0, 0), (x + N*(1-1/8-5/16), y + N * (1 - 5 / 16), 5 * N / 16, 5 * N / 16), 1)

    d.ellipse(screen, (255, 255, 255), (x + N * (1 - 5/16 - 7/32), y + N * (1 - 3 / 32), 7 * N / 32, 3 * N / 32),0)  # feet
    d.ellipse(screen, (0, 0, 0), (x + N * (1 - 5/16 - 7/32), y + N * (1 - 3 / 32), 7 * N / 32, 3 * N / 32), 1)

    d.line(screen, (0, 0, 0), (x + N * (1 - 3 / 8), y + N / 2), (x + N * 1 / 4, y), 5)  # fishing rod

    d.ellipse(screen, (255, 255, 255), (x + N * (1 / 4 + 1 / 16), y + N * 0.4, 7 * N / 32, 3 * N / 32), 0)  # arm
    d.ellipse(screen, (0, 0, 0), (x + N * (1 / 4 + 1 / 16), y + N * 0.4, 7 * N / 32, 3 * N / 32), 1)

    #d.ellipse(screen, (169, 169, 169), (x + N / 2, y + N * (1 - 4 / 16), N / 2, 4 * N / 16), 0)  # proryb
    #d.ellipse(screen, (0, 0, 0), (x + N / 2, y + N * (1 - 4 / 16), N / 2, 4 * N / 16), 1)

    #d.ellipse(screen, (0, 0, 102), (x + N * (0.5 + (1 / 2 - 7 / 16) / 2), y + N * (1 - 3 / 16), 7 * N / 16, 3 * N / 16),0)  # water
    #d.ellipse(screen, (0, 0, 0), (x + N * (0.5 + (1 / 2 - 7 / 16) / 2), y + N * (1 - 3 / 16), 7 * N / 16, 3 * N / 16),1)

    d.line(screen, (0, 0, 0), (x + N * 3 / 4, y), (x + N * 3 / 4, y + N * (1 - 1 / 8)), 2)  # spinning

    d.line(screen, (0, 0, 0), (x + N * 5 / 16, y + 9 / 64 * N), (x + N * 15 / 32, y + 9 / 64 * N), 2)  # mouth

    d.circle(screen, (0, 0, 0), (x + N * 16 / 32, y + 5 / 64 * N), 7 * N / 600, 0)  # nose

    d.circle(screen, (0, 0, 0), (x + N * 10 / 32, y + 4 / 64 * N), 9 * N / 600, 0)  # eye

    d.circle(screen, (255, 255, 255), (x + N * 5 / 32, y + 2 / 64 * N), 18 * N / 600, 0)  # ear
    d.circle(screen, (0, 0, 0), (x + N * 5 / 32, y + 2 / 64 * N), 18 * N / 600, 1)


# d.rect(screen, (red, green, blue), (x_topleft, y_topleft,ширина ,высота ), width)
# d.polygon(screen, (red, green, blue), [(x1, y1), (x2, y2),(x3, y3), (x4, y4)], width)
# d.circle(screen, (red, green, blue), (x, y), R, width)
# d.ellipse(screen, (red, green, blue), (x_topleft, y_topleft,ширина ,высота ), width)

landscape()
medvedL(600, 300, 160)
#medvedL(300, 1000, 400)




screen.blit(surface1, (0,0))
pygame.display.update()  # бновление экрана для отображения картинок
clock = pygame.time.Clock()  # добавление FPS в экран
clock.tick(FPS)  # --
finish = False  # --

while not finish:  # это выход из программы
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
pygame.quit()
