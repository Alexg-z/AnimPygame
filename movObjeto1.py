import pygame as py
import sys

NEGRO = (10,8,12)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
MORADO = (128, 0, 128)

# Crear escenarios utilizando funciones
def dibujarPistaVertical():
    py.draw.rect(pantalla, NEGRO, [160,0,160,620])
    for i in range(10,610,20):
        py.draw.rect(pantalla,BLANCO,[234,i,6,8])
    

def dibujarPistaHorizontal():
    py.draw.rect(pantalla, NEGRO, [0,160,620,160])
    for i in range(10,610,20):
        py.draw.rect(pantalla,BLANCO,[i,234,8,6])

#Inicialización del juego/Biblioteca
py.init()

#Bucle
#Funcion horizontal
dimension1 = [620, 480]
dimension2 = [480,620]

pantalla = py.display.set_mode(dimension1)
py.display.set_caption("Animaciones Manuales")

hecho = False
reloj = py.time.Clock()

#
x = 0 
x2 = 580
y = 480


while not hecho:
    for evento in py.event.get():
        if evento.type == py.QUIT:
            hecho = True
    pantalla.fill(VERDE)
    #dibujarPistaVertical()
    dibujarPistaHorizontal()
    #Cuadro Rojo
    py.draw.rect(pantalla, ROJO,[x,190,30,20])
    x+=1
    #Cuadro Morado
    py.draw.rect(pantalla, MORADO,[x2,260,30,20])
    x2-=1
    py.display.flip()
    reloj.tick(20)

py.quit()