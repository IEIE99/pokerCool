import pygame

def draw_seat(win,n,c,b,color, border, middle):

    w = 40
    h = 20
    thickness = 2

    left = min(n[0],c[0]) - w    
    up = min(n[1],b[1]) - h
    right = w + max(n[0],c[0])
    down = h + max(n[1],b[1])

    bet_top = b[1] < n[1]
    bet_left = b[0] < n[0]

    pygame.draw.rect(win, middle, (left-3,up-3,4*w+9,4*h+9)) 

    if bet_top:
        if bet_left:
            pygame.draw.line(win, color, (left + w, up + (2*h )) , (left + w, up) , thickness)
        else:
            pygame.draw.line(win, color, (right - w, up + (2*h)) , (right-w, up) , thickness)
        pygame.draw.line(win, color, (left + (2*w), up + (2*h)) , (left + (2*w), down) , thickness)
    else:
        if bet_left:
            pygame.draw.line(win, color, (left + w, up + (2*h)) , (left + w, down) , thickness)
        else:
            pygame.draw.line(win, color, (right - w, up + (2*h)) , (right-w, down) , thickness)
        pygame.draw.line(win, color, (left + (2*w), up + (2*h)) , (left + (2*w), up) , thickness)
     
    pygame.draw.line(win, border, (left,up) , (right,up) , thickness)
    pygame.draw.line(win, color, (left,up+(2*h)) , (right,up+(2*h)) , thickness)
    pygame.draw.line(win, border, (left,down) , (right,down) , thickness)

    pygame.draw.line(win, border, (left,up) , (left,down) , thickness)
    pygame.draw.line(win, border, (right,up) , (right,down) , thickness)

def text(win, text,a,size, color):
    font = pygame.font.Font('freesansbold.ttf', size)
    text_surf, text_rect = text_object(str(text),font,color)
    text_rect.center = (a)
    win.blit(text_surf,text_rect)
    pygame.display.update()

def text_object(text, font, color):
    ts = font.render(text, True, color)
    return ts, ts.get_rect()


def highlight(win, seat, color):
    x = seat.top_left[0] - 4
    y = seat.top_left[1] - 4
    
    pygame.draw.line(win, color, (x, y) , (x+168, y) , 4)
    pygame.draw.line(win, color, (x, y) , (x, y+88) , 4)
    pygame.draw.line(win, color, (x, y+88) , (x+168, y+88) , 4)
    pygame.draw.line(win, color, (x+168, y), (x+168, y+88) , 4)
    pygame.display.update()

def clear_bet_sq(win, pl):
    x = pl.get_coord_bet()[0] - 18
    y = pl.get_coord_bet()[1] - 18
    
    pygame.draw.rect(win, black, (x, y, 36, 36))
    
    pygame.display.update()   


def clear_chips_sq(win, pl):
    x = pl.get_coord_chips()[0] - 38
    y = pl.get_coord_chips()[1] - 18
    
    pygame.draw.rect(win, black, (x, y, 76, 36))
    
    pygame.display.update()


def clear_name_sq(win, pl):
    x = pl.get_coord_name()[0] - 38
    y = pl.get_coord_name()[1] - 18
    
    pygame.draw.rect(win, black, (x, y, 76, 36))
    
    pygame.display.update()


def clear_action_sq(win, pl):
    x = pl.get_coord_action()[0] - 58
    y = pl.get_coord_action()[1] - 18
    
    pygame.draw.rect(win, black, (x, y, 116, 36))
    
    pygame.display.update()   
    
