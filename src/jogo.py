import pygame

from src.config import *
from src.sprites import Nave, Meteoro
from src.funcoes import *

def executar():

    pygame.init()

    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Meteor Escape")

    relogio = pygame.time.Clock()

    nave = Nave()
    meteoros = []

    contador = 0
    rodando = True

    while rodando:

        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        teclas = pygame.key.get_pressed()
        nave.mover(teclas)

        contador += 1

        if contador > 30:
            meteoros.append(Meteoro())
            contador = 0

        for meteoro in meteoros:
            meteoro.atualizar()

        meteoros = [
            m for m in meteoros
            if m.rect.right > 0
        ]

        if colisao(nave, meteoros):
            rodando = False

        tela.fill(COR_FUNDO)

        desenhar_nave(tela, nave)

        for meteoro in meteoros:
            desenhar_meteoro(tela, meteoro)

        pygame.display.flip()

    pygame.quit()
