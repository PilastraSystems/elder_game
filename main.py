#-*-coding: cp1252 -*-

import pygame,sys
from pygame.locals import *  # @UnusedWildImport
from classes.jogo import Jogo


def main():
    jogo = Jogo()
    jogo.iniciarTabuleiro()
    jogo.loop()
    

if __name__ == '__main__':
    main()
    