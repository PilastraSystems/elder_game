#-*-coding: cp1252 -*-


from constantes import *  # @UnusedWildImport

class Tabuleiro(object):
    '''
    Classe que representa o tabuleiro do jogo da velha. Possui casas.
    Atualiza o estado das suas casas.
    '''
    def __init__(self,tamanho,origem):
        '''
        Constructor
        '''
        self.tamanho = tamanho
        self.tamanhoCasa = self.tamanho/3
        self.origem = origem
        self.casas = [[0] * 3] * 3
            
    def iniciarTabuleiro(self,tela):
        o_x, o_y = self.origem # Origem do novo sistema cartesiano
        for i in range(4):
            x_a = o_x+(i*self.tamanhoCasa)
            y_a = o_y
            y_b = o_y+self.tamanho
            pygame.draw.line(tela,RED,(x_a,y_a),(x_a,y_b),4)
        for i in range(4):
            x_a = o_x
            x_b = o_x+self.tamanho
            y_a = o_y+(i*self.tamanhoCasa)
            pygame.draw.line(tela,RED,(x_a,y_a),(x_b,y_a),4)
    
    def atualizarTabuleiro(self,coordenada):
        casa = self.coordToCasa(coordenada)
        if casa:
            self.casas[casa[0]][casa[1]] = 1
            # Soma um pequeno offset para a imagem não bater nas bordas do tabuleiro.
            coords = self.casaToCoord(casa)
            x = coords[0]+self.tamanhoCasa/5
            y = coords[1]+self.tamanhoCasa/5
            return (x,y)
        return None
        
    
    def coordToCasa(self,coordenada):
        '''Converte uma coordenada para uma casa.'''
        x,y = coordenada
        
        for casa_x in range(3):
            for casa_y in range(3):
                o_x, o_y = self.casaToCoord((casa_x,casa_y))
                quadrado = pygame.Rect(o_x,o_y,self.tamanhoCasa,self.tamanhoCasa)
                if quadrado.collidepoint(x,y):
                    return (casa_x,casa_y)
        return None
    
    def casaToCoord(self,casa):
        x = self.origem[0]+casa[0]*self.tamanhoCasa
        y = self.origem[1]+casa[1]*self.tamanhoCasa
        return (x,y)
        

        