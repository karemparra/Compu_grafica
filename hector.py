import pygame
import math

def rotarP(punto, angulo):
    a = math.radians(angulo)

    x = (((math.cos(a)))*punto[0]) - (((math.sin(a)))*punto[1])
    y = (((math.sin(a)))*punto[0]) + (((math.cos(a)))*punto[1])

    return [x,y]

def trasladarPL (punto, centro):
    x = punto[0]+centro[0]
    y = (-punto[1])+centro[1]
    return [x,y]

def trasladarPLinv (punto, centro):
    x = punto[0]+(-centro[0])
    y = punto[1]+(-centro[1])
    return [x,-y]

Ancho = 700
Alto = 500
centro = [350,250]
p1 = []
p2 = []

var = 0
if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([Ancho, Alto])

    a = [100, 50]
    b = [175, 50]


    pygame.draw.line(pantalla, [255,0,23], [0,centro[1]], [Ancho,centro[1]])
    pygame.draw.line(pantalla, [255,0,23], [centro[0],0], [centro[0],Alto])
    aini = 0
    reloj = pygame.time.Clock()
    fin = False
    while not fin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if var != 1:
                    if p1 == []:
                        p1 = list(pygame.mouse.get_pos())
                    else:
                        p2 = list(pygame.mouse.get_pos())
                        var = 1

        #ap = rotarP([100, 50], aini)
        #bp = rotarP([175, 50], aini)
        if var == 1:
            car1 = p1
            car2 = p2
            var = 2
        if var == 2:
            pygame.draw.line(pantalla, [255,0,23], p1, p2)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    car1 = trasladarPLinv(car1, centro)
                    car1 = rotarP(car1,2)
                    car1 = trasladarPL(car1,centro)
                    car2 = trasladarPLinv(car2, centro)
                    car2 = rotarP(car2,2)
                    car2 = trasladarPL(car2,centro)
                    pygame.draw.line(pantalla, [255,0,23], car1, car2)



        pygame.display.flip()
        aini+=2
        reloj.tick(300)
