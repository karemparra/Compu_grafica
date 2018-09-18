import math
import pygame

#COLORES
rojo=[225,0,0]
verde=[0,255,0]
azul=[0,0,255]
morado=[225,0,255]
amarillo=[255,255,0]
azulclaro=[0,255,255]
blanco =[255,255,255]
negro = [0,0,0]

def trasladarP (punto, centro): #mover el punto normal
    x = punto[0]+centro[0]
    y = punto[1]+centro[1]
    return [x,y]

def trasladarPC (punto, centro):  #PANTALLA A CARTESIANAS
    x = punto[0]+centro[0]
    y = (-punto[1])+centro[1]
    return [x,y]

def trasladarCP (puntoC, centro):    #CARTESIANAS A PANTALLA
    x = puntoC[0]+(-centro[0])
    y = puntoC[1]+(-centro[1])
    return [x,-y]

def escalamiento(punto,e):
    x = e[0]*punto[0]
    y = e[1]*punto[1]
    return [x,y]


def rotacion(punto, angulo):
    a = math.radians(angulo)

    x = (((math.cos(a)))*punto[0]) - (((math.sin(a)))*punto[1])
    y = (((math.sin(a)))*punto[0]) + (((math.cos(a)))*punto[1])

    return [(x),(y)]


def polaresPOC(p):    #POLARES A CARTESIANAS
    a = math.radians(p[1])

    x = (p[0]*math.cos(a))
    y = (p[0]*math.sin(a))
    return [int(x), int(y)]

def polaresCP0(p):    #CARTESIANAS A POLARES
    x = p[0]
    y = p[1]
    r = math.hypot(x, y)
    angulo = math.asin(y/r)

    return [int(r),math.degrees(angulo)]

"""
import pygame
import math
import karem

Ancho=700
Alto=500

centro=[350,250]


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])

#Cosas estaticas
    pygame.draw.line(pantalla, [255,0,255], [100,100], [100,200], 10)
    pygame.draw.polygon(pantalla, [255,255,150], [[200,200],[200,400],[100,300]])
    pygame.display.flip()
    reloj = pygame.time.Clock()

    fin=False
    while not fin:
        for event in pygame.event.get():          #Eventos que pasan cada que...
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                pygame.draw.polygon(pantalla, [255,0,250], [[200,200],[200,400],[100,300]])
                pygame.display.flip()
        reloj.tick(30)
        pantalla.fill(karem.negro)
"""
