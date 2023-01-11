import pygame
from pygame.locals import *
from random import randint

pygame.init()

LARGURA = 700
ALTURA = 600

x_cobra = LARGURA/2
y_cobra = ALTURA/2

x_maca = randint(40, 660)
y_maca = randint(50, 550)

# Velocidade
velocidade = 5
x_controle = velocidade
y_controle = 0

#Tela
screen = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption('Jogo da cobrinha')

#Delay
relogio = pygame.time.Clock()

#Músicas
colisao = pygame.mixer.Sound("smw_coin.wav")
musica_fundo = pygame.mixer.music.load('happy_adveture.mp3')
pygame.mixer.music.play(-1)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)
lista_cobra = []
comprimento_cobra = 5

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(screen, (0, 255, 0), (XeY[0], XeY[1], 25, 25))    

def reiniciar_jogo():
    global pontos, comprimento_cobra, x_cobra, y_cobra, x_maca, y_maca, lista_cobra, lista_cabeca, morreu
    pontos = 0
    comprimento_cobra = 5
    x_cobra = LARGURA/2
    y_cobra = ALTURA/2
    x_maca = randint(40, 660)
    y_maca = randint(50, 550)
    lista_cobra = []
    lista_cabeca = []
    pygame.mixer.music.play(-1)
    morreu = False

morreu = False

while True:
    screen.fill((0, 0, 102))
    relogio.tick(50)
    mensagem = f'Pontos {pontos}'
    texto = fonte.render(mensagem, True, (232, 76, 76))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        #Movimentação da cobra
        if event.type == KEYDOWN:
            if event.key == K_a and x_controle != velocidade:
                x_controle = - velocidade
                y_controle = 0
            if event.key == K_d and x_controle != - velocidade:
                x_controle =  velocidade
                y_controle = 0
            if event.key == K_w and y_controle != velocidade:
                x_controle = 0
                y_controle = - velocidade
            if event.key == K_s and y_controle != - velocidade:
                x_controle = 0
                y_controle = velocidade
        
    x_cobra += x_controle
    y_cobra += y_controle

    cobra = pygame.draw.rect(screen, (0, 255, 0), (x_cobra, y_cobra, 25, 25))
    maca = pygame.draw.circle(screen, (255, 0, 0), (x_maca, y_maca), 10)

    '''if pygame.key.get_pressed()[K_d]:
        x_cobra += 4
    if pygame.key.get_pressed()[K_a]:
        x_cobra -= 4
    if pygame.key.get_pressed()[K_w]:
        y_cobra -= 4
    if pygame.key.get_pressed()[K_s]:
        y_cobra += 4'''

    if cobra.colliderect(maca):
        x_maca = randint(40, 660)
        y_maca = randint(50, 550)
        colisao.play()
        pontos += 1
        comprimento_cobra += 2

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 70, bold=True, italic=False)
        mensagem2 = 'GAMER OVER'
        texto2 = fonte2.render(mensagem2, True, (249, 46, 132))

        fonte3 = pygame.font.SysFont('arial', 20, bold=True, italic=True)
        mensagem3 = 'Pressione R ou ESPAÇO para jogar novamente'
        texto3 = fonte3.render(mensagem3, True, (249, 46, 132))

        morreu = True
        while morreu:
            screen.fill((0, 0, 102))
            pygame.mixer.music.stop()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r or event.key == K_SPACE:
                        reiniciar_jogo()
            screen.blit(texto2, (LARGURA/7, ALTURA/3))
            screen.blit(texto3, (120, 300))
            pygame.display.update()

    if len(lista_cobra) > comprimento_cobra:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    if x_cobra > LARGURA:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = LARGURA
    if y_cobra > ALTURA:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = ALTURA

    screen.blit(texto, (40, 40))
    pygame.display.update()