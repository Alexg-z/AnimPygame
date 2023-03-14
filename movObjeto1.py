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

pantalla = py.display.set_mode(dimension2)
py.display.set_caption("Animaciones Manuales")

hecho = False
reloj = py.time.Clock()

#
x = 0
x2 = 270
y = 0
y2 = 620


while not hecho:
    for evento in py.event.get():
        if evento.type == py.QUIT:
            hecho = True
    pantalla.fill(VERDE)
    dibujarPistaVertical()
    #dibujarPistaHorizontal()
    #Cuadro Rojo
    py.draw.rect(pantalla, ROJO,[190,y,20,30])
    x+=1
    y+=1
    #Cuadro Morado
    if y2 > 300:
        x = 190
    if y2 < 350:
        #x = 260
        for i in range(190,260,5):
            x = i
        
        
    py.draw.rect(pantalla, MORADO,[x,y2,20,30])
    x2-=1
    y2-=1
    py.display.flip()
    reloj.tick(60)

py.quit()