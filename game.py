import pygame
# importando todas funções e constantes do submódulo locals
from pygame.locals import *
# função pra fechar a janela
from sys import exit
from random import randint

# inicializando funções e variáveis do pygame
pygame.init()

LARGURA = 640
ALTURA = 480

# posição inicial da cobrinha
x_cobrinha = int(LARGURA/2) - 25
y_cobrinha = int(ALTURA/2) - 25

# posição inicial da maçã
x_maca = randint(40, 600)
y_maca = randint(50, 430)

# controlando movimentação da cobrinha
velocidade = 5

# enquanto um eixo tem velocida o outro deve está zerado pra impedir movimento na horizontal
x_controle = velocidade
y_controle = 0

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")

# relogio para controle de frame
relogio = pygame.time.Clock()

# fonte
fonte = pygame.font.SysFont('arial', 30, bold=True, italic=True)
pontuacao = 0

#musicas 
musica_fundo = pygame.mixer.music.load('music\happy_adveture.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

som_colisao = pygame.mixer.Sound('music\smw_coin.wav')
som_colisao.set_volume(0.6)


# armazena os lista com posições assumidas pela cobrinha
lista_cobra = []
# qtd máxima de listas dentro de lista_cobra
comprimento_inicial = 5

# funções
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 25, 25))

morreu = False
def reiniciar_jogo():
    global pontuacao, comprimento_inicial, x_cobrinha, y_cobrinha, x_maca, y_maca, lista_cabeca, lista_cobra, morreu
    pontuacao = 0
    comprimento_inicial = 5
    x_cobrinha = int(LARGURA/2) - 25
    y_cobrinha = int(ALTURA/2) - 25
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    lista_cabeca = []
    lista_cobra = []
    morreu = False

# loop principal
while True:
    # frames por segundo
    relogio.tick(60)

    tela.fill((0, 0, 0))

    mensagem = f'Pontos: {pontuacao}'
    texto_formatado = fonte.render(mensagem, True, (232, 255, 255))


    # checar evento a cada iteração do loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle -= velocidade
            if event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle += velocidade
            if event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle -= velocidade
                    y_controle = 0
            if event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle += velocidade
                    y_controle = 0

    # fazendo a cobra não parar de andar
    x_cobrinha += x_controle
    y_cobrinha += y_controle

    #desenhando na tela
    cobrinha = pygame.draw.rect(tela, (0, 255, 0), (x_cobrinha, y_cobrinha, 25, 25))
    maca = pygame.draw.circle(tela, (255, 0, 0), (x_maca, y_maca), 10)

    # caso ultrapasse a tela
    if x_cobrinha > LARGURA:
        x_cobrinha = 0
    if x_cobrinha < 0:
        x_cobrinha = LARGURA
    if y_cobrinha > ALTURA:
        y_cobrinha = 0
    if y_cobrinha < 0:
        y_cobrinha = ALTURA

    # colisão
    if cobrinha.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)        

        pontuacao += 1

        som_colisao.play()

        comprimento_inicial += 1

    # armazenando valores de x e y da cobrinha
    # armazena valor atual de x e y
    lista_cabeca = []
    lista_cabeca.append(x_cobrinha)
    lista_cabeca.append(y_cobrinha)

    # armazena todos os valores x e y 
    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0] 

    aumenta_cobra(lista_cobra)

    # game over
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 45, bold=True, italic=True)
        fonte3 = pygame.font.SysFont('arial', 20, bold=True, italic=True)
        mensagem2 = 'Game Over'
        mensagem3 = 'Pressione a tecla R ou ESPAÇO para reiniciar'
        texto_formatado2 = fonte2.render(mensagem2, True, (255, 255, 255))
        texto_formatado3 = fonte3.render(mensagem3, True, (255, 255, 255))
        ret_texto = texto_formatado2.get_rect()

        morreu = True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE or event.key == K_r:
                        reiniciar_jogo()
            tela.blit(texto_formatado2, ((LARGURA//2) - 150, 150))
            tela.blit(texto_formatado3, (LARGURA//2 - 220, ALTURA//2))
            pygame.display.update()

    # escrevendo mensagem na tela
    tela.blit(texto_formatado, (30, 20))

    # atualizar tela a cada iteração do loop
    pygame.display.update()
 