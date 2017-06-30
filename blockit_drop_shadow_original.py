#this is optimised version
import pygame,sys,random
from animations import *
from pygame import *

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

mixer.music.load("sounds/bg.wav")

infoObject=pygame.display.Info()
WINDOW_WIDTH=infoObject.current_w
WINDOW_HEIGHT=infoObject.current_h#820 for nexus 5
PLAYER1="BLACK"
PLAYER2="WHITE"
WHITE=(255,255,255)
BLACK=(70,70,70)
GREEN=(0,255,0)
RED=(100,0,0)
BACKGROUND=(150,150,150)
BUTTON_WIDTH=250
BUTTON_HEIGHT=150
DISPLAYSURF=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption("BLOCK IT!!")

new_image_up=pygame.image.load("images/new_button_up.png")
new_image_up=pygame.transform.scale(new_image_up,(BUTTON_WIDTH,BUTTON_HEIGHT))
new_image_down=pygame.image.load("images/new_button_down.png")
new_image_down=pygame.transform.scale(new_image_down,(BUTTON_WIDTH,BUTTON_HEIGHT))
new_rect=new_image_up.get_rect()
new_rect.bottomright=WINDOW_WIDTH-20,WINDOW_HEIGHT-20

undo_image_up=pygame.image.load("images/undo_button_up.png")
undo_image_up=pygame.transform.scale(undo_image_up,(BUTTON_WIDTH,BUTTON_HEIGHT))
undo_image_down=pygame.image.load("images/undo_button_down.png")
undo_image_down=pygame.transform.scale(undo_image_down,(BUTTON_WIDTH,BUTTON_HEIGHT))
undo_rect=undo_image_up.get_rect()
undo_rect.bottomleft=20,WINDOW_HEIGHT-20

turn_image=pygame.image.load("images/turn.png")
turn_image=pygame.transform.scale(turn_image,(2*BUTTON_WIDTH/5,BUTTON_WIDTH/2))
turn_rect=turn_image.get_rect()
turn_rect.top=10


previous_first_time=None

OVER_RIDE_SURF,OVER_RIDE_RECT=make_text("OVERRIDE",RED,None,0,0,24)

undo=False

def loop():
    fade_out(DISPLAYSURF)
    while True:
        global r_c
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONDOWN :
                if TWO_RECT.collidepoint(event.pos):
                    button_animation(DISPLAYSURF,TWO_IMAGE_DOWN,TWO_IMAGE,TWO_RECT)
                    fade_in(DISPLAYSURF)
                    r_c=2
                    return
                elif FOUR_RECT.collidepoint(event.pos):
                    button_animation(DISPLAYSURF,FOUR_IMAGE_DOWN,FOUR_IMAGE,FOUR_RECT)
                    fade_in(DISPLAYSURF)
                    r_c=4
                    return
                elif SIX_RECT.collidepoint(event.pos):
                    button_animation(DISPLAYSURF,SIX_IMAGE_DOWN,SIX_IMAGE,SIX_RECT)
                    fade_in(DISPLAYSURF)
                    r_c=6
                    return
                elif EIGHT_RECT.collidepoint(event.pos):
                    button_animation(DISPLAYSURF,EIGHT_IMAGE_DOWN,EIGHT_IMAGE,EIGHT_RECT)
                    fade_in(DISPLAYSURF)
                    r_c=8
                    return    
def display_start():
    global r_c,BLOCK_SIZE,BLOCK_WIDTH,BOARD_X_PLACE,BOARD_Y_PLACE,\
           TWO_RECT,FOUR_RECT,SIX_RECT,EIGHT_RECT,\
           TWO_IMAGE,FOUR_IMAGE,SIX_IMAGE,EIGHT_IMAGE,\
           TWO_IMAGE_DOWN,FOUR_IMAGE_DOWN,SIX_IMAGE_DOWN,EIGHT_IMAGE_DOWN,\
           player2_,player1_,player1__rect,player2__rect,\
           player2_0,player2_1,player2_2,player2_3,\
           player1_0,player1_1,player1_2,player1_3,\
           player2_0_rect,player2_1_rect,player2_2_rect,player2_3_rect,\
           player1_0_rect,player1_1_rect,player1_2_rect,player1_3_rect
    TWO_IMAGE=pygame.image.load("images/two_button_up.png")
    TWO_IMAGE=pygame.transform.scale(TWO_IMAGE,(BUTTON_WIDTH,BUTTON_HEIGHT))
    TWO_IMAGE_DOWN=pygame.image.load("images/two_button_down.png")
    TWO_IMAGE_DOWN=pygame.transform.scale(TWO_IMAGE_DOWN,(BUTTON_WIDTH,BUTTON_HEIGHT))
    TWO_RECT=TWO_IMAGE.get_rect(left=WINDOW_WIDTH/2,top=WINDOW_HEIGHT/2)
    TWO_RECT.top-=2.1*TWO_RECT.height
    TWO_RECT.left-=TWO_RECT.width/2
    FOUR_IMAGE=pygame.image.load("images/four_button_up.png")
    FOUR_IMAGE=pygame.transform.scale(FOUR_IMAGE,(BUTTON_WIDTH,BUTTON_HEIGHT))
    FOUR_IMAGE_DOWN=pygame.image.load("images/four_button_down.png")
    FOUR_IMAGE_DOWN=pygame.transform.scale(FOUR_IMAGE_DOWN,(BUTTON_WIDTH,BUTTON_HEIGHT))
    FOUR_RECT=FOUR_IMAGE.get_rect(left=TWO_RECT.left,top=TWO_RECT.top+TWO_RECT.height+20)
    SIX_IMAGE=pygame.image.load("images/six_button_up.png")
    SIX_IMAGE=pygame.transform.scale(SIX_IMAGE,(BUTTON_WIDTH,BUTTON_HEIGHT))
    SIX_IMAGE_DOWN=pygame.image.load("images/six_button_down.png")
    SIX_IMAGE_DOWN=pygame.transform.scale(SIX_IMAGE_DOWN,(BUTTON_WIDTH,BUTTON_HEIGHT))
    SIX_RECT=FOUR_IMAGE.get_rect(left=TWO_RECT.left,top=FOUR_RECT.top+FOUR_RECT.height+20)
    EIGHT_IMAGE=pygame.image.load("images/eight_button_up.png")
    EIGHT_IMAGE=pygame.transform.scale(EIGHT_IMAGE,(BUTTON_WIDTH,BUTTON_HEIGHT))
    EIGHT_IMAGE_DOWN=pygame.image.load("images/eight_button_down.png")
    EIGHT_IMAGE_DOWN=pygame.transform.scale(EIGHT_IMAGE_DOWN,(BUTTON_WIDTH,BUTTON_HEIGHT))
    EIGHT_RECT=FOUR_IMAGE.get_rect(left=TWO_RECT.left,top=SIX_RECT.top+SIX_RECT.height+20)
    DISPLAYSURF.fill(BACKGROUND)
    set_bgs(DISPLAYSURF) 
    DISPLAYSURF.blit(TWO_IMAGE,TWO_RECT)
    DISPLAYSURF.blit(FOUR_IMAGE,FOUR_RECT)
    DISPLAYSURF.blit(SIX_IMAGE,SIX_RECT)
    DISPLAYSURF.blit(EIGHT_IMAGE,EIGHT_RECT)
    loop()
    BLOCK_SIZE=WINDOW_HEIGHT/r_c
    BLOCK_WIDTH=BLOCK_SIZE/20
    if (BLOCK_SIZE-BLOCK_WIDTH)%4!=0:
        BLOCK_SIZE=BLOCK_SIZE-((BLOCK_SIZE-BLOCK_WIDTH)%4)
    #BLOCK_SIZE-BLOCK_WIDTH should be divisible by 4 dont know why
    BOARD_X_PLACE=WINDOW_WIDTH-(r_c*BLOCK_SIZE)-(WINDOW_WIDTH-r_c*BLOCK_SIZE)/2
    BOARD_Y_PLACE=WINDOW_HEIGHT-(r_c*BLOCK_SIZE)-(WINDOW_HEIGHT-r_c*BLOCK_SIZE)/2+8
    #
    player2_0=pygame.image.load("images/player2_0.png")
    player2_0=pygame.transform.scale(player2_0,(BLOCK_SIZE-5*BLOCK_WIDTH,BLOCK_SIZE/2-5*BLOCK_WIDTH/2))
    player2_0_rect=player2_0.get_rect()
    player2_1=pygame.image.load("images/player2_1.png")
    player2_1=pygame.transform.scale(player2_1,(BLOCK_SIZE/2-5*BLOCK_WIDTH/2,BLOCK_SIZE-5*BLOCK_WIDTH))
    player2_1_rect=player2_1.get_rect()
    player2_2=pygame.image.load("images/player2_2.png")
    player2_2=pygame.transform.scale(player2_2,(BLOCK_SIZE-5*BLOCK_WIDTH,BLOCK_SIZE/2-5*BLOCK_WIDTH/2))
    player2_2_rect=player2_2.get_rect()
    player2_3=pygame.image.load("images/player2_3.png")
    player2_3=pygame.transform.scale(player2_3,(BLOCK_SIZE/2-5*BLOCK_WIDTH/2,BLOCK_SIZE-5*BLOCK_WIDTH))
    player2_3_rect=player2_3.get_rect()
    
    player1_0=pygame.image.load("images/player1_0.png")
    player1_0=pygame.transform.scale(player1_0,(BLOCK_SIZE-5*BLOCK_WIDTH,BLOCK_SIZE/2-5*BLOCK_WIDTH/2))
    player1_0_rect=player1_0.get_rect()
    player1_1=pygame.image.load("images/player1_1.png")
    player1_1=pygame.transform.scale(player1_1,(BLOCK_SIZE/2-5*BLOCK_WIDTH/2,BLOCK_SIZE-5*BLOCK_WIDTH))
    player1_1_rect=player1_1.get_rect()
    player1_2=pygame.image.load("images/player1_2.png")
    player1_2=pygame.transform.scale(player1_2,(BLOCK_SIZE-5*BLOCK_WIDTH,BLOCK_SIZE/2-5*BLOCK_WIDTH/2))
    player1_2_rect=player1_2.get_rect()
    player1_3=pygame.image.load("images/player1_3.png")
    player1_3=pygame.transform.scale(player1_3,(BLOCK_SIZE/2-5*BLOCK_WIDTH/2,BLOCK_SIZE-5*BLOCK_WIDTH))
    player1_3_rect=player1_3.get_rect()
    
    player2_=pygame.image.load("images/player2_.png");
    player2_=pygame.transform.scale(player2_,(BLOCK_SIZE,BLOCK_SIZE));
    player2__rect=player2_.get_rect();

    player1_=pygame.image.load("images/player1_.png");
    player1_=pygame.transform.scale(player1_,(BLOCK_SIZE,BLOCK_SIZE));
    player1__rect=player1_.get_rect();
    
    #
class triangle():
    def __init__(self,pts,player):
        self.pts=pts
        self.player=player
    def collide(self,points):
        poly=self.pts
        area=abs((poly[0][0]*(poly[1][1]-poly[2][1])+poly[1][0]*(poly[2][1]-poly[0][1])+poly[2][0]*(poly[0][1]-poly[1][1]))/2)
        area1=abs((points[0]*(poly[1][1]-poly[2][1])+poly[1][0]*(poly[2][1]-points[1])+poly[2][0]*(points[1]-poly[1][1]))/2)
        area2=abs((poly[0][0]*(points[1]-poly[2][1])+points[0]*(poly[2][1]-poly[0][1])+poly[2][0]*(poly[0][1]-points[1]))/2)
        area3=abs((poly[0][0]*(poly[1][1]-points[1])+poly[1][0]*(points[1]-poly[0][1])+points[0]*(poly[0][1]-poly[1][1]))/2)
        if area==area1+area2+area3:
            return True
        else:
            return False
class Block(object):
    def __init__(self,marked=False,rect=pygame.Rect(0,0,0,0)):
        self.marked=marked
        self.rect=rect
        self.triangles=(triangle((self.rect.topleft,self.rect.topright,self.rect.center),None)\
                        ,triangle((self.rect.topleft,self.rect.bottomleft,self.rect.center),None)\
                        ,triangle((self.rect.bottomleft,self.rect.bottomright,self.rect.center),None)\
                        ,triangle((self.rect.bottomright,self.rect.topright,self.rect.center),None))


def draw_board(FIRST_PLAYER):
    global winner,player1_score,player2_score
    DISPLAYSURF.fill(BACKGROUND)
    set_bgs(DISPLAYSURF)
    player1_score=0
    player2_score=0
    for i in range(0,r_c): 
        for j in range(0,r_c):
            block=list_of_objects[i][j]
            if number_list[i*r_c+j]%2==0:
                player1__rect.center=block.rect.center
                DISPLAYSURF.blit(player1_,player1__rect)
            else:
                player2__rect.center=block.rect.center
                DISPLAYSURF.blit(player2_,player2__rect)
            for k in range(4): 
                if block.triangles[k].player==PLAYER2:
                    player2_score+=1
                    #
                    if k==0:
                        player2_0_rect.center=(block.triangles[0].pts[0][0]+BLOCK_SIZE/2-BLOCK_WIDTH/2,block.triangles[0].pts[0][1]+BLOCK_SIZE/4+BLOCK_WIDTH/4)
                        DISPLAYSURF.blit(player2_0,player2_0_rect)
                    elif k==1:
                        player2_1_rect.center=(block.triangles[1].pts[0][0]+BLOCK_SIZE/4+BLOCK_WIDTH/4,block.triangles[1].pts[0][1]+BLOCK_SIZE/2-BLOCK_WIDTH/2)
                        DISPLAYSURF.blit(player2_1,player2_1_rect)
                    elif k==2:
                        player2_2_rect.center=(block.triangles[2].pts[0][0]+BLOCK_SIZE/2-BLOCK_WIDTH/2,block.triangles[2].pts[0][1]-BLOCK_SIZE/4-BLOCK_WIDTH/4)
                        DISPLAYSURF.blit(player2_2,player2_2_rect)
                    else:
                        player2_3_rect.center=(block.triangles[3].pts[0][0]-BLOCK_SIZE/4-BLOCK_WIDTH/4,block.triangles[3].pts[0][1]-BLOCK_SIZE/2+BLOCK_WIDTH/2)
                        DISPLAYSURF.blit(player2_3,player2_3_rect)
                    #
                elif block.triangles[k].player==PLAYER1:
                    player1_score+=1
                    #
                    if k==0:
                        player1_0_rect.center=(block.triangles[0].pts[0][0]+BLOCK_SIZE/2-BLOCK_WIDTH/2,block.triangles[0].pts[0][1]+BLOCK_SIZE/4+BLOCK_WIDTH/4)
                        DISPLAYSURF.blit(player1_0,player1_0_rect)
                    elif k==1:
                        player1_1_rect.center=(block.triangles[1].pts[0][0]+BLOCK_SIZE/4+BLOCK_WIDTH/4,block.triangles[1].pts[0][1]+BLOCK_SIZE/2-BLOCK_WIDTH/2)
                        DISPLAYSURF.blit(player1_1,player1_1_rect)
                    elif k==2:
                        player1_2_rect.center=(block.triangles[2].pts[0][0]+BLOCK_SIZE/2-BLOCK_WIDTH/2,block.triangles[2].pts[0][1]-BLOCK_SIZE/4-BLOCK_WIDTH/4)
                        DISPLAYSURF.blit(player1_2,player1_2_rect)
                    else:
                        player1_3_rect.center=(block.triangles[3].pts[0][0]-BLOCK_SIZE/4-BLOCK_WIDTH/4,block.triangles[3].pts[0][1]-BLOCK_SIZE/2+BLOCK_WIDTH/2)
                        DISPLAYSURF.blit(player1_3,player1_3_rect)
                    #
    winner=None
    if player1_score>player2_score:
        winner=PLAYER1
    elif player2_score>player1_score:
        winner=PLAYER2
    player1_bgcolor=BLACK
    player2_bgcolor=BLACK
    
    PLAYER2_SURF,PLAYER2_RECT=make_text(PLAYER2,player2_bgcolor,None,0,0,40)
    PLAYER2_RECT.top=4*r_c*BLOCK_WIDTH
    PLAYER2_RECT.left=BOARD_X_PLACE+r_c*(BLOCK_SIZE)+2*r_c*BLOCK_WIDTH

    PLAYER2_SCORE_SURF,PLAYER2_SCORE_RECT=make_text(str(player2_score),BLACK,None,0,0,120)
    PLAYER2_SCORE_RECT.top=PLAYER2_RECT.bottom+PLAYER2_RECT.height*3
    PLAYER2_SCORE_RECT.centerx=PLAYER2_RECT.centerx
    
    PLAYER1_SURF,PLAYER1_RECT=make_text(PLAYER1,player1_bgcolor,None,0,0,40)
    PLAYER1_RECT.top=4*r_c*BLOCK_WIDTH
    PLAYER1_RECT.right=BOARD_X_PLACE-BLOCK_WIDTH-2*r_c*BLOCK_WIDTH

    PLAYER1_SCORE_SURF,PLAYER1_SCORE_RECT=make_text(str(player1_score),BLACK,None,0,0,120)
    PLAYER1_SCORE_RECT.top=PLAYER1_RECT.bottom+PLAYER1_RECT.height*3
    PLAYER1_SCORE_RECT.centerx=PLAYER1_RECT.centerx
    
    DISPLAYSURF.blit(PLAYER1_SURF,PLAYER1_RECT)
    DISPLAYSURF.blit(PLAYER1_SCORE_SURF,PLAYER1_SCORE_RECT)

    DISPLAYSURF.blit(PLAYER2_SURF,PLAYER2_RECT)
    DISPLAYSURF.blit(PLAYER2_SCORE_SURF,PLAYER2_SCORE_RECT)

    
    DISPLAYSURF.blit(new_image_up,new_rect)
    DISPLAYSURF.blit(undo_image_up,undo_rect)

    if not first_time:
        if FIRST_PLAYER==PLAYER1:
            player1_bgcolor=BACKGROUND
            turn_rect.centerx=PLAYER1_RECT.centerx
            OVER_RIDE_RECT.top=PLAYER1_SCORE_RECT.bottom+40
            OVER_RIDE_RECT.centerx=PLAYER1_SCORE_RECT.centerx
            
        elif FIRST_PLAYER==PLAYER2:
            player2_bgcolor=BACKGROUND
            turn_rect.centerx=PLAYER2_RECT.centerx
            OVER_RIDE_RECT.top=PLAYER2_SCORE_RECT.bottom+40
            OVER_RIDE_RECT.centerx=PLAYER2_SCORE_RECT.centerx
        DISPLAYSURF.blit(turn_image,turn_rect)
    
    if first_time and previous_first_time==None:
        fade_out(DISPLAYSURF)
    if over_ride:
        DISPLAYSURF.blit(OVER_RIDE_SURF,OVER_RIDE_RECT)
    
def blocked(player,i,j,k):
    block=list_of_objects[i][j]
    if block.triangles[0].player==player and block.triangles[1].player==player and block.triangles[2].player==player and block.triangles[3].player==player:
        return(True)
    else:
        if k==0and j!=0:
            block2=list_of_objects[i][j-1]
            if block2.triangles[2].player==player:
                return True
        elif k==1 and i!=0:
            block2=list_of_objects[i-1][j]
            if block2.triangles[3].player==player:
                return True
        elif k==2 and j!=r_c-1:
            block2=list_of_objects[i][j+1]
            if block2.triangles[0].player==player:
                return True
        elif k==3 and i!=r_c-1:
            block2=list_of_objects[i+1][j]
            if block2.triangles[1].player==player:
                return True
    return False
def check_end(current_player,over_ride):
    for i in range(0,r_c):
        for j in range(0,r_c):
            if (number_list[i*r_c+j]%2==0 and current_player==PLAYER1) or (number_list[i*r_c+j]%2!=0 and current_player==PLAYER2):
                for k in range(4):
                    if list_of_objects[i][j].triangles[k].player==None:
                        return False
                    elif over_ride==True and list_of_objects[i][j].triangles[k].player!=current_player:
                        return False
                
    return(True)

def new():
    display_start()
    global list_of_objects,number_list,over_ride,first_time,previous_number_list
    list_of_objects=[]
    number_list=[]
    previous_number_list=[]
    for i in range(0,r_c):
        list_of_objects.append([])
        for j in range(0,r_c):
            obj=Block(False,pygame.Rect(i*BLOCK_SIZE+BOARD_X_PLACE,j*BLOCK_SIZE+BOARD_Y_PLACE,BLOCK_SIZE-BLOCK_WIDTH,BLOCK_SIZE-BLOCK_WIDTH))
            list_of_objects[i].append(obj)
    for i in range(r_c*r_c): 
        number_list.append(i)
    random.shuffle(number_list)
    previous_number_list.extend(number_list)
    over_ride=False
    first_time=True
    draw_board(BACKGROUND)
def display_win_message():
    global WIN_RECT,WIN_SURF
    if winner==PLAYER1:
        text=PLAYER1+'!! won ...tap to start new game'
        write_high_score(player1_score)
    elif winner==PLAYER2:
        text=PLAYER2+'!! won ...tap to start new game'
        write_high_score(player2_score)
    else:
        text="it's a DRAW ...tap to start new game"
        write_high_score(player1_score)
    WIN_SURF,WIN_RECT=make_text(text,WHITE,None,0,0)
    WIN_RECT.left=WINDOW_WIDTH/2-WIN_RECT.width/2
    WIN_RECT.top=WINDOW_HEIGHT/2-WIN_RECT.height/2
    half_fade_in(DISPLAYSURF)
    DISPLAYSURF.blit(WIN_SURF,WIN_RECT)
    
def end_event_handeling_function():
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONDOWN:
                fade_in(DISPLAYSURF)
                return
new()
#mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
            
        elif event.type==MOUSEBUTTONDOWN:
            if new_rect.collidepoint(event.pos):
                button_animation(DISPLAYSURF,new_image_down,new_image_up,new_rect)
                fade_in(DISPLAYSURF)
                new()
            elif undo_rect.collidepoint(event.pos):
                button_animation(DISPLAYSURF,undo_image_down,undo_image_up,undo_rect)
                if not first_time and undo==True:
                    number_list=[]
                    number_list.extend(previous_number_list)
                    previous_triangle.player=previous_player
                    if previous_first_time:
                        first_time=previous_first_time
                    if not over_ride:
                        FIRST_PLAYER,SECOND_PLAYER=SECOND_PLAYER,FIRST_PLAYER
                    over_ride=previous_over_ride
                    draw_board(FIRST_PLAYER)
                    fade_in_out(DISPLAYSURF)
                    undo=False
                    break
                
            for i in range(0,r_c): 
                for j in range(0,r_c):
                    block=list_of_objects[i][j]
                    if block.rect.collidepoint(event.pos):
                        if first_time:
                            if number_list[r_c*i+j]%2==0:
                                FIRST_PLAYER=PLAYER1
                                SECOND_PLAYER=PLAYER2
                            else:
                                FIRST_PLAYER=PLAYER2
                                SECOND_PLAYER=PLAYER1
                            previous_first_time=first_time
                            first_time=False
                        else:
                            previous_first_time=first_time
                        if (number_list[r_c*i+j]%2==0 and FIRST_PLAYER==PLAYER1) or (number_list[r_c*i+j]%2!=0 and FIRST_PLAYER==PLAYER2):
                            if block.triangles[0].collide(event.pos):
                                k=0
                                if FIRST_PLAYER==PLAYER2:
                                    if block.triangles[k].player==None or (block.triangles[k].player!=PLAYER2 and over_ride):
                                        player2_0_rect.center=(block.triangles[0].pts[0][0]+BLOCK_SIZE/2-BLOCK_WIDTH/2,block.triangles[0].pts[0][1]+BLOCK_SIZE/4+BLOCK_WIDTH/4)
                                        put_in(DISPLAYSURF,player2_0,player2_0_rect)
                                        undo=True
                                        previous_triangle=block.triangles[k]
                                else:
                                    if block.triangles[k].player==None or (block.triangles[k].player!=PLAYER1 and over_ride):
                                        player1_0_rect.center=(block.triangles[0].pts[0][0]+BLOCK_SIZE/2-BLOCK_WIDTH/2,block.triangles[0].pts[0][1]+BLOCK_SIZE/4+BLOCK_WIDTH/4)
                                        put_in(DISPLAYSURF,player1_0,player1_0_rect)
                                        undo=True
                                        previous_triangle=block.triangles[k]
                            elif block.triangles[1].collide(event.pos):
                                k=1
                                if FIRST_PLAYER==PLAYER2:
                                    if block.triangles[k].player==None or (block.triangles[k].player!=PLAYER2 and over_ride):
                                        player2_1_rect.center=(block.triangles[1].pts[0][0]+BLOCK_SIZE/4+BLOCK_WIDTH/4,block.triangles[1].pts[0][1]+BLOCK_SIZE/2-BLOCK_WIDTH/2)
                                        put_in(DISPLAYSURF,player2_1,player2_1_rect)
                                        undo=True
                                        previous_triangle=block.triangles[k]
                                else:
                                    if block.triangles[k].player==None or (block.triangles[k].player!=PLAYER1 and over_ride):
                                        player1_1_rect.center=(block.triangles[1].pts[0][0]+BLOCK_SIZE/4+BLOCK_WIDTH/4,block.triangles[1].pts[0][1]+BLOCK_SIZE/2-BLOCK_WIDTH/2)
                                        put_in(DISPLAYSURF,player1_1,player1_1_rect)
                                        undo=True
                                        previous_triangle=block.triangles[k]
                            elif block.triangles[2].collide(event.pos):
                                k=2
                                if FIRST_PLAYER==PLAYER2:
                                    if block.triangles[k].player==None or (block.triangles[k].player!=PLAYER2 and over_ride):
                                        player2_2_rect.center=(block.triangles[2].pts[0][0]+BLOCK_SIZE/2-BLOCK_WIDTH/2,block.triangles[2].pts[0][1]-BLOCK_SIZE/4-BLOCK_WIDTH/4)
                                        put_in(DISPLAYSURF,player2_2,player2_2_rect)
                                        undo=True
                                        previous_triangle=block.triangles[k]
                                else:
                                    if block.triangles[k].player==None or (block.triangles[k].player!=PLAYER1 and over_ride):
                                        player1_2_rect.center=(block.triangles[2].pts[0][0]+BLOCK_SIZE/2-BLOCK_WIDTH/2,block.triangles[2].pts[0][1]-BLOCK_SIZE/4-BLOCK_WIDTH/4)
                                        put_in(DISPLAYSURF,player1_2,player1_2_rect)
                                        undo=True
                                        previous_triangle=block.triangles[k]
                            else:
                                k=3
                                if FIRST_PLAYER==PLAYER2:
                                    if block.triangles[k].player==None or (block.triangles[k].player!=PLAYER2 and over_ride):
                                        player2_3_rect.center=(block.triangles[3].pts[0][0]-BLOCK_SIZE/4-BLOCK_WIDTH/4,block.triangles[3].pts[0][1]-BLOCK_SIZE/2+BLOCK_WIDTH/2)
                                        put_in(DISPLAYSURF,player2_3,player2_3_rect)
                                        undo=True
                                        previous_triangle=block.triangles[k]
                                else:
                                    if block.triangles[k].player==None or (block.triangles[k].player!=PLAYER1 and over_ride):
                                        player1_3_rect.center=(block.triangles[3].pts[0][0]-BLOCK_SIZE/4-BLOCK_WIDTH/4,block.triangles[3].pts[0][1]-BLOCK_SIZE/2+BLOCK_WIDTH/2)
                                        put_in(DISPLAYSURF,player1_3,player1_3_rect)
                                        undo=True
                                        previous_triangle=block.triangles[k]
                            previous_player=block.triangles[k].player
                            block.triangles[k].player=FIRST_PLAYER
                            if blocked(FIRST_PLAYER,i,j,k)==False:
                                if previous_player==None:
                                    FIRST_PLAYER,SECOND_PLAYER=SECOND_PLAYER,FIRST_PLAYER
                                    previous_over_ride=over_ride
                                    over_ride=False
                                    previous_number_list=[]
                                    previous_number_list.extend(number_list)
                                    random.shuffle(number_list)
                                    
                                elif previous_player==SECOND_PLAYER and over_ride==True:
                                    FIRST_PLAYER,SECOND_PLAYER=SECOND_PLAYER,FIRST_PLAYER
                                    previous_over_ride=over_ride
                                    over_ride=False
                                    previous_number_list=[]
                                    previous_number_list.extend(number_list)
                                    random.shuffle(number_list)
                                    
                                elif previous_player==SECOND_PLAYER and over_ride==False:
                                    block.triangles[k].player=previous_player  
                            elif blocked(FIRST_PLAYER,i,j,k)==True:
                                if previous_player==SECOND_PLAYER and over_ride==False:
                                    block.triangles[k].player=previous_player
                                elif previous_player==FIRST_PLAYER:
                                    pass
                                else:
                                    previous_over_ride=over_ride
                                    over_ride=True
                                    play_block_sound()
                                    if android:
                                        android.vibrate(0.2)
                                    shake(DISPLAYSURF)
                                    previous_number_list=[]
                                    previous_number_list.extend(number_list)
                                    random.shuffle(number_list)
                        draw_board(FIRST_PLAYER)
    pygame.display.update()
    if not first_time:
        if check_end(FIRST_PLAYER,over_ride):
            play_end_sound()
            pygame.time.wait(500)
            display_win_message()
            end_event_handeling_function()
            new()



