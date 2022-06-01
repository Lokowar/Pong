import pygame
from pygame.locals import *
import sys

import cores
import comandos
import render
import objetos
import engine

def menu(janela):
    menu = True

    # DIMENSÕES DO BOTÃO
    botãoX = 200
    botãoY = 150
    botãoL = 100
    botãoA = 20

    # INICIA BOTÃO
    botão = objetos.Botão(botãoX, botãoY, botãoL, botãoA)

    # INICIAR O FONTE DE TEXTO
    FONTE_TEXTO = pygame.font.SysFont("times new roman", 13)

    # LOOP DO MENU
    while menu == True:
        janela.fill(cores.PRETO)

        # FECHAR JANELA
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # INCIAR COMANDO
        Comandos = pygame.key.get_pressed()
        comandos.menu(Comandos)

        # FUNCIONAMENTO DO BOTÃO
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        botão = objetos.Botão(botãoX - botãoL // 2, botãoY - botãoA // 2, botãoL, botãoA)
        objetos.Botão.renderBotão(botão, janela)

        if botãoX - botãoL // 2 <= mouse[0] <= (botãoX - botãoL // 2)  + botãoL and botãoY - botãoA // 2 <= mouse[1] <= (botãoY - botãoA // 2) + botãoA:
            if click[0] == True:
                menu = False
                engine.jogo(janela)

        # TEXTO DO BOTÃO
        texto = FONTE_TEXTO.render("Iniciar jogo", 1, cores.PRETO)
        janela.blit(texto, (botãoX - 28 , botãoY - 8))

        # UPDATE
        pygame.display.update()

