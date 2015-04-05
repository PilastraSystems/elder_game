#-*-coding: cp1252 -*-

import pygame,sys
from pygame.locals import *  # @UnusedWildImport


def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((600,600))
    pygame.display.set_caption('Hello World!')
    
    WHITE = pygame.Color(255,255,255)
    RED = pygame.Color(255,0,0)
    GREEN = pygame.Color(0,255,0)
    BLUE  = pygame.Color(0,0,255)
    retangulo = pygame.Rect((180,100,40,40))
    
    # Textos
    fonte = pygame.font.Font('freesansbold.ttf',24)
    textoSurface  = fonte.render('Pontuação: ',True,BLUE)
    texto = textoSurface.get_rect()
    texto.center = (100,100)
    
    # Desenhos
    pygame.draw.line(DISPLAYSURF,RED,(200,0),(200,600), 4)
    pygame.draw.line(DISPLAYSURF,RED,(400,0),(400,600), 4)
    pygame.draw.line(DISPLAYSURF,RED,(0,200),(600,200), 4)
    pygame.draw.line(DISPLAYSURF,RED,(0,400),(600,400), 4)
    
    # Imagens
    imagem = pygame.image.load("recursos/imagens/django.png")
    imagem2 = pygame.image.load("recursos/imagens/windows.png")
    print dir(imagem)
    
    # Música
    pygame.mixer.music.load("recursos/BGM/music.mp3")
    pygame.mixer.music.play(1,0.0)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    retangulo.center = event.pos
                    DISPLAYSURF.blit(imagem,event.pos)
                elif event.button == 3:
                    DISPLAYSURF.blit(imagem2,event.pos)
            pygame.display.update()
    

if __name__ == '__main__':
    main()
    