import pygame,sys
from pygame.locals import *
from animations import *
import main

try:
    import android
except ImportError:
    android=None

if android:
    android.init()
    android.map_key(android.KEYCODE_BACK,pygame.K_ESCAPE)

try:
    import pygame.mixer as mixer
except ImportError:
    import android.mixer as mixer

pygame.init()
pygame.display.set_caption("help")

fpsClock=pygame.time.Clock()
info_object=pygame.display.Info()
WINDOW_WIDTH=info_object.current_w
WINDOW_HEIGHT=info_object.current_h

infoimage=pygame.image.load("images/info1.png")
infoimage=pygame.transform.scale(infoimage,(WINDOW_WIDTH,WINDOW_HEIGHT))

DISPLAYSURF=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),FULLSCREEN)
DISPLAYSURF.blit(infoimage,(0,0))
def info_main():
    while True:
        set_bgs(DISPLAYSURF)
        DISPLAYSURF.blit(infoimage,(0,0))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYUP and event.key==K_ESCAPE or (event.type==MOUSEBUTTONDOWN):
                return
        pygame.display.update()
        fpsClock.tick()

if __name__=="__main__":
    info_main()

