import Main_poker_2 as pok
import pygame

while intro == True:


    ################################################################################################

    """ NUMBER OF SEATS / CHIPS / BLINDS """
    Players = 5 #int(input("Enter number of Players: "))
    Starting_Chips = 3000 #int(input("Starting Chips: "))
    SB = 25
    BB = 50

    """ CONSTANTS """

    display_width = 1000
    display_height = 600
    card_width = 78
    card_height = 106
    gap = 2

    """ COLOURS """

    white = (255, 255, 255)
    light_grey = (150,150,150)
    lighter_grey = (211,222,233)

    fold_color = (77,135,240)
    black = (0, 0, 0)
    green = (40,80,20)
    yellow = (255,200,50)

    """ INITIATE PLAYERS """

    for i in range(Players):
        globals()['player'+str(i)] = Player()    
        
        if i == Players - 1:
            globals()['player'+str(i)].next = 'player'+str(0)
        else:
            globals()['player'+str(i)].next = 'player'+str(i+1)    
        
    try:
        player0.name = "Ian"
    except: a = 1
    try:
        player1.name = "Garth"
    except: a = 1
    try:
        player2.name = "Tony"
    except: a = 1
    try:
        player3.name = "Jimmy"
    except: a = 1
    try:
        player4.name = "Edu"
    except: a = 1
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

    player0.pos = "D"
    current = Current_Hand()      



    """ LAUNCH PYGAME"""
    pygame.init()
    clock = pygame.time.Clock()


    """ DRAW TABLE """
    win = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("POKER")

    x = pygame.image.load('Cards_png/download2.jpe')
    y = pygame.image.load('Cards_png/table.png')
    ##print("Width: ",y.get_width())
    ##print("Height: ",y.get_height())
    win.blit(x ,(0, 0))
    win.blit(x ,(474, 0))
    win.blit(x ,(948, 0))
    win.blit(y ,(180, 85))


    pok.draw_table()
    pok.prepare_new_hand()

        
    """ START HAND """        
    ##for p in Player._registry:
    ##   
    ##    print (p.name)
    ##    print(p.dealt_hand)
    ##    print(p.get_turn())


    pok.hand_loop()
    pygame.display.update()


       

        #message(str(clock.get_time),10,10,20)
        

        
    




    pygame.quit()
    quit()
    
