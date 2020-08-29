import pygame
from colours import white
from players import Player
from seats import Seat
import inspect

""" CONSTANTS """

DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 600
CARD_WIDTH = 78
CARD_HEIGHT = 106
GAP = 2

class GameWindow():
    def __init__(self, width, height):
        self.surface = pygame.display.set_mode((width, height))
        

class Table:
    background = pygame.image.load('Cards_png/download2.jpe') 
    table_design = pygame.image.load('Cards_png/table.png')
    
    def __init__(self):

        self.players = [Player(1, 'Ian', win.surface),
                        Player(2, 'Tony', win.surface),
                        Player(4, 'James', win.surface),
                        Player(5, 'Oli', win.surface),
                        Player(7, 'Garth', win.surface),
                        Player(8, 'Jono', win.surface),
                        Player(10, 'Edu', win.surface),                        
                        ]

        self.total_chips = 7000

    def move_dealer(self):
        temp = self.players[0]
        temp.name2 = temp.name
        del self.players[0]
        self.players.append(temp)
        print('----------------------------')

    def show_blinds(self, SB, BB):
        self.players[0].bet = SB
        self.players[1].bet = BB
        self.players[0].chips -= SB
        self.players[1].chips -= BB
        self.players[0].update_bet()
        self.players[1].update_bet()
        self.players[0].update_chips()
        self.players[1].update_chips()
        self.players[0].seat.update_action('Small Blind', 16, white)
        self.players[1].seat.update_action('Big Blind', 16, white)
        self.players[len(table.players)-1].seat.update_action('Dealer', 16, white)


    def update(self):
        
        win.surface.blit(Table.background ,(0, 0))
        win.surface.blit(Table.background ,(474, 0))
        win.surface.blit(Table.background ,(948, 0))
        win.surface.blit(Table.table_design ,(180, 85))

        seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        for p in self.players:
            p()
            if p.seat.number in seats:
                seats.remove(p.seat.number)

        for s in seats:
            Seat.draw_empty_seat(win.surface, s)         

        
        
        
    @classmethod
    def draw_table(self):
        
        win.surface.blit(Table.background ,(0, 0))
        win.surface.blit(Table.background ,(474, 0))
        win.surface.blit(Table.background ,(948, 0))
        win.surface.blit(Table.table_design ,(180, 85))

        pygame.draw.line(win.surface, white, (0,470) , (1000,470) , 10)
        x=200
        color = (x,x,x)
        pygame.draw.line(win.surface, color, (0,471) , (1000,471) , 9)
        x=150
        color = (x,x,x)
        pygame.draw.line(win.surface, color, (0,472) , (1000,472) , 8)
        x=100
        color = (x,x,x)
        pygame.draw.line(win.surface, color, (0,473) , (1000,473) , 7)
        x=75
        color = (x,x,x)
        pygame.draw.line(win.surface, color, (0,474) , (1000,474) , 6)
        x=50
        color = (x,x,x)
        pygame.draw.line(win.surface, color, (0,475) , (1000,475) , 5)
        x=100
        color = (x,x,x)
        pygame.draw.line(win.surface, color, (0,476) , (1000,476) , 4)
        x=150
        color = (x,x,x)
        pygame.draw.line(win.surface, color, (0,477) , (1000,477) , 3)
        x=200
        color = (x,x,x)
        pygame.draw.line(win.surface, color, (0,478) , (1000,478) , 2)
        
        pygame.draw.line(win.surface, white, (0,479) , (1000,479) , 1)

        
    @classmethod
    def show_flop(self, current):
        win.surface.blit(current.flop.card1.image,(GAP+(CARD_WIDTH * 4), int(DISPLAY_HEIGHT*0.3)))
        win.surface.blit(current.flop.card2.image,(GAP+(CARD_WIDTH * 5), int(DISPLAY_HEIGHT*0.3)))
        win.surface.blit(current.flop.card3.image,(GAP+(CARD_WIDTH * 6), int(DISPLAY_HEIGHT*0.3)))
        pygame.display.update()
        
    @classmethod
    def show_turn(self, current):
        win.surface.blit(current.turn.image,(GAP+(CARD_WIDTH * 7), int(DISPLAY_HEIGHT*0.3)))
        pygame.display.update()

    @classmethod
    def show_river(self, current):
        win.surface.blit(current.river.image,(GAP+(CARD_WIDTH * 8), int(DISPLAY_HEIGHT*0.3)))
        pygame.display.update()

    @classmethod
    def clear_pot(self):
        win.surface.blit(pygame.image.load('Cards_png/table_new3.png'),(290,140 ))
        pygame.display.update()




        
""" LAUNCH PYGAME """
pygame.init()
clock = pygame.time.Clock()

""" DRAW TABLE """
win = GameWindow(DISPLAY_WIDTH, DISPLAY_HEIGHT)

pygame.display.set_caption("POKER")


Table.draw_table()

for s in range(1,11):
    Seat.draw_empty_seat(win.surface,s)
            



table = Table()






##table.player1.seat.draw()

##print(inspect.signature(table))
##print(dir(table))#.__getattribute__)





