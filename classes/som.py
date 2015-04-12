#-*-coding: cp1252 -*-
import pygame.mixer

class Som(object):
    '''
    Classe com responsabilidades sobre música e efeitos sonoros.
    '''
    musica = pygame.mixer.music
    def __init__(self,sons,musicas,conf):
        '''
        Recebe uma lista de músicas e um dict de configuracoes. 
        '''
        self.sons = sons
        self.musicas = musicas
        self.conf = conf
    
    def playMusica(self,musica):
        if not self.conf['DEBUG']:
            Som.musica.load(self.musicas[musica])
            Som.musica.play(-1)
    
    def stopMusica(self):
        if not self.conf['DEBUG']:
            Som.musica.stop()