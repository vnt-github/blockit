import pygame
from pygame.locals import *

try:
    import android
except ImportError:
    android = None

pygame.init()
if android:
    android.init()
    android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)
    
try:
    import pygame.mixer as mixer
except ImportError:
    import android.mixer as mixer
    
infoObject=pygame.display.Info()
WINDOW_WIDTH=infoObject.current_w
WINDOW_HEIGHT=infoObject.current_h
bgimage=pygame.image.load("images/bg1.png")
bgimage=pygame.transform.scale(bgimage,(WINDOW_WIDTH,WINDOW_HEIGHT))
fpsClock=pygame.time.Clock()
def button_animation(DISPLAYSURF,image_down,image_up,position):
    play_button_sound()
    static_surf=DISPLAYSURF.copy()
    DISPLAYSURF.blit(static_surf,(0,0))
    DISPLAYSURF.blit(image_down,position)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONUP:
                DISPLAYSURF.blit(image_up,position)
                pygame.display.update()
                
                return
    
def fade_in(DISPLAYSURF):
    real_surf=DISPLAYSURF.copy()
    fade_speed=20
    if android:
        fade_speed=50
    for a in range(0,255,fade_speed):
        static_surf=DISPLAYSURF.convert_alpha()
        DISPLAYSURF.blit(real_surf,(0,0))
        static_surf.fill((0,0,0,a))
        DISPLAYSURF.blit(static_surf,(0,0))
        pygame.display.update()
        fpsClock.tick(120)

def fade_out(DISPLAYSURF):
    real_surf=DISPLAYSURF.copy()
    fade_speed=20
    if android:
        fade_speed=50
    for a in range(0,255,fade_speed):
        static_surf=DISPLAYSURF.convert_alpha()
        DISPLAYSURF.blit(real_surf,(0,0))
        static_surf.fill((0,0,0,255-a))
        DISPLAYSURF.blit(static_surf,(0,0))
        pygame.display.update()
        fpsClock.tick(120)

def fade_in_out(DISPLAYSURF):
    real_surf=DISPLAYSURF.copy()
    fade_speed=20
    if android:
        fade_speed=50
    for a in range(0,255,fade_speed):
        static_surf=DISPLAYSURF.convert_alpha()
        DISPLAYSURF.blit(real_surf,(0,0))
        static_surf.fill((0,0,0,a))
        DISPLAYSURF.blit(static_surf,(0,0))
        pygame.display.update()
        fpsClock.tick(120)
    for a in range(0,255,fade_speed):
        static_surf=DISPLAYSURF.convert_alpha()
        DISPLAYSURF.blit(real_surf,(0,0))
        static_surf.fill((0,0,0,255-a))
        DISPLAYSURF.blit(static_surf,(0,0))
        pygame.display.update()
        fpsClock.tick(120)

def put_in(DISPLAYSURF,image,rect):
    real_surf=DISPLAYSURF.copy()
    put_in_speed=-5
    if android:
        put_in_speed=-20
    for size in range(200,0,put_in_speed):
        DISPLAYSURF.blit(real_surf,(0,0))
        new_image=pygame.transform.scale(image,(rect.width+size,rect.height+size))
        DISPLAYSURF.blit(new_image,rect)
        pygame.display.update()
        fpsClock.tick()
    DISPLAYSURF.blit(real_surf,(0,0))
    DISPLAYSURF.blit(image,rect)
    pygame.display.update()
    fpsClock.tick()
    
def half_fade_in(DISPLAYSURF):
    real_surf=DISPLAYSURF.copy()
    fade_speed=20
    if android:
        fade_speed=50
    for a in range(0,220,fade_speed):
        static_surf=DISPLAYSURF.convert_alpha()
        DISPLAYSURF.blit(real_surf,(0,0))
        static_surf.fill((0,0,0,a))
        DISPLAYSURF.blit(static_surf,(0,0))
        pygame.display.update()
        fpsClock.tick(120)
def shake(DISPLAYSURF):
    BORDER_COLOR=(0,0,0)
    shake_range=20
    no_of_shakes=1
    time_shake=20
    shake_surf=DISPLAYSURF.copy()
    for i in range(2):
        #DISPLAYSURF.fill(BORDER_COLOR)
        DISPLAYSURF.blit(shake_surf,(-shake_range,-shake_range))
        pygame.display.update()
        pygame.time.wait(time_shake)
        #DISPLAYSURF.fill(BORDER_COLOR)
        DISPLAYSURF.blit(shake_surf,(shake_range,-shake_range))
        pygame.display.update()
        pygame.time.wait(time_shake)
        #DISPLAYSURF.fill(BORDER_COLOR)
        DISPLAYSURF.blit(shake_surf,(shake_range,shake_range))
        pygame.display.update()
        pygame.time.wait(time_shake)
        #DISPLAYSURF.fill(BORDER_COLOR)
        DISPLAYSURF.blit(shake_surf,(-shake_range,shake_range))
        pygame.display.update()
        pygame.time.wait(time_shake)
        #DISPLAYSURF.fill(BORDER_COLOR)
        DISPLAYSURF.blit(shake_surf,(0,0))
        pygame.display.update()
#to delete if lakshay doesnt like the gradual colour bg idea
c=150
g=1
def gradual_bg(DISPLAYSURF):
    global c,g
    if c>204:
        g=-1
    elif c<50:
        g=1
    c+=g
    DISPLAYSURF.fill((c,(c+50),c))
#till here to be deleted

BLOCKSOUND=mixer.Sound("sounds/blocked.wav")
def play_block_sound():
    BLOCKSOUND.play()
PUTSOUND=mixer.Sound("sounds/put.wav")
def play_put_sound():
    PUTSOUND.play()
ENDSOUND=mixer.Sound("sounds/end.wav")
def play_end_sound():
    ENDSOUND.play()
BUTTONSOUND=mixer.Sound("sounds/button.wav")
def play_button_sound():
    BUTTONSOUND.play()
def read_high_score():
    fin=open('score.txt','r')
    for line in fin:
        print("score is :"+line)
    fin.close()
def write_high_score(score):
    fin=open('score.txt','r')
    for line in fin:
        if int(line)<score:
            fin.close()
            fout=open('score.txt','w')
            fout.write(str(score))
            fout.close()
            return
def set_bgs(DISPLAYSURF):
    DISPLAYSURF.blit(bgimage,(0,0))
    
shadow_color=(180,180,180)

def make_text(text,color,bgcolor,top,left,size=50):
    FONT_OBJECT=pygame.font.Font('fonts_and_extras/SourceSansPro-BlackIt.otf',size)
    if bgcolor!=None:
        text_surf=FONT_OBJECT.render(text,0,color,bgcolor)
    else:
        text_surf=FONT_OBJECT.render(text,0,color)#if no background color is provided then the background is transparent
    text_rect=text_surf.get_rect()
    text_rect.topleft=(top,left)
    
    img=pygame.Surface(text_rect.size,16)

    img.blit(bgimage,(0,0))

    text_surf.set_palette_at(1,shadow_color)
    img.blit(text_surf,(0,1))
        
    text_surf.set_palette_at(1,color)
    img.blit(text_surf,(0,0))

    
    
    return (img,text_rect)

