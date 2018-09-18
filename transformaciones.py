import math
import pygame

class Transformaciones:


    """Contiene todas las transformaciones necesarias, como:
    rotacion, traslacion, traslacion de punto cartesiano a pantalla,
    transformacion de plano polar a punto y viceversa, etc.
    """


    def trasSimple(self, t, *p):
        if len(p) > 1:
            puntos = []
            for px in p:
                tr = []
                tr.append(px[0] + t[0])
                tr.append(px[1] + t[1])
                puntos.append(tr)
            return puntos
        else:
            tr = []
            tr.append(p[0][0] + t[0])
            tr.append(p[0][1] + t[1])
            return tr


    def trasCartePantalla(self, c, *p):
        if len(p) > 1:
            puntos = []
            for px in p:
                tc = []
                tc.append(px[0] + c[0])
                tc.append(-1*px[1] + c[1])
                puntos.append(tc)
            return puntos
        else:
            tc = []
            tc.append(p[0][0] + c[0])
            tc.append(-1*p[0][1] + c[1])
            return tc


    def trasPantallaCarte(self, c, *p):
        if len(p) > 1:
            puntos = []
            for px in p:
                tp = []
                tp.append(px[0] - c[0])
                tp.append(c[1] - px[1])
                puntos.append(tp)
            return puntos
        else:
            tp = []
            tp.append(p[0][0] - c[0])
            tp.append(c[1] - p[0][1])
            return tp

    def rotacionSimple(self, tetha, *p):
        theta = math.radians(tetha)
        if len(p) > 1:
            puntos = []
            for px in p:
                r = []
                r.append(px[0]*math.cos(theta) - px[1]*math.sin(theta))
                r.append(px[0]*math.sin(theta) + px[1]*math.cos(theta))
                puntos.append(r)
            return puntos
        else:
            r = []
            r.append(p[0][0]*math.cos(theta) - p[0][1]*math.sin(theta))
            r.append(p[0][0]*math.sin(theta) + p[0][1]*math.cos(theta))
            return r

    def rotacionReferencia(self, ref, theta, *p):
        p = list(p)
        p = [self.trasSimple([-1* i for i in ref], px) for px in p]
        p = [self.rotacionSimple(theta, py) for py in p]
        p = [self.trasSimple(ref, pz) for pz in p]
        if len(p) > 1:
            return p
        else:
            return p[0]

    def escalamientoSimple(self, e, *p):
        if len(p) > 1:
            puntos = []
            for px in p:
                ep = []
                ep.append(px[0]*e[0])
                ep.append(c[1]*e[1])
                puntos.append(ep)
            return puntos
        else:
            ep = []
            ep.append(p[0][0]*e[0])
            ep.append(p[0][1]*e[1])
            return ep

    def escalamientoReferencia(self, ref, e, *p):
        p = list(p)
        p = [self.trasSimple([-1* i for i in ref], px) for px in p]
        p = [self.escalamientoSimple(e, py) for py in p]
        p = [self.trasSimple(ref, pz) for pz in p]
        if len(p) > 1:
            return p
        else:
            return p[0]

    def dibujarPlano(self, pantalla, w, h, c):
        pygame.draw.line(pantalla, [255,255,255], [c[0], 0], [c[0], h])
        pygame.draw.line(pantalla, [255,255,255], [0, c[1]], [w, c[1]])

    def dibujarFiguraRegular(self, pantalla, pIni, nLados, centro):
        grados = 360*1.0/nLados
        puntos = [pIni]
        for i in range(nLados-1):
            puntos.append(self.rotacionReferencia(centro, grados, puntos[i]))
            pygame.draw.line(pantalla, [255, 255, 255], puntos[i], puntos[i+1])
        pygame.draw.line(pantalla, [255, 255, 255], puntos[len(puntos) - 1], puntos[0])
        return puntos

    def dibujarFigura(self, pantalla, puntos):
        ultimo = len(puntos)-1
        for i in range(ultimo):
            pygame.draw.line(pantalla, [255, 255, 255], puntos[i], puntos[i+1])
        pygame.draw.line(pantalla, [255, 255, 255], puntos[ultimo], puntos[0])

    def polarPunto(self, *p):
        if len(p) > 1:
            puntos = []
            for px in p:
                l = []
                l.append(int(px[0] * math.cos(math.radians(px[1]))))
                l.append(int(px[0] * math.sin(math.radians(px[1]))))
                puntos.append(l)
            return puntos
        else:
            l = []
            l.append(int(p[0][0] * math.cos(math.radians(p[0][1]))))
            l.append(int(p[0][0] * math.sin(math.radians(p[0][1]))))
            return l

    def puntoPolar(self, *p):
        if len(p) > 1:
            puntos = []
            for px in p:
                l = []
                l.append(math.sqrt(px[0]**2 + px[1]**2))
                l.append(math.degrees(math.atan(px[1]*1.0/px[0])))
                puntos.append(l)
            return puntos
        else:
            l = []
            l.append(math.sqrt(p[0][0]**2 + p[0][1]**2))
            l.append(math.degrees(math.atan(p[0][1]*1.0/p[0][0])))
            return l
