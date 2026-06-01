# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Escreva aqui o nome provisório do jogo.

Exemplo:

> Corrida dos Obstáculos
> AstroRun

## 2. Integrantes do grupo

Liste os integrantes do grupo.
- Nome 1: Kennedy Pereira Mendes
- Nome 2: Maria Eduarda Barreto da Silva

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo:

> Nave desviando de meteoros.

## 4. Descrição geral do jogo


Descrição:

> O jogo consiste em uma nave espacial que se desloca em um cenário horizontal. Durante a partida, meteoritos surgem continuamente do lado direito da tela e se movem em direção ao lado esquerdo, criando obstáculos que o jogador deve evitar. A nave pode ser controlada pelo jogador para realizar os desvios necessários, tornando a jogabilidade dinâmica e progressivamente desafiadora.
## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

> O objetivo do jogador é permanecer em jogo pelo maior tempo possível sem colidir com os meteoritos. A pontuação é calculada com base no tempo de sobrevivência, de modo que quanto mais tempo a nave permanecer intacta, maior será a pontuação obtida. Quando ocorre uma colisão, a partida é encerrada e a pontuação final é comparada ao recorde armazenado. Caso a nova pontuação seja superior à anterior, ela passa a ser registrada como o novo recorde, incentivando o jogador a superar sua própria marca em partidas futuras.

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

- Regra 1: O jogador controla uma nave espacial utilizando teclado
- Regra 2: A nave pode se mover apenas para cima ou para baixo
- Regra 3: Meteoros aparecem do lado direito e se movem para o lado esquerdo
- Regra 4: Quanto maior o tempo de sobrevivência, maior a pontuação
- Regra 5: O jogo registra automaticamente o maior recorde alcançado pelo jogador
- Regra 6: O jogo termina quando a nave colide com um meteoro

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

> Toda vez que o jogador alcançar o próprio recorde.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

> A nave colidir com algum meteoro.

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Descrição:
> Uma nave controlada pelas setas do teclado.

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

> Meteoros saindo do lado direito da tela e indo em diração ao esquerdo.

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

> Tempo de sobrevivência que será convertido em pontuação.

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

> A cada segundo que o jogador se mantém vivo, ele ganhará 1 ponto no somatório da pontuação na partida.

## 10. Controles previstos


Controles do grupo:

- Seta para cima: mover a nave para cima
- Seta para baixo: mover a nave para baixo
- Enter: iniciar ou reiniciar o jogo
- ESC: sair do jogo

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

> - main.py: inicia o jogo e executa o loop principal;
- src/player.py: contém a classe e as funções relacionadas à nave do jogador;
- src/meteor.py: contém a criação e movimentação dos meteoros;
- src/game.py: controla as regras do jogo, pontuação e colisões;
- src/config.py: armazena configurações como tamanho da tela, cores e velocidades;
- src/record.py: realiza a leitura e gravação do recorde em arquivo;
- assets/: contém imagens, sons e demais recursos utilizados..


## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:


Caso não pretenda utilizar recursos externos, escreva:

> Não pretendemos utilizar recursos externos.
> - imagens gratuitas para a nave e os meteoros;
- fonte gratuita para exibição da pontuação e do recorde;
- tutoriais de Pygame utilizados apenas como referência para implementação;
- possíveis efeitos sonoros gratuitos para colisões e menu..

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1: implementação de detecção de colisão entre a nave e os meteoros;
- Dificuldade 2: armazenamento e atualização do recorde do jogador;

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

> A versão mínima do jogo terá uma nave controlada pelo teclado, movimentação vertical, meteoros atravessando a tela, sistema de pontuação baseado no tempo de sobrevivência, registro do maior recorde e tela de fim de jogo quando ocorrer uma colisão.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1: Tela inicial e menu de reinício
- Melhoria 2: Efeitos sonoros e música de fundo
- Melhoria 3: Diferentes tipos de meteoros com velocidade variadas
- Malhoria 4: aumento progressivo da dificuldade
