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

help0=pygame.image.load("images/help0.png");
help0=pygame.transform.scale(help0,(WINDOW_WIDTH,WINDOW_HEIGHT));
help1=pygame.image.load("images/help1.png");
help1=pygame.transform.scale(help1,(WINDOW_WIDTH,WINDOW_HEIGHT))
help2=pygame.image.load("images/help2.png");
help2=pygame.transform.scale(help2,(WINDOW_WIDTH,WINDOW_HEIGHT))
help3=pygame.image.load("images/help3.png");
help3=pygame.transform.scale(help3,(WINDOW_WIDTH,WINDOW_HEIGHT))
help4=pygame.image.load("images/help4.png");
help4=pygame.transform.scale(help4,(WINDOW_WIDTH,WINDOW_HEIGHT))
help5=pygame.image.load("images/help5.png");
help5=pygame.transform.scale(help5,(WINDOW_WIDTH,WINDOW_HEIGHT))
help6=pygame.image.load("images/help6.png");
help6=pygame.transform.scale(help6,(WINDOW_WIDTH,WINDOW_HEIGHT))
help_images=(help0,help1,help2,help3,help4,help5,help6)

BLACK=(70,70,70)

DISPLAYSURF=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),FULLSCREEN)

def help_main():
    global help_images
    i=0
    while True:
        try:
            help_image=help_images[i]
            set_bgs(DISPLAYSURF)
            DISPLAYSURF.blit(help_image,(0,0))
        except Exception as error:
            print str(error)
            return
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYUP and event.key==K_ESCAPE:
                return
            elif event.type==MOUSEBUTTONDOWN:
                x,y=event.pos
                if x>WINDOW_WIDTH/2:
                    i+=1
                else:
                    i-=1
                if i<0:
                    return
        pygame.display.update()
        fpsClock.tick()

if __name__=="__main__":
    help_main()
