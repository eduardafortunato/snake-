import pygame , random 

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
largura_tela, altura_tela = 600, 400
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo da Cobrinha")

# Loop principal do jogo
rodando = True
while rodando:
    # Verifica eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Atualiza a tela
    pygame.display.flip()
# Inicializa a cobrinha
cobra = [(200, 200)]
tamanho_segmento = 10

# Loop principal do jogo
while rodando:
    # ... (código anterior)

    # Desenha a cobrinha
    for segmento in cobra:
        pygame.draw.rect(tela, (0, 255, 0), (segmento[0], segmento[1], tamanho_segmento, tamanho_segmento))
        # Direção inicial da cobra
direcao = 'direita'

# Loop principal do jogo
while rodando:
    # ... (código anterior)

    # Verifica as teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        direcao = 'esquerda'
    # ... (outros comandos para cima, baixo)

    # Atualiza a posição da cobra
    cabeca = cobra[-1]
    x, y = cabeca
    if direcao == 'direita':
        x += tamanho_segmento
    # ... (outros casos para outras direções)
    nova_cabeca = (x, y)
    cobra.append(nova_cabeca)
    # Remove o último segmento da cobra (opcional)
    # Inicializa a comida
comida = (300, 300)

# Loop principal do jogo
while rodando:
    # ... (código anterior)

    # Verifica se a cobra comeu a comida
    if cabeca == comida:
        # Gera nova comida
        comida = (random.randint(0, largura_tela//tamanho_segmento)*tamanho_segmento,
                  random.randint(0, altura_tela//tamanho_segmento)*tamanho_segmento)
        # Não remove o último segmento da cobra
        # Verifica se a cobra bateu nas paredes ou em si mesma
if cabeca[0] < 0 or cabeca[0] >= largura_tela or cabeca[1] < 0 or cabeca[1] >= altura_tela or cabeca in cobra[:-1]:
    rodando = False
    # Finaliza o Pygame
pygame.quit()