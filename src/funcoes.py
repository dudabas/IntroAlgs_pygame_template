import pygame

def desenhar_nave(tela, nave):
    pygame.draw.rect(tela, (0, 255, 0), nave.rect)

def desenhar_meteoro(tela, meteoro):
    pygame.draw.rect(tela, (255, 0, 0), meteoro.rect)

def colisao(nave, meteoros):
    for meteoro in meteoros:
        if nave.rect.colliderect(meteoro.rect):
            return True

    return False
