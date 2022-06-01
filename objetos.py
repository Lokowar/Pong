import pygame
import typing

import cores

class Palheta():
    BRANCO = (255, 255, 255)

    def __init__(self, x: int, y: int, largura: int, altura: int, vel: int):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.vel = vel

    def renderPalheta(self, janela):
        pygame.draw.rect(janela, cores.BRANCO, (self.x, self.y, self.largura, self.altura))

class Bola():
    MAX_VEL = 5

    def __init__(self, x: int, y: int, raio: int):
       self.x = self.orginal_x = x
       self.y = self.original_y = y
       self.raio = raio
       self.x_vel = self.MAX_VEL
       self.y_vel = 0

    def renderBola(self, janela):
        pygame.draw.circle(janela, cores.BRANCO, (self.x, self.y), self.raio)

    def moverBola(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.orginal_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1

class Botão():
    def __init__(self, x: int, y: int, largura: int, altura: int):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    def renderBotão(self, janela):
        pygame.draw.rect(janela, cores.BRANCO, (self.x, self.y, self.largura, self.altura))