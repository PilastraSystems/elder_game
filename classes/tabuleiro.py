'''
Created on 10/03/2015

@author: Victor
'''

class Tabuleiro(object):
    '''
    Classe que representa o tabuleiro do jogo da velha. Possui uma imagem e casas.
    Atualiza o estado das suas casas
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
        self.casas = {} #Pensei num dicionário pra fazer a matriz das casas. Idéias?
        self.imagem = self.setImagem()
        
    def setImagem(self):
        pass
    
    def atualizarCasas(self,posicao):
        pass
        