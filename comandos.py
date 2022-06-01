import pygame
import sys

def controle(comandos, palheta1, palheta2):
    if comandos[pygame.K_UP] and palheta1.y - palheta1.vel >= 0:
        palheta1.y -= palheta1.vel
    if comandos[pygame.K_DOWN] and palheta1.y + palheta1.vel + palheta1.altura <= 300:
        palheta1.y += palheta1.vel

    if comandos[pygame.K_w] and palheta2.y - palheta2.vel >= 0:
        palheta2.y -= palheta1.vel
    if comandos[pygame.K_s] and palheta2.y + palheta2.vel + palheta2.altura <= 300:
        palheta2.y += palheta1.vel

    if comandos[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

def menu(comandos):
    # SAIR DO JOGO
    if comandos[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    