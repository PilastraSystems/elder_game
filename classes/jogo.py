#-*-coding: cp1252 -*-

import pygame.draw
import sys
from constantes import *  # @UnusedWildImport
from pygame.locals import *  # @UnusedWildImport
from classes.jogador import Jogador

class Jogo(object):
    '''
    Classe Controladora do Jogo. Responsabilidades ainda não definidas.
    (Aqui entra um debate huehuehue).
    '''
    def __init__(self):
        pygame.init()
        self.tabuleiro = pygame.display.set_mode((600,600))
        self.vez = JOGADOR1
        self.jogadores = [Jogador("recursos/imagens/img1.png"),Jogador("recursos/imagens/img2.png")]
        self.musica = pygame.mixer.music
        self.musica.load("recursos/BGM/music.mp3")
    
    def iniciarTabuleiro(self):
        '''Inicia o tabuleiro. 
        TODO: Ler preferências de um arquivo.
        TODO: Sistema de conversão entre coordenadas cartesianas e as casas do tabuleiro
        '''
        pygame.draw.line(self.tabuleiro,RED,(200,0),(200,600), 4)
        pygame.draw.line(self.tabuleiro,RED,(400,0),(400,600), 4)
        pygame.draw.line(self.tabuleiro,RED,(0,200),(600,200), 4)
        pygame.draw.line(self.tabuleiro,RED,(0,400),(600,400), 4)
        self.musica.play()
    
    def getJogada(self,vez,posicao):
        '''Desenha na tela a jogada e passa a vez para outro jogador.'''
        jogada = self.jogadores[vez].imagem
        self.tabuleiro.blit(jogada,posicao)
        self.vez = JOGADOR2 if self.vez == JOGADOR1 else JOGADOR1
    
    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.musica.stop()
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.getJogada(self.vez,event.pos)
            pygame.display.update()