from random import randint, random
from collections import namedtuple

Color = namedtuple('Color', 'red, blue, green, alpha')

def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red, green, blue, alpha)

rand_col = random_color()

white = (255, 255, 255, 1)
grey = (150,150,150)
lgrey = (222,244,222)

fold_color = (155,66,44)
black = (0, 0, 0)
lblack = (33,33,33)
green = (40,80,20)
lblue = (88, 133, 255)
yellow = (255,200,50)
red = (255,10,20)

""" from random """

one = (126, 85, 62, 0.22)
two = (141, 55, 36, 0.39)
three = (199, 49, 26, 0.98)
four = (140, 101, 79, 0.13)

name_chips = (17,191,230,0.75)
to_act = yellow
all_in = lblue
action = white
empty_seat = grey
winner = yellow
player_border = lgrey
empty_seat_outer = lgrey
empty_seat_inner = grey


#Color(red=125, blue=197, green=116, alpha=0.98)
