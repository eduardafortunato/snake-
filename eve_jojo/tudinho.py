import pygame
import menu
import jogo

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo da Cobrinha")

# Variável global para controlar o estado
ESTADO_ATUAL = "menu"

def trocar_tela(novo_estado):
    global ESTADO_ATUAL
    ESTADO_ATUAL = novo_estado
    pygame.display.flip()  # Limpa a tela

# Loop principal do jogo
running = True
while running:
    if ESTADO_ATUAL == "menu":
        menu.main_loop()
    elif ESTADO_ATUAL == "jogo":
        jogo.main_loop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()