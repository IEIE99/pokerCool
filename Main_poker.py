import random
import pokerfunctions as pf
import pygame
import time



class Player(object):
    """
    Player represented as Table, Position, Chips, Dealt_Hand, in_Hand Boolean
    """
    _registry = []
    
    def __init__(self):
        self._registry.append(self)
        
        #,table,position,chips, name, dealt_hand): #, inhand, dealer, SB, BB):
        #assert type(table) == int and type(position)== int and type(name) == str and type(chips) == int and type(dealt_hand) == pf.HoleCards,"" # and type(in_hand)== bool and type(dealer)== bool and type(SB)== bool and type(BB)== bool,""
        #self.dealer = dealer
        #self.SB = SB
        #self.BB = BB
        self.table = 1
        self.pos = ""
        self.dealt_hand = None
        self.next = ""
        self.curr_bet = 0
        self.action_count = 0
        self.in_hand = True
        self.opened_betting = False
        self.chips = Starting_Chips
        self.turn = False
        self.name = None
        self.coord_name = None
        self.coord_chips = None
        self.coord_action = None
        self.coord_bet = None
        self.coord_top_left = None
        
    def set_pos(self,pos):
        self.pos = pos
    def get_pos(self):
        return self.pos

    def set_curr_bet(self,curr_bet):
        self.curr_bet = curr_bet
    def get_curr_bet(self):
        return self.curr_bet
    def set_chips(self,chips):
        self.chips = chips
    def get_chips(self):
        return self.chips    
    def set_turn(self,turn):
        self.turn = turn
    def get_turn(self):
        return self.turn
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def set_coord_name(self,coord_name):
        self.coord_name = coord_name
    def get_coord_name(self):
        return self.coord_name
    def set_coord_chips(self,coord_chips):
        self.coord_chips = coord_chips
    def get_coord_chips(self):
        return self.coord_chips
    def set_coord_action(self,coord_action):
        self.coord_action = coord_action
    def get_coord_action(self):
        return self.coord_action
    def set_coord_bet(self,coord_bet):
        self.coord_bet = coord_bet
    def get_coord_bet(self):
        return self.coord_bet
    def set_coord_top_left(self,coord_top_left):
        self.coord_top_left = coord_top_left
    def get_coord_top_left(self):
        return self.coord_top_left

class Current_Hand(object):
    def __init__(self, active_players, turn_count):

        self.active_players = active_players
        self.turn_count = turn_count
        self.pre_flop_bet = None
        self.flop_bet = None
        self.turn_bet = None
        self.river_bet = None
        self.pot = 0

    def set_ap(self, ap):
        self.active_players = ap

    
    
    def get_ap(self):
        return self.active_players

    def get_tc(self):
        return self.turn_count
        
       
""" END OF CLASS DEFINITIONS """

def card(a, b):
    win.blit(Ad,(a,b))

def text_object(text, font, color):
    ts = font.render(text, True, color)
    return ts, ts.get_rect()
    
def message(text,a,b,size, color):
    font = pygame.font.Font('freesansbold.ttf', size)
    text_surf, text_rect = text_object(text,font,color)
    text_rect.center = (a,b)
    win.blit(text_surf,text_rect)
    pygame.display.update()

def message2(text,a,size, color):
    font = pygame.font.Font('freesansbold.ttf', size)
    text_surf, text_rect = text_object(str(text),font,color)
    text_rect.center = (a)
    win.blit(text_surf,text_rect)
    pygame.display.update()

def draw_highlight(pl):
    x = pl.get_coord_top_left()[0] - 4
    y = pl.get_coord_top_left()[1] - 4
    red = (255, 0, 0)
    pygame.draw.line(win, red, (x, y) , (x+168, y) , 4)
    pygame.draw.line(win, red, (x, y) , (x, y+88) , 4)
    pygame.draw.line(win, red, (x, y+88) , (x+168, y+88) , 4)
    pygame.draw.line(win, red, (x+168, y), (x+168, y+88) , 4)
    pygame.display.update()    
    
    return

def remove_highlight(pl):
    x = pl.get_coord_top_left()[0] - 4
    y = pl.get_coord_top_left()[1] - 4
    
    pygame.draw.line(win, black, (x, y) , (x+168, y) , 4)
    pygame.draw.line(win, black, (x, y) , (x, y+88) , 4)
    pygame.draw.line(win, black, (x, y+88) , (x+168, y+88) , 4)
    pygame.draw.line(win, black, (x+168, y), (x+168, y+88) , 4)
    pygame.display.update()

def clear_bet_sq(pl):
    x = pl.get_coord_bet()[0] - 18
    y = pl.get_coord_bet()[1] - 18
    
    pygame.draw.rect(win, black, (x, y, 36, 36))
    
    pygame.display.update()   
    
    return

def clear_chips_sq(pl):
    x = pl.get_coord_chips()[0] - 38
    y = pl.get_coord_chips()[1] - 18
    
    pygame.draw.rect(win, black, (x, y, 76, 36))
    
    pygame.display.update()   
    
    return

def clear_action_sq(pl):
    x = pl.get_coord_action()[0] - 58
    y = pl.get_coord_action()[1] - 18
    
    pygame.draw.rect(win, black, (x, y, 116, 36))
    
    pygame.display.update()   
    
    return

def draw_seat2(n,c,b,color):
    w = 40
    h = 20
    thickness = 2

    left = min(n[0],c[0]) - w    
    up = min(n[1],b[1]) - h
    right = w + max(n[0],c[0])
    down = h + max(n[1],b[1])

    bet_top = b[1] < n[1]
    bet_left = b[0] < n[0]

    pygame.draw.line(win, color, (left,up) , (right,up) , thickness)
    pygame.draw.line(win, color, (left,up+(2*h)) , (right,up+(2*h)) , thickness)
    pygame.draw.line(win, color, (left,down) , (right,down) , thickness)

    pygame.draw.line(win, color, (left,up) , (left,down) , thickness)
    pygame.draw.line(win, color, (right,up) , (right,down) , thickness)

    if bet_top:
        if bet_left:
            pygame.draw.line(win, color, (left + w, up + (2*h)) , (left + w, up) , thickness)
        else:
            pygame.draw.line(win, color, (right - w, up + (2*h)) , (right-w, up) , thickness)
        pygame.draw.line(win, color, (left + (2*w), up + (2*h)) , (left + (2*w), down) , thickness)
    else:
        if bet_left:
            pygame.draw.line(win, color, (left + w, up + (2*h)) , (left + w, down) , thickness)
        else:
            pygame.draw.line(win, color, (right - w, up + (2*h)) , (right-w, down) , thickness)
        pygame.draw.line(win, color, (left + (2*w), up + (2*h)) , (left + (2*w), up) , thickness)
     
    

    print(left,up,right,down,bet_top,"Dimensions: ",right - left, down - up)
    
    
def draw_table():
    
    pygame.draw.line(win, white, (0,470) , (1000,470) , 10)
    x=200
    color = (x,x,x)
    pygame.draw.line(win, color, (0,471) , (1000,471) , 9)
    x=150
    color = (x,x,x)
    pygame.draw.line(win, color, (0,472) , (1000,472) , 8)
    x=100
    color = (x,x,x)
    pygame.draw.line(win, color, (0,473) , (1000,473) , 7)
    x=75
    color = (x,x,x)
    pygame.draw.line(win, color, (0,474) , (1000,474) , 6)
    x=50
    color = (x,x,x)
    pygame.draw.line(win, color, (0,475) , (1000,475) , 5)
    x=100
    color = (x,x,x)
    pygame.draw.line(win, color, (0,476) , (1000,476) , 4)
    x=150
    color = (x,x,x)
    pygame.draw.line(win, color, (0,477) , (1000,477) , 3)
    x=200
    color = (x,x,x)
    pygame.draw.line(win, color, (0,478) , (1000,478) , 2)
    
    pygame.draw.line(win, white, (0,479) , (1000,479) , 1)
    #seat 1
    try:
        player0.set_coord_name((115,260))
        player0.set_coord_chips((195,260))
        player0.set_coord_action((135,220))
        player0.set_coord_bet((215,220))
        player0.set_coord_top_left((75,200))
                
        draw_seat2(player0.get_coord_name(),player0.get_coord_chips(),player0.get_coord_bet(),white)
        message2(player0.get_name(),player0.get_coord_name(),20, white)
        message2(str(player0.get_chips()),player0.get_coord_chips(),20, white)
    except:
        draw_seat2((115,260),(195,260),(215,220),light_grey)
        message2("Seat 1",(115,260),20, light_grey)
        message2("Empty",(195,260),20, light_grey)

    #seat 2
    try:
        player1.set_coord_name((140,100))
        player1.set_coord_chips((220,100))
        player1.set_coord_action((160,140))
        player1.set_coord_bet((240,140))
        player1.set_coord_top_left((100,80))

        draw_seat2(player1.get_coord_name(),player1.get_coord_chips(),player1.get_coord_bet(),white)
        message2(player1.get_name(),player1.get_coord_name(),20, white)
        message2(str(player1.get_chips()),player1.get_coord_chips(),20, white)
    except:
        draw_seat2((140,100),(220,100),(240,140),light_grey)
        message2("Seat 2",(140,100),20, light_grey)
        message2("Empty",(220,100),20, light_grey)
        

    #seat 3
    try:
        player2.set_coord_name((365,60))
        player2.set_coord_chips((445,60))
        player2.set_coord_action((385,100))
        player2.set_coord_bet((465,100))
        player2.set_coord_top_left((325,40))

        draw_seat2(player2.get_coord_name(),player2.get_coord_chips(),player2.get_coord_bet(),white)
        message2(player2.get_name(),player2.get_coord_name(),20, white)
        message2(str(player2.get_chips()),player2.get_coord_chips(),20, white)
    except:
        draw_seat2((365,60),(445,60),(465,100),light_grey)
        message2("Seat 3",(365,60),20, light_grey)
        message2("Empty",(445,60),20, light_grey)  

    #seat 4
    try:
        player3.set_coord_name((565,60))
        player3.set_coord_chips((645,60))
        player3.set_coord_action((585,100))
        player3.set_coord_bet((665,100))
        player3.set_coord_top_left((525,40))

        draw_seat2(player3.get_coord_name(),player3.get_coord_chips(),player3.get_coord_bet(),white)
        message2(player3.get_name(),player3.get_coord_name(),20, white)
        message2(str(player3.get_chips()),player3.get_coord_chips(),20, white)
    except:
        draw_seat2((565,60),(645,60),(665,100),light_grey)
        message2("Seat 4",(565,60),20, light_grey)
        message2("Empty",(645,60),20, light_grey) 
       
    #seat 5
    try:
        player4.set_coord_name((790,100))
        player4.set_coord_chips((870,100))
        player4.set_coord_action((850,140))
        player4.set_coord_bet((770,140))
        player4.set_coord_top_left((750,80))

        draw_seat2(player4.get_coord_name(),player4.get_coord_chips(),player4.get_coord_bet(),white)
        message2(player4.get_name(),player4.get_coord_name(),20, white)
        message2(str(player4.get_chips()),player4.get_coord_chips(),20, white)
    except:
        draw_seat2((790,100),(870,100),(770,140),light_grey)
        message2("Seat 1",(790,100),20, light_grey)
        message2("Empty",(870,100),20, light_grey) 

    #seat 6   
    try:
        player5.set_coord_name((815,220))
        player5.set_coord_chips((895,220))
        player5.set_coord_action((875,260))
        player5.set_coord_bet((795,260))
        player5.set_coord_top_left((775,200))

        draw_seat2(player5.get_coord_name(),player5.get_coord_chips(),player5.get_coord_bet(),white)
        message2(player5.get_name(),player5.get_coord_name(),20, white)
        message2(str(player5.get_chips()),player5.get_coord_chips(),20, white)
    except:
        draw_seat2((815,220),(895,220),(795,260),light_grey)
        message2("Seat 6",(815,220),20, light_grey)
        message2("Empty",(895,220),20, light_grey)

    #seat 7
    try:
        player6.set_coord_name((790,380))
        player6.set_coord_chips((870,380))
        player6.set_coord_action((850,340))
        player6.set_coord_bet((770,340))
        player6.set_coord_top_left((750,320))

        draw_seat2(player6.get_coord_name(),player6.get_coord_chips(),player6.get_coord_bet(),white)
        message2(player6.get_name(),player6.get_coord_name(),20, white)
        message2(str(player6.get_chips()),player6.get_coord_chips(),20, white)
    except:
        draw_seat2((790,380),(870,380),(770,340),light_grey)
        message2("Seat 7",(790,380),20, light_grey)
        message2("Empty",(870,380),20, light_grey)
        

    #seat 8
    try:
        player7.set_coord_name((565,420))
        player7.set_coord_chips((645,420))
        player7.set_coord_action((625,380))
        player7.set_coord_bet((545,380))
        player7.set_coord_top_left((525,360))

        draw_seat2(player7.get_coord_name(),player7.get_coord_chips(),player7.get_coord_bet(),white)
        message2(player7.get_name(),player7.get_coord_name(),20, white)
        message2(str(player7.get_chips()),player7.get_coord_chips(),20, white)
    except:
        draw_seat2((565,420),(645,420),(545,380),light_grey)
        message2("Seat 8",(565,420),20, light_grey)
        message2("Empty",(645,420),20, light_grey)

    #seat 9
    try:
        player8.set_coord_name((365,420))
        player8.set_coord_chips((445,420))
        player8.set_coord_action((425,380))
        player8.set_coord_bet((345,380))
        player8.set_coord_top_left((325,360))

        draw_seat2(player8.get_coord_name(),player8.get_coord_chips(),player8.get_coord_bet(),white)
        message2(player8.get_name(),player8.get_coord_name(),20, white)
        message2(str(player8.get_chips()),player8.get_coord_chips(),20, white)
    except:
        draw_seat2((365,420),(445,420),(345,380),light_grey)
        message2("Seat 9",(365,420),20, light_grey)
        message2("Empty",(445,420),20, light_grey)       

    #seat 10
    try:
        player9.set_coord_name((140,380))
        player9.set_coord_chips((220,380))
        player9.set_coord_action((160,340))
        player9.set_coord_bet((240,340))
        player9.set_coord_top_left((100,320))

        draw_seat2(player9.get_coord_name(),player9.get_coord_chips(),player9.get_coord_bet(),white)
        message2(player9.get_name(),player9.get_coord_name(),20, white)
        message2(str(player9.get_chips()),player9.get_coord_chips(),20, white)
    except:
        draw_seat2((140,380),(220,380),(240,340),light_grey)
        message2("Seat 10",(140,380),20, light_grey)
        message2("Empty",(220,380),20, light_grey)

def prepare_new_hand():
    
    pygame.draw.rect(win, black, (320, 180, 400, 200))
    pygame.display.update()




    
    return

def show_current_player(pl):
    print("in current player loop")
    
    win.blit(pl.dealt_hand.card1.image,(gap+(card_width * 0), display_height - 113))
    win.blit(pl.dealt_hand.card2.image,(gap+(card_width * 1), display_height - 113))
    
    clear_bet_sq(pl)        
    message2(pl.get_curr_bet(),pl.get_coord_bet(),20, white)

    clear_chips_sq(pl)        
    message2(pl.get_chips(),pl.get_coord_chips(),20, white)
    
    pygame.draw.rect(win,black,(400,300,200,60)) ###delete pot    
    message("POT: "+str(current.pot), 500, 330, 20, white) ###show pot
    
    if pl.curr_bet != current.largest_bet:
        pygame.draw.rect(win,white,(250,510,100,60))
        message("Fold",300, 540, 20, black)
    
    pygame.draw.rect(win,white,(400,510,100,60))

    if pl.curr_bet == current.largest_bet:
        message("Call",450, 540, 20, black)
    else:
        message("Check",450, 540, 20, black)
        
    pygame.draw.rect(win,white,(550,510,100,60))
    
    if pl.curr_bet == current.largest_bet:
        message("Bet",600, 540, 20, black)
    else:
        message("Raise",600, 540, 20, black)

    

    
    

    
            
    pygame.display.update()
    return
def show_click_fold():
    print("show click")
    pygame.draw.rect(win,light_grey,(250,510,100,60))
    pygame.display.update()
    pygame.time.wait(250)
    return

def show_click_check():
    print("show click")
    pygame.draw.rect(win,light_grey,(400,510,100,60))
    pygame.display.update()
    pygame.time.wait(250)
    return

def show_click_bet():
    print("show click")
    pygame.draw.rect(win,light_grey,(550,510,100,60))
    pygame.display.update()
    pygame.time.wait(250)
    return

def reset_action_count():
    for p in Player._registry:
        p.action_count = 0
        
    return

def select_next_player():
    for p in Player._registry:
        if p.turn == True:
                       
            globals()[p.next].set_turn(True)
            p.set_turn(False)
            return

def show_folded():
    for p in Player._registry:
        if p.in_hand == False:
            message2("Folded",p.get_coord_action(),20, fold_color)
    return    
             
    
    
def more_betting():
    print("in more betting")
    #find out if all bets are the same#
    global pre_flop_betting
    global flop_betting
    global turn_betting
    global river_betting
    
    show_folded()

    for p in Player._registry:
        if p.turn == True:
            if p.in_hand == False:
                select_next_player()
                break
            draw_highlight(p)
           
            if p.curr_bet < current.largest_bet:                
                    
                wait_for_action(p)
                remove_highlight(p)
                globals()[p.next].set_turn(True)
                p.set_turn(False)
                return
            elif p.action_count == 0:                
                    
                wait_for_action(p)
                remove_highlight(p)
                globals()[p.next].set_turn(True)
                p.set_turn(False)
                return
            else:
                pre_flop_betting = False
                flop_betting = False
                turn_betting = False
                river_betting = False

                current.largest_bet = 0
                reset_action_count()
                
                for p in Player._registry:
                    p.set_turn(False)
                    if p.get_pos() == "SB":
                        p.set_turn(True)
                    
                    p.set_curr_bet(0)
                    clear_bet_sq(p)
                    clear_action_sq(p)
                    remove_highlight(p)
                    message2(p.get_pos(),p.get_coord_bet(),20, white)                  
                return
            
def wait_for_action(pl):
   
    pygame.event.clear()
    while True:
        event3 = pygame.event.wait()
        if event3.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event3.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            print("mouse pressed")
            if 250 < mouse[0] < 350 and 510 < mouse[1] < 570:
                show_click_fold()
                pl.action_count += 1
                if current.largest_bet == 0:
                    clear_action_sq(pl)
                    message2("Checked",pl.get_coord_action(),20, white)
                    show_current_player(pl)
                else:
                    clear_action_sq(pl)
                    message2("Folded",pl.get_coord_action(),20, fold_color)
                    pl.in_hand = False
                    
                    clear_bet_sq(pl)
                    message2(pl.get_pos(),pl.get_coord_bet(),20, white)
                    draw_seat2(pl.get_coord_name(),pl.get_coord_chips(),pl.get_coord_bet(),light_grey)
                    show_current_player(pl)
                print("POT: "+str(current.pot))
                return
            if 400 < mouse[0] < 500 and 510 < mouse[1] < 570:
                show_click_check()
                pl.action_count += 1
                if current.largest_bet == 0:
                    clear_action_sq(pl)
                    message2("Checked",pl.get_coord_action(),20, white)
                    show_current_player(pl)
                else:
                    pl.chips -= (current.largest_bet - pl.curr_bet)
                    current.pot += (current.largest_bet - pl.curr_bet)
                    pl.curr_bet += (current.largest_bet - pl.curr_bet)
                    clear_action_sq(pl)
                    message2("Called",pl.get_coord_action(),20, white)
                    show_current_player(pl)
                print("POT: "+str(current.pot))
                return
            if 550 < mouse[0] < 650 and 510 < mouse[1] < 570:
                show_click_bet()
                pl.action_count += 1
                if current.largest_bet == 0:
                    pl.curr_bet += current.largest_bet + 20
                    pl.chips -= 20
                    current.pot += 20
                    current.largest_bet = pl.curr_bet                    
                    clear_action_sq(pl)
                    message2("Bet",pl.get_coord_action(),20, white)
                    show_current_player(pl)
                else:
                    pl.curr_bet += current.largest_bet + 20
                    pl.chips -= current.largest_bet + 20
                    current.pot += current.largest_bet + 20
                    current.largest_bet = pl.curr_bet                    
                    clear_action_sq(pl)
                    message2("Raised",pl.get_coord_action(),20, white)
                    show_current_player(pl)
                print("POT: "+str(current.pot))
                return
                
                
        
def river_loop():
    
    win.blit(river.image,(gap+(card_width * 8), int(display_height*0.3)))
    pygame.display.update()    

    while river_betting:
        
        more_betting()
        
def turn_loop():
    
    win.blit(turn.image,(gap+(card_width * 7), int(display_height*0.3)))
    pygame.display.update()

    while turn_betting:
        
        more_betting()

def flop_loop():

    win.blit(flop.card1.image,(gap+(card_width * 4), int(display_height*0.3)))
    win.blit(flop.card2.image,(gap+(card_width * 5), int(display_height*0.3)))
    win.blit(flop.card3.image,(gap+(card_width * 6), int(display_height*0.3)))
    pygame.display.update()

    while flop_betting:
        
        more_betting()

def pre_flop_loop():
    print("Entered pre_flop_loop")
    

    while pre_flop_betting:
        
        more_betting()
    


        
def hand_loop():
    
    global action_count
    global open_count
    global pre_flop_betting
    global flop_betting
    global turn_betting
    global river_betting

    global clock

    tick_count = 0

    current_hand = True
    
    while current_hand:

        pygame.time.delay(50)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        while pre_flop_betting:
            
            pre_flop_loop()
                        
        flop_betting = True
        
        while flop_betting: 

            flop_loop()            
            
        turn_betting = True
        
        while turn_betting:                              
            
            turn_loop()
                                   
        river_betting = True
       
        while river_betting:                              
            
            river_loop()
                        
        break
    print("hand loop finished")
    prepare_new_hand()
    hand_loop()

def shuffle():

    """ SHUFFLE DECK """

    Deck_Fresh =pf.FreshDeck()
    Deck_Shuffled = pf.ShuffleDeck(Deck_Fresh)



    """ DEAL HANDS """

    hands, DECK = pf.Deal(Deck_Shuffled,Players)



    for index in range(len(hands)):
        print(hands[index])

    """Deal community cards"""

    flop, DECK = pf.Deal_Flop(DECK)
    turn = DECK[0]
    river = DECK[1]

    print("Flop:")
    print (flop)
    print("Turn:")
    print(turn)
    print("River:")
    print(river)


    return hands, flop, turn, river


""" NUMBER OF SEATS / CHIPS """
Players = 5 #int(input("Enter number of Players: "))
Starting_Chips = 3000 #int(input("Starting Chips: "))
hands, flop, turn, river = shuffle()


display_width = 1000
display_height = 600
card_width = 78
card_height = 106
white = (255, 255, 255)
light_grey = (150,150,150)
fold_color = (77,125,200)
black = (0, 0, 0)

action_count = 0
open_count = 0
gap = 2



""" INITIATE PLAYERS """

for i in range(Players):
    globals()['player'+str(i)] = Player()
    globals()['player'+str(i)].position = i
    globals()['player'+str(i)].dealt_hand = hands[i]
    if i == Players - 1:
        globals()['player'+str(i)].next = 'player'+str(0)
    else:
        globals()['player'+str(i)].next = 'player'+str(i+1)
    
    #print (globals()['player'+str(i)].next)

player0.name = "Ian"
player1.name = "Garth"
player2.name = "Tony"
player3.name = "Jimmy"
player4.name = "Edu"
try:
    player5.name = "Jono"
except: a = 1
try:
    player6.name = "Oli"
except: a = 1
try:
    player7.name = "Vargas"
except: a = 1
try:
    player8.name = "Diego"
except: a = 1
try:
    player9.name = "Juan"
except: a = 1


""" DEFINE GLOBALS """

player1.curr_bet = 10
player1.chips -= 10
player2.curr_bet = 20
player2.chips -= 20
player0.pos = "D"
player1.pos = "SB"
player2.pos = "BB"
player2.opened_betting = True

       
current = Current_Hand(Players, 0)
current.largest_bet = 20
current.pot = 30

pre_flop_betting = True
flop_betting = False
turn_betting = False
river_betting = False

next_action = True



""" LAUNCH PYGAME"""
pygame.init()
clock = pygame.time.Clock()


""" DRAW TABLE """
win = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("POKER")
draw_table()
message2(player0.get_pos(),player0.get_coord_bet(),20, white)
message2(player1.get_curr_bet(),player1.get_coord_bet(),20, white)
message2("Small Blind",player1.get_coord_action(),20, white)
message2(player2.get_curr_bet(),player2.get_coord_bet(),20, white)
message2("Big Blind",player2.get_coord_action(),20, white)
player3.set_turn(True)
show_current_player(player3)



    
""" START HAND """        
for p in Player._registry:
   
    print (p.name)
    print(p.dealt_hand)
    print(p.get_turn())


hand_loop()
pygame.display.update()


   

    #message(str(clock.get_time),10,10,20)
    

    
    




pygame.quit()
quit()



        

    
