import pygame
import sys
from tudinho import trocar_tela
import pygame.mixer

# Inicialização do Pygame
pygame.init()
pygame.mixer.init()

# Configurações da tela
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Meu Jogo")

# Cores e fontes
white = (255, 255, 255)
black = (0, 0, 0)
button_color = (41, 1, 6)  # Cor normal do botão
button_hover_color = (255, 128, 0)  # Cor de hover do botão
font = pygame.font.Font('fonte.otf', 32)  # Fonte e tamanho do texto

# Carregando imagem de fundo e som de clique
imagem_fundo = pygame.image.load("background.png")


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# Função para desenhar texto
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Função para verificar se o mouse está sobre um botão
def is_over_button(pos, rect):
    if rect.left <= pos[0] <= rect.right and rect.top <= pos[1] <= rect.bottom:
        return True
    return False


# Funções para as ações dos botões
def game():
    # Lógica do jogo
    pass


def options():
    # Configurações do jogo
    pass


def scores():
    # Exibir pontuações
    pass


def quit_game():
    pygame.quit()
    sys.exit()


# Loop principal do menu
running = True
while running:
    screen.blit(imagem_fundo, (0, 0))

    mx, my = pygame.mouse.get_pos()

    # Botões e seus estados (normal ou hover)
    buttons = [
        {"rect": pygame.Rect(170, 200, 250, 50), "text": "Jogar", "action": game, "state": "normal", "border_radius": 15},
        {"rect": pygame.Rect(170, 300, 250, 50), "text": "Opções", "action": options, "state": "normal", "border_radius": 15},
        {"rect": pygame.Rect(170, 400, 250, 50), "text": "Pontuações", "action": scores, "state": "normal", "border_radius": 15},
        {"rect": pygame.Rect(170, 500, 250, 50), "text": "Sair", "action": quit_game, "state": "normal", "border_radius": 15}
    ]

    for button in buttons:
        if is_over_button((mx, my), button["rect"]):
            button["state"] = "hover"
        else:
            button["state"] = "normal"

    # Desenhando os botões
    for button in buttons:
        pygame.draw.rect(screen, button_hover_color if button["state"] == "hover" else button_color, button["rect"], border_radius=button["border_radius"])
        draw_text(button["text"], font, white, screen, button["rect"].x + 20, button["rect"].y + 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button["state"] == "hover" and event.button == 1:
                    button["action"]()

    pygame.display.update()