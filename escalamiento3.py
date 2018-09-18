#Escalamiento punto fijo

import pygame
import math
from transformaciones import Transformaciones


ancho=600
alto=600
centro=[300,300]
trans = Transformaciones()

def apantalla(c,p):
    x = c[0] + p[0]
    y = c[1] - p[1]
    return [x,y]

def acartesiana(c,p):
    x=p[0]-c[0]
    y=c[1]-p[1]
    return [x,y]

def trasladarCP (puntoC, centro):    #CARTESIANAS A PANTALLA
    x = puntoC[0]+(-centro[0])
    y = puntoC[1]+(-centro[1])
    return [x,-y]

def trasladarPC (punto, centro):  #PANTALLA A CARTESIANAS
    x = punto[0]+centro[0]
    y = (-punto[1])+centro[1]
    return [x,y]

def escala(p,S):
    x = int(p[0]*S[0])
    y = int(p[1]*S[1])
    return [x,y]

def mov_00(p,f):
    x = p[0]-f[0]
    y = p[1]-f[1]
    return [x,y]

def mov_ori(p,f):
    x = p[0]+f[0]
    y = p[1]+f[1]
    return [x,y]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    pygame.draw.line(pantalla,0xff2d00,[0,300],[600,300])
    pygame.draw.line(pantalla,0xff2d00,[300,0],[300,600])
    var=0
    p1 = []
    p2 = []
    p3 = []
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] > centro[0] and pygame.mouse.get_pos()[1] > centro[1]:

                    if p1 == []:
                        p1 = list(pygame.mouse.get_pos())
                    elif p2 == []:
                        p2 = list(pygame.mouse.get_pos())
                    elif p3 == []:
                        p3 = list(pygame.mouse.get_pos())
                        var = 2
                        if p1[1] > p2[1] and p1[1] > p3[1]:
                            puntoMayor = [p1[0], p1[1]]
                            p1 = [p3[0], p3[1]]

                        elif p2[1] > p1[1] and p2[1] > p3[1]:
                            puntoMayor = p2
                            p2 = [p3[0], p3[1]]
                        elif p3[1] > p1[1] and p3[1] > p2[1]:
                            puntoMayor = p3

                        pygame.draw.polygon(pantalla,0xff2d00,[p1,p2,puntoMayor],5)


            if  event.type == pygame.KEYDOWN and var == 2:
                if event.key == pygame.K_e:
                    pantalla.fill([0,0,0])

                    pygame.draw.line(pantalla,0xff2d00,[0,300],[600,300])
                    pygame.draw.line(pantalla,0xff2d00,[300,0],[300,600])
                    x = trans.escalamientoReferencia(puntoMayor, [0.4,0.4],p1,p2)
                    p1 = x[0]
                    p2 = x[1]

                    pygame.draw.polygon(pantalla,0xff2d00,[p1,p2,puntoMayor],5)



        pygame.display.flip()
