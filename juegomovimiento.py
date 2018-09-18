import karem
import pygame
import random


Ancho=700
Alto=500

centro=[350,250]
pos =[0,0]


class Jugadores(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill(karem.blanco)
        self.rect = self.image.get_rect()
        self.vel_x=0
        self.vel_y=0

    def update(self):
        self.rect.y+=self.vel_y

class Rival(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([30,30])
        self.image.fill(karem.verde)
        self.rect = self.image.get_rect()
        self.vel_x=2

    def update(self):
        if(self.rect.x>670):
            self.vel_x = -2
        if(self.rect.x<0):
            self.vel_x = 2
        self.rect.x+=self.vel_x


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])

    jugadores = pygame.sprite.Group()
    j1 = Jugadores()
    j1.rect.x=100
    j1.rect.y=100
    jugadores.add(j1)

    n=10
    rivales=pygame.sprite.Group()
    for i in range(n):
        r=Rival()
        r.rect.x=random.randrange(Ancho)
        r.rect.y=random.randrange(Alto)
        rivales.add(r)

    reloj = pygame.time.Clock()
    puntos=0
    #salud=300
    fin=False
    while not fin:
        for event in pygame.event.get():          #Eventos que pasan cada que...
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                        j1.vel_y= 4
                if event.key == pygame.K_UP:
                        j1.vel_y = -4
            if event.type == pygame.KEYUP:
                j1.vel_y=0

        listaCol = pygame.sprite.spritecollide(j1,rivales,True) #Colision
        #listaCol = pygame.sprite.spritecollide(j1,rivales,False)
        for r in listaCol:
            puntos+=1
            print (puntos)
            #salud-=1
            #print salud

        jugadores.update()
        rivales.update()
        pantalla.fill(karem.negro)
        jugadores.draw(pantalla)
        rivales.draw(pantalla)
        pygame.display.flip()
        reloj.tick(50)
