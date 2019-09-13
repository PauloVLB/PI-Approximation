#!/usr/bin/env python

import cv2
import numpy as np
from random import randint
#from Tkinter import *
import easygui

lado = 500
imgCirculo = np.zeros((lado,lado,3), np.uint8) # fundo
larguraImgCirculo = imgCirculo.shape[1] 
alturaImgCirculo = imgCirculo.shape[0] 


centroCirculo = (larguraImgCirculo/2, alturaImgCirculo/2)
raioCirculo = larguraImgCirculo/2
corCirculo = (255,255,255)
cv2.circle(imgCirculo, centroCirculo, raioCirculo, corCirculo) # circulo maior


nPontos = float(0)
pontosDentro = float(0)
maxPontos = float(1)

def desenharPonto(img, centro, cor):
    #cor = (0,0,255)
    grossura = 1
    cv2.circle(img, centro, 1, cor, grossura)

def escreverEmDados(img, texto, org):
    cor = (255,255,255)
    cv2.putText(img, texto, org, cv2.FONT_HERSHEY_SIMPLEX, .6, cor)


maxPontos = float(easygui.enterbox("Numero maximo de pontos: "))

while (True):
    imgDados = np.zeros((80, 300,3), np.uint8)
    larguraImgDados = imgDados.shape[1]
    alturaImgDados = imgDados.shape[0]

    if nPontos < maxPontos:
        cor = (0,0, 255)

        x = randint(0, larguraImgCirculo)
        y = randint(0, alturaImgCirculo)
        nPontos += 1

        xT = ((larguraImgCirculo/2)-x)*-1
        yT = ((alturaImgCirculo/2)-y)

        distanciaPonto = (xT ** 2 + yT ** 2) ** .5
        if distanciaPonto < lado/2:
            pontosDentro += 1
            cor = (0, 255, 0) 

        desenharPonto(imgCirculo, (x, y), cor)

    percentual = float((pontosDentro*100)/nPontos)
    pi = ((float(percentual)/float(100))*(float(lado)**2))/((float(lado)/float(2))**2)
    
    escreverEmDados(imgDados, 'nPontos: ' + str(nPontos), (0, 20))
    escreverEmDados(imgDados, 'Percentual: ' + str(percentual) + '%', (0, 40))
    escreverEmDados(imgDados, 'Aprox PI: ' + str(pi), (0, 60))

    cv2.imshow('Dados', imgDados)
    if nPontos == 1:
        cv2.moveWindow('Dados', lado, 0)
    cv2.imshow('AreaCirculo', imgCirculo)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()