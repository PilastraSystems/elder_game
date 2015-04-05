import pygame.image

class Jogador(object):
    ''' Classe que representa um jogador. Possui nome, imagem e pontuacao.
        Faz jogadas e carrega a imagem(bolinha ou x).
    '''
    def __init__(self, path_imagem, nome="Jogador 1"):
        '''
        Constructor
        '''
        self.nome = nome
        self.imagem = self.setImagem(path_imagem)
        self.pontuacao = {"vitorias": 0, "empates": 0, "derrotas": 0}
    
    
    def setImagem(self,imagem):
        return pygame.image.load(imagem)
       
    def jogar(self):
        pass
        