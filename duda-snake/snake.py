import pygame, sys
import math
import random
import time

pygame.init()

largura_janela = 1920   
altura_janela = 1080
pygame.display.set_caption('jogo da galinha')
clock = pygame.time.Clock()

fgExit = False

cenario= pygame.image.load('menu.png')
personagem= pygame.image.load('snake.right.png')
personagemup= pygame.image.load('snake.up.png')
personagemdo= pygame.image.load('snake.down.png')
personagemle= pygame.image.load('snake.left.png')
personagemri= pygame.image.load('snake.right.png')
personagem2 = pygame.image.load ('maca.png')

tela = pygame.display.set_mode((largura_janela, altura_janela))
x = (largura_janela * 0.1)
y = (altura_janela * 0.5)#posiöäao do personagem
x1 = 0
x2 = 0
y1 = 0
y2 = 0
personagem_speed = 0

xpersonagem = x+45
ypersonagem = y+65
xpersonagem2 = 500+96 #atenção! 128 é o raio do meu cogumelo!
ypersonagem2 = 300+96
x_1 = x
y_1 = y
t = 0

def colisão():
    distancia =  math.sqrt(math.pow(xpersonagem-xpersonagem2,2)+math.pow(ypersonagem-ypersonagem2,2))
    print (distancia)
    if distancia<96+50:
        return True
    else:
        return False

while not fgExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fgExit = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x1 = 0
            if event.key == pygame.K_RIGHT:
                x2 = 0
            if event.key == pygame.K_UP:
                y1 = 0
            if event.key == pygame.K_DOWN:
                y2 = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1 = -5
                personagem = personagemle
            if event.key == pygame.K_RIGHT:
                x2 = 5
                personagem = personagemri
            if event.key == pygame.K_UP:
                y1 = -5
                personagem = personagemup
            if event.key == pygame.K_DOWN:
                y2 = 5
                personagem = personagemdo #personagem se mexe pra direção da tecla 

    x += x1 + x2
    y += y1 + y2
    xpersonagem = x+45
    ypersonagem = y+65
    if colisão():
        tela.fill((0,0,0))
        pygame.display.update()
        time.sleep(4)
        pygame.quit()
        x = x_1
        y = y_1                       
    else:
        x_1 = x
        y_1 = y

    tela.blit(cenario,(0,0))
    tela.blit(personagem, (x, y))
    tela.blit(personagem2, ( xpersonagem2 -96 , ypersonagem2 -96 ))
    pygame.display.update()
    clock.tick(60)


pygame.quit()