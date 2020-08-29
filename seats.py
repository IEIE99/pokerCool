import pygame
from colours import black, lblack, white, yellow, red, lblue, rand_col,fold_color, \
     one, two, three, four, lgrey, grey, name_chips, to_act, action, empty_seat, winner,\
     player_border, empty_seat_inner, empty_seat_outer, all_in

print(rand_col)

""" CONSTANTS """

CENTRE = {1:(155,240, 'top_right'),
          2:(180,120, 'bottom_right'),
          3:(405,80, 'bottom_right'), 
          4:(605,80, 'bottom_right'),
          5:(830,120, 'bottom_left'),
          6:(855,240, 'bottom_left'),
          7:(830,360, 'top_left'),
          8:(605,400, 'top_left'),
          9:(405,400, 'top_left'),
          10:(180,360,'top_right')
          }

up = 20
right = 39
right_bet = 59

OFFSET_TEXT = {'top_right': {'bet': (right_bet, -up),
                         'name': (-right, up),
                         'chips': (right, up),
                         'action': (-up, -up)},
           'top_left': {'bet': (-right_bet, -up),
                         'name': (-right, up),
                         'chips': (right, up),
                         'action': (up, -up)},
           'bottom_right': {'bet': (right_bet, up),
                         'name': (-right, -up),
                         'chips': (right, -up),
                         'action': (-up, up)},
           'bottom_left': {'bet': (-right_bet, up),
                         'name': (-right, -up),
                         'chips': (right, -up),
                         'action': (up, up)}
           }

OFFSET_LINE = {'top_right': {'quarter': (right, -up),
                             'half': (0, up)},
               'top_left': {'quarter': (-39, -up),
                             'half': (0, up)},
               'bottom_right': {'quarter': (right, up),
                                'half': (0, -up)},
               'bottom_left': {'quarter': (-right, up),
                               'half': (0, -up)},           
           }

OFFSET_HIGHLIGHT = {'top_right': {'quarter': (+right, -18),
                             'half': (0, +18)},
               'top_left': {'quarter': (-right, -18),
                             'half': (0, +18)},
               'bottom_right': {'quarter': (+right, +18),
                                'half': (0, -18)},
               'bottom_left': {'quarter': (-right, +18),
                               'half': (0, -18)},           
           }


class Seat():
    def __init__(self, number, name, game_window, in_hand=True):
        self.number = number
        self.name = name
        self.game_window = game_window
        
        self.occupied = False
        self.drawing_func = None #'(Decorator)'
        self.color = white


    def update_player_info(self, name, chips, bet):
        
        self.draw()
        self.update_bet(bet)
        self.update_name(name, name_chips)
        self.update_chips(chips, name_chips)       
        pygame.display.update()

    def update_bet(self, bet):
        x, y = parse('bet', self.number, CENTRE, OFFSET_TEXT)
        self.color = lblack
        self.draw_rect(x, y, 33, 31)
        if bet > 0:
            self.draw_msg(x, y, '{0:.0f}'.format(bet), 16, red)
        pygame.display.update()

    def update_chips(self, chips, color):
        x, y = parse('chips', self.number, CENTRE, OFFSET_TEXT)
        self.color = lblack
        self.draw_rect(x, y, 70, 30)
        self.draw_msg(x, y, '{0:.0f}'.format(chips), 16, color)
        pygame.display.update()

    def update_name(self, name, color):
        x, y = parse('name', self.number, CENTRE, OFFSET_TEXT)
        self.color = lblack
        self.draw_rect(x, y, 70, 30)
        self.draw_msg(x, y, name, 16, color)
        pygame.display.update()

    def update_action(self, action, size, color):
        x, y = parse('action', self.number, CENTRE, OFFSET_TEXT)
        self.color = lblack
        self.draw_rect(x, y, 110, 30)
        self.draw_msg(x, y, action, size, color)
        pygame.display.update()
        
    def draw(self):
        x, y, _ = CENTRE[self.number]
        x_half, y_half = parse('half', self.number, CENTRE, OFFSET_LINE)
        x_quarter, y_quarter = parse('quarter', self.number, CENTRE, OFFSET_LINE)
        self.color = player_border
        self.draw_rect(x, y, 161, 81)        
        self.color = lblack
        self.draw_rect(x, y, 155, 75)
        self.color = player_border
        self.draw_rect(x, y, 161, 3)
        self.draw_rect(x_half, y_half, 3, 37)
        self.draw_rect(x_quarter, y_quarter, 3, 37)
        
        pygame.display.update()

    def draw_highlight(self, name, chips, bet):
        highlight = red
        x, y, _ = CENTRE[self.number]
        x_half, y_half = parse('half', self.number, CENTRE, OFFSET_HIGHLIGHT)
        x_quarter, y_quarter = parse('quarter', self.number, CENTRE, OFFSET_HIGHLIGHT)
        self.color = yellow
        self.draw_rect(x, y, 161, 81)
        self.color = highlight
        self.draw_rect(x, y, 157, 77)
        self.color = white
        self.draw_rect(x, y, 153, 73)
        self.color = lblack
        self.draw_rect(x, y, 151, 71)
        self.color = black
        self.draw_rect(800, 540, 200, 60)

        self.color = white
        self.draw_rect(x, y, 151, 3)
        self.draw_rect(x_half, y_half, 3, 36)
        self.draw_rect(x_quarter, y_quarter, 3, 36)

        self.color = highlight
        self.draw_rect(x, y, 151, 1)
        self.draw_rect(x_half, y_half, 1, 36)
        self.draw_rect(x_quarter, y_quarter, 1, 36)

        if bet != 0:
            self.update_bet(bet)
        self.update_chips(chips, name_chips)
        self.update_name(name, name_chips)
        self.update_action('TO ACT...', 20, yellow)

        
        pygame.display.update()

    def draw_folded_seat(self, name, chips):
        highlight = grey
        x, y, _ = CENTRE[self.number]
        x_half, y_half = parse('half', self.number, CENTRE, OFFSET_HIGHLIGHT)
        x_quarter, y_quarter = parse('quarter', self.number, CENTRE, OFFSET_HIGHLIGHT)
        self.color = highlight
        self.draw_rect(x, y, 161, 81)
        self.color = lblack
        self.draw_rect(x, y, 157, 77)
        self.color = highlight
        self.draw_rect(x, y, 153, 73)
        self.color = lblack
        self.draw_rect(x, y, 151, 71)

        self.color = highlight
        self.draw_rect(x, y, 151, 3)
        self.draw_rect(x_half, y_half, 3, 36)
        self.draw_rect(x_quarter, y_quarter, 3, 36)

        self.color = lblack
        self.draw_rect(x, y, 151, 1)
        self.draw_rect(x_half, y_half, 1, 36)
        self.draw_rect(x_quarter, y_quarter, 1, 36)

        self.update_chips(chips, fold_color)
        self.update_name(name, fold_color)
        self.update_bet(0)
        pygame.display.update()
        
    @classmethod
    def draw_empty_seat(self, display, seat):
        x, y, _ = CENTRE[seat]
        
        pygame.draw.circle(display, empty_seat_outer, (x+20, y), 40)
        pygame.draw.circle(display, empty_seat_outer, (x-20, y), 40)
        Seat.draw_rect_cls_method(display, empty_seat_outer, x,y, 40,80)
        pygame.draw.circle(display, lblack, (x+20, y), 39)
        pygame.draw.circle(display, lblack, (x-20, y), 39)
        Seat.draw_rect_cls_method(display, black, x,y, 40,78)
        pygame.draw.circle(display, empty_seat_inner, (x+20, y), 37)
        pygame.draw.circle(display, empty_seat_inner, (x-20, y), 37)
        Seat.draw_rect_cls_method(display, empty_seat_inner, x,y, 40,74)
        pygame.draw.circle(display, lblack, (x+20, y), 35)
        pygame.draw.circle(display, lblack, (x-20, y), 35)
        Seat.draw_rect_cls_method(display, lblack, x,y, 40,70)
        Seat.draw_msg_cls_method(display, x, y, 'Empty Seat', 16, fold_color)
        pygame.display.update()
        
        
    def show_pot(self, amount):
        pygame.draw.rect(self.game_window,black,(430,317,140,26))            ###delete pot
        pygame.draw.line(self.game_window,yellow,(429,316),(570,316),2)
        pygame.draw.line(self.game_window,yellow,(429,342),(570,342),2)
        pygame.draw.line(self.game_window,yellow,(429,342),(429,316),2)
        pygame.draw.line(self.game_window,yellow,(570,316),(570,342),2)
        self.color = white
        self.draw_msg(500, 332, "POT: "+str(amount), 20, white)

    def draw_rect(self, x, y, w, h):
        rect = pygame.Rect(x, y, w, h)
        rect.center = (x, y)
        pygame.draw.rect(self.game_window, self.color, rect)

    def draw_msg(self, x, y, message, size, color):
        msg = pygame.font.Font('freesansbold.ttf', size).render(message, True, color)
        rect = msg.get_rect()
        rect.center = (x, y)
        self.game_window.blit(msg,rect)
        
    @classmethod
    def draw_rect_cls_method(self,display, color, x, y, w, h):
        rect = pygame.Rect(x, y, w, h)
        rect.center = (x, y)
        pygame.draw.rect(display, color, rect)

    @classmethod
    def draw_msg_cls_method(self,display, x, y, message, size, color):
        msg = pygame.font.Font('freesansbold.ttf', size).render(message, True, color)
        rect = msg.get_rect()
        rect.center = (x, y)
        display.blit(msg,rect)



def parse(square, seat, centre, offset):
    x, y, pos = centre[seat]    
    x_, y_ = offset[pos][square]
    x_new, y_new = x + x_, y + y_
    return (x_new, y_new)

