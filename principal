
import pygame
import random
from pygame.locals import *

# Cores
branco = (255,255,255)
preto = ((254,161,182))
cores_objetos = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (188,11,243)]
# (255, 255, 0) AMARELO, VERDE(0,255,0), VERMELHO(255,0,0), AZUL (0,255,0), ROXO (188,11,243)
# Dimensões da tela
largura_tela = 600
altura_tela = 600


pygame.init()
screen = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')

# Classe para a cobra
class Cobra:
    def __init__(self):
        self.corpo = [(200, 200), (210, 200), (220, 200), (230, 200)]
        self.cor = branco
        self.direcao = LEFT

    def mover(self):
        x = self.corpo[0][0]
        y = self.corpo[0][1]

        if self.direcao == UP:
            y -= 10
        elif self.direcao == DOWN:
            y += 10
        elif self.direcao == RIGHT:
            x += 10
        elif self.direcao == LEFT:
            x -= 10

        self.corpo.insert(0, (x, y))
        self.corpo.pop()

    def desenhar(self):
        for pos in self.corpo:
            pygame.draw.rect(screen, self.cor, pygame.Rect(pos[0], pos[1], 10, 10))

# Classe para o objeto
class Objeto:
    def __init__(self):
        self.pos = on_grid_random()
        self.cor = random.choice(cores_objetos)

    def desenhar(self):
        pygame.draw.rect(screen, self.cor, pygame.Rect(self.pos[0], self.pos[1], 10, 10))

# Função para gerar posição aleatória na grade
def on_grid_random():
    x = random.randint(0, 59)
    y = random.randint(0, 59)
    return x * 10, y * 10

# Função para verificar colisão
def colisão(c1, c2):
    return c1 == c2

# Direções
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Inicialização
cobra = Cobra()
objeto = Objeto()
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 18)
placar = 0

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                cobra.direcao = UP
            elif event.key == K_DOWN:  # Corrigido para K_DOWN
                cobra.direcao = DOWN
            elif event.key == K_RIGHT:
                cobra.direcao = RIGHT
            elif event.key == K_LEFT:
                cobra.direcao = LEFT

    # Move a cobra
    cobra.mover()

    # Verifica se a cobra saiu da tela
    cabeça_x, cabeça_y = cobra.corpo[0]
    if cabeça_x < 0 or cabeça_x >= largura_tela or cabeça_y < 0 or cabeça_y >= altura_tela:
        # Game Over
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, (255,255,255) )
        text_rect = text.get_rect(center=(largura_tela//2, altura_tela//2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        quit()

    # Verifica colisão com o objeto
    if colisão(cobra.corpo[0], objeto.pos):
        cobra.cor = objeto.cor  # Muda a cor da cobra para a cor do objeto
        objeto.pos = on_grid_random()
        objeto.cor = random.choice(cores_objetos)  # Muda a cor do objeto
        cobra.corpo.append((0, 0))
        placar += 1

    # Desenho na tela
    screen.fill(preto)
    cobra.desenhar()
    objeto.desenhar()

    # Placar
    score_text = font.render("Score: " + str(placar), True, branco)
    screen.blit(score_text, [10, 10])


    pygame.display.update()
    clock.tick(10)
