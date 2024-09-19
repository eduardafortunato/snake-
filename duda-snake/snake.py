#Título: criando uma tela inicial de game
#link do material da aula: https://bit.ly/pythontela01

#Setup de Entrada - Import Bibliotecas-----------------------------------------#
import pygame, sys

#Setup de Entrada - Definições ----------------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
# Configura a janela
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Grade Dinâmica")
font = pygame.font.Font('freesansbold.ttf', 32)
#magem_fundo = pygame.image.load('background.png').convert() #nao achou a imagem


#Definição de Escrita de Texto------------------------------------------------#
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

#Definição de ações do Menu Inicial--------------------------------------------#
def main_menu():
    while True:

        screen.fill ((255,203,219)) #cor da tela 
        draw_text('COBRAS E PIQUINIQUES', font, (41,1,6), screen, 240, 40) #cor da fonte

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(300, 200, 200, 50)
        button_2 = pygame.Rect(300, 300, 200, 50)
        button_3 = pygame.Rect(300, 400, 200, 50)
        button_4 = pygame.Rect(300, 500, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_4.collidepoint((mx, my)):#botão novo
            if click:
                novidades() #defini para qual tela vou ao clicar no botão novo
        if button_3.collidepoint((mx, my)):
            if click:
                exite()
        pygame.draw.rect(screen, (41,1,6), button_1)
        pygame.draw.rect(screen, (41,1,6), button_2)
        pygame.draw.rect(screen, (41,1,6), button_3) # cor do botão 
        pygame.draw.rect(screen, (41,1,6), button_4)
        draw_text('JOGAR', font, (255, 255, 255), screen, 350, 215)
        draw_text('OPÇÕES', font, (255, 255, 255), screen, 340, 315)
        draw_text('SAIR', font, (255, 255, 255), screen, 365, 415) #cor e posição do texto
        draw_text('PLACAR', font, (255, 255, 255), screen, 340, 515)# texto do novo botão
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

#Definições dos Submenus dos Botões - Game - Opções - Sair --------------------#
def game():
    running = True
    while running:
        screen.fill((255,203,219))

        draw_text('JOGAR', font, (41,1,6), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    while running:
        screen.fill((255,203,219))

        draw_text('OPÇÕES', font, (41,1,6), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)
      
def novidades(): 
  running = True
  while running:
    #defino tela de novidades
      screen.fill((255,203,219))

      draw_text('PLACAR', font, (41,1,6), screen, 20, 20) #textos e infos

    # defino os eventos do novo botão (sair da tela)
      for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
          if event.type == KEYDOWN:
              if event.key == K_ESCAPE:
                  running = False

      pygame.display.update()
      mainClock.tick(60)

def exite():
    pygame.quit()
    sys.exit()


main_menu()
    # Atualiza a tela
pygame.display.flip()

#screen.blit(imagem_fundo, (0, 0))