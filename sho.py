import pygame

def textDropShadow(font, message, offset, fontcolor, shadowcolor):
    base = font.render(message, 0, fontcolor)
    size = base.get_width() + offset, base.get_height() + offset
    img = pygame.Surface(size, 16)
    base.set_palette_at(1, shadowcolor)
    img.blit(base, (offset, offset))
    base.set_palette_at(1, fontcolor)
    img.blit(base, (0, 0))
    return img




entry_info = 'Drop Shadow, by Pete Shinners'

#this code will display our work, if the script is run...
if __name__ == '__main__':
    pygame.init()

    #create our fancy text
    white = 255, 255, 255
    grey = 100, 100, 100
    bigfont = pygame.font.Font(None, 60)
    text = textDropShadow(bigfont, entry_info, 3, white, grey)

    #create a window the correct size
    win = pygame.display.set_mode(text.get_size())
    winrect = win.get_rect()
    win.blit(text, (0, 0))
    pygame.display.flip()
    
    #wait for the finish
    while 1:
        event = pygame.event.wait()
        if event.type is KEYDOWN and event.key == K_s: #save it
            name = os.path.splitext(sys.argv[0])[0] + '.bmp'
            print('Saving image to:', name)
            pygame.image.save(win, name)
        elif event.type in (QUIT,KEYDOWN,MOUSEBUTTONDOWN):
            break
