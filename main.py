#-*-coding: cp1252 -*-

from constantes import *  # @UnusedWildImport
from pygame.locals import *  # @UnusedWildImport
from classes.jogo import Jogo

def main():
    jogo = Jogo(not DEBUG)
    jogo.loop()
    
if __name__ == '__main__':
    main()  