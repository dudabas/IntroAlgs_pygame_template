from src.sprites import Meteoro

def test_meteoro_move_para_esquerda():
    meteoro = Meteoro()

    posicao_inicial = meteoro.rect.x

    meteoro.atualizar()

    assert meteoro.rect.x < posicao_inicial
