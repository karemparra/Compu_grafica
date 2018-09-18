import pygame
import math
import karem

Ancho=700
Alto=500

centro = [350,250]
pos = [350,220]


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])

#Cosas estaticas
    pygame.draw.line(pantalla, karem.blanco, [0,centro[1]], [700,centro[1]], 2)
    pygame.draw.line(pantalla, karem.blanco, [centro[0],0], [centro[0],700], 2)
    pygame.draw.circle(pantalla, karem.morado,pos,2)
    pygame.display.flip()
    reloj = pygame.time.Clock()

    fin=False
    while not fin:
        for event in pygame.event.get():          #Eventos que pasan cada que...
            if event.type == pygame.QUIT:
                fin=True



        pos = karem.trasladarCP(pos,centro)
        print (pos)
        pos = karem.rotacion(pos,10)
        pos = karem.trasladarPC(pos,centro)
        pygame.draw.circle(pantalla, karem.morado, [int(pos[0]), int(pos[1])],2)
        pygame.display.flip()
        reloj.tick(10)



        reloj.tick(100)
        ##pantalla.fill(karem.negro)
