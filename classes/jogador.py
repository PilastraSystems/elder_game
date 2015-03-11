'''
Created on 10/03/2015

@author: Victor
'''



class Jogador(object):
    ''' Classe que representa um jogador. Possui nome, imagem e pontuacao.
        Faz jogadas e carrega a imagem(bolinha ou x).
    '''
    def __init__(self, time, nome="Jogador 1"):
        '''
        Constructor
        '''
        self.nome = nome
        self.imagem = self.setImagem(time)
        self.pontuacao = 0
    
    
    def setImagem(self,time):
        pass
    
    
    def jogar(self):
        pass
        