import pygame,sys
from animations import *
from pygame.locals import *
import my_help
import info
import blockit_drop_shadow
RED=(255,100,100)
BLUE=(150,150,255)
RED_BOUNDARY=(255,0,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE_BOUNDARY=(0,0,255)
GREEN=(0,255,0)
BUTTON_WIDTH=250
BUTTON_HEIGHT=150

try:
    import android
except ImportError:
    android = None
    
if android:
    android.init()
    android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)
    
try:
    import pygame.mixer as mixer
except ImportError:
    import android.mixer as mixer
    

pygame.init()
pygame.display.set_caption("main screen")
fpsClock=pygame.time.Clock()
infoObject=pygame.display.Info()
WINDOW_WIDTH=infoObject.current_w
WINDOW_HEIGHT=infoObject.current_h#820 for nexus 5
DISPLAYSURF=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),FULLSCREEN)

new_image_up=pygame.image.load("images/new_button_up.png")
#new_image_up=pygame.transform.scale(new_image_up,(BUTTON_WIDTH,BUTTON_HEIGHT))
new_image_down=pygame.image.load("images/new_button_down.png")
#new_image_down=pygame.transform.scale(new_image_down,(BUTTON_WIDTH,BUTTON_HEIGHT))
new_rect=new_image_up.get_rect()
new_rect.center=(WINDOW_WIDTH/2,WINDOW_HEIGHT-new_rect.height/2-60)

info_image_up=pygame.image.load("images/info_up.png")
#info_image_up=pygame.transform.scale(info_image_up,(2*BUTTON_HEIGHT/3,2*BUTTON_HEIGHT/3))
info_image_down=pygame.image.load("images/info_down.png")
#info_image_down=pygame.transform.scale(info_image_down,(2*BUTTON_HEIGHT/3,2*BUTTON_HEIGHT/3))
info_rect=info_image_up.get_rect()
info_rect.topleft=0+40,40
help_image_up=pygame.image.load("images/help_up.png")
#help_image_up=pygame.transform.scale(help_image_up,(2*BUTTON_HEIGHT/3,2*BUTTON_HEIGHT/3))
help_image_down=pygame.image.load("images/help_down.png")
#help_image_down=pygame.transform.scale(help_image_down,(2*BUTTON_HEIGHT/3,2*BUTTON_HEIGHT/3))
help_rect=help_image_up.get_rect()
help_rect.topright=WINDOW_WIDTH-40,40

bgimage=pygame.image.load("images/bg.png")
bgimage=pygame.transform.scale(bgimage,(WINDOW_WIDTH,WINDOW_HEIGHT))

DISPLAYSURF.blit(info_image_up,info_rect)
DISPLAYSURF.blit(bgimage,(0,0))
DISPLAYSURF.blit(new_image_up,new_rect)
DISPLAYSURF.blit(help_image_up,help_rect)

def if_first_game():
    try:
        read_high_score()
    except Exception:
        fout=open('score.txt','w')
        fout.write('0')
        fout.close()
        my_help.help_main()
def for_fade_out():
    DISPLAYSURF.blit(bgimage,(0,0))
    DISPLAYSURF.blit(info_image_up,info_rect)
    DISPLAYSURF.blit(help_image_up,help_rect)
    DISPLAYSURF.blit(new_image_up,new_rect)
    fade_out(DISPLAYSURF)
def the_main():
    for_fade_out()
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONDOWN:
                if new_rect.collidepoint(event.pos):
                    button_animation(DISPLAYSURF,new_image_down,new_image_up,new_rect)
                    fade_in(DISPLAYSURF)
                    if_first_game()
                    blockit_drop_shadow.game_main()
                elif info_rect.collidepoint(event.pos):
                    button_animation(DISPLAYSURF,info_image_down,info_image_up,info_rect)
                    fade_in(DISPLAYSURF)
                    info.info_main()
                    for_fade_out()
                elif help_rect.collidepoint(event.pos):
                    button_animation(DISPLAYSURF,help_image_down,help_image_up,help_rect)
                    fade_in(DISPLAYSURF)
                    my_help.help_main()
                    for_fade_out()
                    
        pygame.display.update()
        fpsClock.tick()

if __name__=="__main__":
    the_main()

