import pygame, sys
from pygame.locals import *

import cores
import comandos
import objetos
import colisão
import render
import menu

# VARIAVEIS
ALTURA = 400
LARGURA = 300

FPS = 60

def jogo(janela):
    pygame.init()
    clock = pygame.time.Clock()

    global PONTO_PALHETA1
    global PONTO_PALHETA2

    PONTO_PALHETA1 = 0
    PONTO_PALHETA2 = 0

    # FONTE DO PLACAR
    FONTE_PLACAR = pygame.font.SysFont("times new roman", 30)

    # TITULO DA JANELA
    pygame.display.set_caption('Pong')

    ## INICIAR BOLA
    bola = objetos.Bola(ALTURA // 2, LARGURA // 2, 5) 

    ## INICIAR PALHETAS
    palheta1 = objetos.Palheta(ALTURA - 390, LARGURA // 2 - 50 // 2, 10, 50, 4)
    palheta2 = objetos.Palheta(ALTURA - 10, LARGURA // 2 - 50 // 2, 10, 50, 4)

    jogo = True

    while jogo == True:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        janela.fill(cores.PRETO)

        # MECANICAS
        objetos.Bola.moverBola(bola)
        colisão.checarColisao(bola, palheta1, palheta2)

        # CONTROLES
        Comandos = pygame.key.get_pressed()
        comandos.controle(Comandos, palheta1, palheta2)

        # RENDER
        render.renderJogo(janela)
        objetos.Bola.renderBola(bola, janela)
        objetos.Palheta.renderPalheta(palheta1, janela)
        objetos.Palheta.renderPalheta(palheta2, janela)

        # PONTUAÇÂO
        if bola.x < 0:
            bola.reset()
            PONTO_PALHETA2 += 1
    
        elif bola.x > ALTURA:
            bola.reset()
            PONTO_PALHETA1 += 1

        # CONDIÇÂO DE VITÒRIA
        venceu = False
        if PONTO_PALHETA1 == 5:
            venceu = True
            texto_vitoria = "Player 1 VENCEU"
            
        elif PONTO_PALHETA2 == 5:
            venceu = True
            texto_vitoria = "Player 2 VENCEU"

        # SE VENCER
        if venceu:
            texto = FONTE_PLACAR.render(texto_vitoria, 1, cores.BRANCO)
            janela.blit(texto, (LARGURA // 2 - 58, ALTURA // 2 - 100))
            pygame.display.update()
            pygame.time.delay(5000)
            jogo = False
            menu.menu(janela)

        pygame.display.update()