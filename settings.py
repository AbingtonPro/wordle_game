# COLORS (r, g, b)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (80, 80, 80)
LIGHTGREY = (120, 120, 120)
BRIGHTGREY = (180, 180, 180)
# For a softer green added 30 to red and blue
GREEN = (30, 180, 30)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
CYAN = (0, 180, 180)
# For a softer yellow added 30 to red and 30 to blue
YELLOW = (210, 180, 30)
BRIGHTYELLOW = (255, 255, 0)
MAGENTA = (220, 0, 195)
BGCOLOUR = (40, 40, 40)

# Game settings
WIDTH = 600
HEIGHT = 900
MARGINHEIGHT = 800
FPS = 60
title = "Wordle! written in Python PyGame - https://github.com/AbingtonPro"

TILESIZE = 80
GAPSIZE = 10

MARGIN_X = int((WIDTH - (5 * (TILESIZE + GAPSIZE))) / 2)
MARGIN_Y = int((MARGINHEIGHT - (6 * (TILESIZE + GAPSIZE))) / 2)

# Constant values for keyboard indicators
ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
KEY_WIDTH     = 40
KEY_HEIGHT    = 40
KEY_RADIUS    = 5
KEY_MARGIN    = 5
LEFT_MARGIN   = 50
TOP_MARGIN    = 700
