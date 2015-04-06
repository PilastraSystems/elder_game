#-*-coding: cp1252 -*-

import sys
from constantes import *  # @UnusedWildImport
from pygame.locals import *  # @UnusedWildImport
from classes.jogador import Jogador
from classes.tabuleiro import Tabuleiro

class Jogo(object):
    '''
    Classe Controladora do Jogo. Responsabilidades ainda não definidas.
    (Aqui entra um debate huehuehue).
    '''
    def __init__(self,modo):
        pygame.init()
        pygame.display.set_caption("Elders Game")
        self.tela = pygame.display.set_mode((800,600))
        self.tabuleiro = Tabuleiro(300,(200,200))
        self.tabuleiro.iniciarTabuleiro(self.tela)
        self.jogadores = [Jogador("recursos/imagens/img1.png"),Jogador("recursos/imagens/img2.png")]
        self.vez = JOGADOR1
        self.musica = pygame.mixer.music
        if not modo == DEBUG:
            self.musica.load("recursos/BGM/music.mp3")
            self.musica.play()
            
    def passarVez(self):
        self.vez = JOGADOR2 if self.vez == JOGADOR1 else JOGADOR1
        
    def getJogada(self,posicao):
        '''Desenha na tela a jogada e passa a vez para outro jogador.'''
        jogada = self.jogadores[self.vez].imagem
        posicao = self.tabuleiro.atualizarTabuleiro(posicao)
        if posicao:
            self.tela.blit(jogada,posicao)
            self.passarVez()
        
    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.musica.stop()
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.getJogada(event.pos)
            pygame.display.update()