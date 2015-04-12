#-*-coding: cp1252 -*-

import sys
from constantes import *  # @UnusedWildImport
from pygame.locals import *  # @UnusedWildImport
from classes.jogador import Jogador
from classes.tabuleiro import Tabuleiro
from time import sleep
from classes.som import Som
import re

class Jogo(object):
    '''
    Classe Controladora do Jogo. Responsabilidades ainda não definidas.
    (Aqui entra um debate huehuehue).
    '''
    def __init__(self,modo):
        pygame.init()
        pygame.display.set_caption("Elders Game")
        self.configuracoes = self.carregarConfiguracoes(modo)
        self.tela = pygame.display.set_mode((self.configuracoes['WIDTH'],self.configuracoes['HEIGHT']))
        self.tabuleiro = Tabuleiro(300,(240,190))
        self.jogadores = [Jogador("recursos/imagens/img1.png"),Jogador("recursos/imagens/img2.png")]
        self.vez = JOGADOR1
        self.musica = Som(None,{'main': "recursos/BGM/music.ogg"},self.configuracoes)
        
    def carregarConfiguracoes(self,debug):
        arquivo = open(CONF_PATH,"r")
        configuracoes = {}
        for conf in arquivo.readlines():
            temp = re.split("\s",conf)
            try:
                configuracoes[temp[0]] = int(temp[1])
            except ValueError:
                configuracoes[temp[0]] = temp[1]
        arquivo.close()
        configuracoes['DEBUG'] = debug
        return configuracoes
            
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
                    self.musica.stopMusica()
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.getJogada(event.pos)
            pygame.display.update()
    
    def opening(self):
        fonte = pygame.font.Font('freesansbold.ttf',80)
        elderSurface = fonte.render('Elder',True,BLUE)
        fonte = pygame.font.Font('freesansbold.ttf',80)
        gameSurface = fonte.render('Game',True,BLUE)
        self.tela.blit(elderSurface,(240,100))
        pygame.display.update()
        sleep(1)
        self.tela.fill(BLACK)
        self.tela.blit(gameSurface,(240,450))
        pygame.display.update()
        sleep(3/2.)
        self.tela.fill(BLACK)
        pygame.display.update()
        sleep(1)
        self.tabuleiro.iniciarTabuleiro(self.tela)
        self.musica.playMusica('main')