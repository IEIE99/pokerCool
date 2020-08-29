import pygame
import table_graphics as tg
#import Main_poker_2 as mp

class Table10(object):
    def __init__(self):
        self.s1 = Seat((115,260),(195,260),(135,220),(215,220),(75,200))
        self.s2 = Seat((140,100),(220,100),(160,140),(240,140),(100,80))
        self.s3 = Seat((365,60),(445,60),(385,100),(465,100),(325,40))
        self.s4 = Seat((565,60),(645,60),(585,100),(665,100),(525,40))
        self.s5 = Seat((790,100),(870,100),(850,140),(770,140),(750,80))
        self.s6 = Seat((815,220),(895,220),(875,260),(795,260),(775,200))
        self.s7 = Seat((790,380),(870,380),(850,340),(770,340),(750,320))
        self.s8 = Seat((565,420),(645,420),(625,380),(545,380),(525,360))
        self.s9 = Seat((365,420),(445,420),(425,380),(345,380),(325,360))
        self.s10 = Seat((140,380),(220,380),(160,340),(240,340),(100,320))
        
        self.win = pygame.display.set_mode((1000,600))

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.lt_grey = (222,222,222)
        self.dk_grey = (150,150,150)
        self.dk_red = (155,66,44)
        
    def draw_seat(self, seat, num):

        x = seat.top_left[0]
        y = seat.top_left[1]

        tg.highlight(self.win, seat, self.lt_grey)
        tg.draw_seat(self.win, seat.name, seat.chips, seat.bet, self.dk_grey, self.black,self.dk_grey)
        pygame.draw.rect(self.win, self.black,(x+4,y+4,154,74))
        tg.text(self.win, "Seat "+str(num),(x + 80,y + 26),20, self.dk_red)
        tg.text(self.win, "Empty",(x + 80,y + 54),20, self.dk_red)
        pygame.draw.line(self.win, self.lt_grey, (x + 20,y + 38),(x + 140,y + 38) , 2)
        pygame.display.update()

    def draw_table(self):        
                                      
        pygame.display.set_caption("POKER")

        x = pygame.image.load('Cards_png/download2.jpe')
        y = pygame.image.load('Cards_png/table.png')
        self.win.blit(x ,(0, 0))
        self.win.blit(x ,(474, 0))
        self.win.blit(x ,(948, 0))
        self.win.blit(y ,(180, 85))

        pygame.draw.line(self.win, self.white, (0,470) , (1000,470) , 10)
        x=200
        color = (x,x,x)
        pygame.draw.line(self.win, color, (0,471) , (1000,471) , 9)
        color = (x-50,x-50,x-50)
        pygame.draw.line(self.win, color, (0,472) , (1000,472) , 8)
        color = (x-100,x-100,x-100)
        pygame.draw.line(self.win, color, (0,473) , (1000,473) , 7)
        color = (x-125,x-125,x-125)
        pygame.draw.line(self.win, color, (0,474) , (1000,474) , 6)
        color = (x-150,x-150,x-150)
        pygame.draw.line(self.win, color, (0,475) , (1000,475) , 5)
        color = (x-100,x-100,x-100)
        pygame.draw.line(self.win, color, (0,476) , (1000,476) , 4)
        color = (x-50,x-50,x-50)
        pygame.draw.line(self.win, color, (0,477) , (1000,477) , 3)
        color = (x,x,x)
        pygame.draw.line(self.win, color, (0,478) , (1000,478) , 2)    
        pygame.draw.line(self.win, self.white, (0,479) , (1000,479) , 1)

        self.draw_seat(self.s1, 1)
        self.draw_seat(self.s2, 2)
        self.draw_seat(self.s3, 3)
        self.draw_seat(self.s4, 4)
        self.draw_seat(self.s5, 5)
        self.draw_seat(self.s6, 6)
        self.draw_seat(self.s7, 7)
        self.draw_seat(self.s8, 8)
        self.draw_seat(self.s9, 9)
        self.draw_seat(self.s10, 10)

        
        pygame.display.update()
             

class Seat(object):
    def __init__(self, name, chips, action, bet, top_left):
        self.top_left = top_left
        self.name = name
        self.action = action
        self.bet = bet
        self.chips = chips
        self.empty = True


        


t1 = Table10()
pygame.init()
t1.draw_table()
##t1.draw_seat(t1.s1)

        
