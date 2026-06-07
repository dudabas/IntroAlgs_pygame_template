import pygame
import random
from src.config import *

class Nave:
    def __init__(self):
        self.rect = pygame.Rect(
            50,
            ALTURA // 2,
            LARGURA_NAVE,
            ALTURA_NAVE
        )

    def mover(self, teclas):
        if teclas[pygame.K_UP]:
            self.rect.y -= VELOCIDADE_NAVE

        if teclas[pygame.K_DOWN]:
            self.rect.y += VELOCIDADE_NAVE

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > ALTURA:
            self.rect.bottom = ALTURA

class Meteoro:
    def __init__(self):
        self.rect = pygame.Rect(
            LARGURA,
            random.randint(0, ALTURA - ALTURA_METEORO),
            LARGURA_METEORO,
            ALTURA_METEORO
        )

    def atualizar(self):
        self.rect.x -= VELOCIDADE_METEORO
