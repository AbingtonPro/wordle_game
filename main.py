# main.py - Wordle game written in Pygame 
# Improvements by Art@AbingtonPro.com 11/27/2023
# Credits (I got the basic code and ideas from these YouTube channels):
#   https://www.youtube.com/@techandgaming0
#   https://www.youtube.com/@baraltech
# Many thanks to the above and others who post about python and pygame on YouTube.com
# I hope to eventually post some videos on the improvements on this channel https://www.youtube.com/@abingtonpro

import random
from time import *
import pygame
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.letters_text = UIElement(165, 100, "Not Enough Letters", MAGENTA, 25)
        self.not_valid_text = UIElement(165, 100, " Not a Valid Word", MAGENTA, 25)
        self.title_text = UIElement(122, 20, "Wordle Game", BRIGHTYELLOW, 60)
        self.title_subtext = UIElement(70, 75, "Solve a 5-letter word in 6 tries", BRIGHTYELLOW, 25)
        self.create_answers_list()
        self.create_allwords_list()
        
    def create_answers_list(self):
        with open("answers.txt", "r") as file:
            self.answers_list = file.read().splitlines()

    def create_allwords_list(self):
        with open("allwords.txt", "r") as file:
            self.allwords_list = file.read().splitlines()

    def new(self):
        #self.word = "SPEED"
        self.word = random.choice(self.answers_list).upper()
        print()
        print("The secret word is", self.word)
        self.text = ""
        self.current_row = 0
        self.tiles = []
        self.create_tiles()
        self.flip = True
        self.not_enough_letters = False
        self.not_valid_word = False
        self.create_answers_list
        self.darkgrey_letters = []
        self.yellow_letters   = []
        self.green_letters    = []
        self.timer = 0

    def create_tiles(self):
        for row in range(6):
            self.tiles.append([])
            for col in range(5):
                for col in range(5):
                    self.tiles[row].append(Tile((col * (TILESIZE + GAPSIZE)) + MARGIN_X, (row * (TILESIZE + GAPSIZE)) + MARGIN_Y))

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.add_letter()

    def add_letter(self):
        #empty all the letters in the current row
        for tile in self.tiles[self.current_row]:
            tile.letter = ''

        # add the letters typed to the current row
        for i, letter in enumerate(self.text):
            self.tiles[self.current_row][i].letter = letter
            self.tiles[self.current_row][i].create_font()
            
    def draw_tiles(self):
        for row in self.tiles:
            for tile in row:
                tile.draw(self.screen)

    def draw_keyboard(self):
        keyboard_font = pygame.font.SysFont("Consolas", 30)
        
        def draw_letter(letter, font, text_color, x, y):
            img = font.render(letter, True, text_color)
            self.screen.blit(img, (x, y))
 
        for i in range(3):
            j = 0
            x, y = 25 + LEFT_MARGIN, TOP_MARGIN
            if i == 1:
                x, y = 25 + ( KEY_WIDTH /2 ) + KEY_MARGIN + LEFT_MARGIN, TOP_MARGIN + 50
            if i == 2:
                x, y = 25 + (KEY_WIDTH * 1.5) + (KEY_MARGIN * 2) + LEFT_MARGIN, TOP_MARGIN + 100

            for letter in ALPHABET[i]:
                key_colour = BRIGHTGREY
                if letter in self.darkgrey_letters:
                    key_colour = LIGHTGREY
                if letter in self.yellow_letters:
                    key_colour = YELLOW
                if letter in self.green_letters:
                    key_colour = GREEN

                pygame.draw.rect(self.screen, key_colour, (x, y, KEY_WIDTH, KEY_HEIGHT), width = 0, border_radius = KEY_RADIUS)
                key_x = x + (KEY_WIDTH * 0.3)
                key_y = y + (KEY_HEIGHT * 0.15)
                draw_letter(letter, keyboard_font, WHITE, key_x, key_y)

                x = x + KEY_WIDTH + KEY_MARGIN
                j += 1

    def draw(self):
        self.screen.fill(BGCOLOUR)
       
        # display not enough letters text
        if self.not_enough_letters:
            self.timer += 1
            self.letters_text.fade_in()
            if self.timer > 105:
                self.not_enough_letters = False
                self.timer = 0
        else:
            self.letters_text.fade_out()

        if self.not_valid_word:
            self.timer += 1
            self.not_valid_text.fade_in()
            if self.timer > 105:
                self.not_valid_word = False
                self.timer = 0
        else:
            self.not_valid_text.fade_out()
 
        self.letters_text.draw(self.screen)
        self.not_valid_text.draw(self.screen)
        self.title_text.fade_in()
        self.title_text.draw(self.screen)
        self.title_subtext.fade_in()
        self.title_subtext.draw(self.screen)
        self.draw_tiles()
        self.draw_keyboard()
        pygame.display.flip()

    def row_animation(self):
        #row shaking if not enough letters
        #self.not_enough_letters = True ## moved to:  # row animation, not enough letters message
        start_pos = self.tiles[0][0].x
        amount_move = 4
        move = 3
        screen_copy = self.screen.copy()
        screen_copy.fill(BGCOLOUR)
        for row in self.tiles:
            for tile in row:
                if row != self.tiles[self.current_row][0]:
                    tile.draw(screen_copy)

        while True:
            while self.tiles[self.current_row][0].x < start_pos + amount_move:
                self.screen.blit(screen_copy, (0, 0))
                for tile in self.tiles[self.current_row]:
                    tile.x += move
                    tile.draw(self.screen)
                self.clock.tick(FPS)
                pygame.display.flip()

            while self.tiles[self.current_row][0].x > start_pos - amount_move:
                self.screen.blit(screen_copy, (0, 0))
                for tile in self.tiles[self.current_row]:
                    tile.x -= move
                    tile.draw(self.screen)
                self.clock.tick(FPS)
                pygame.display.flip()

            amount_move -= 2
            if amount_move < 0:
                break

    def box_animation(self):
        # tile scale animation for every letter inserted
        for tile in self.tiles[self.current_row]:
            if tile.letter == "":
                screen_copy = self.screen.copy()
                for start, end, step in ((0, 6, 1), (0, -6, -1)):
                    for size in range(start, end, 2*step):
                        self.screen.blit(screen_copy, (0, 0))
                        tile.x -= size
                        tile.y -= size
                        tile.width += size * 2
                        tile.height += size * 2
                        surface = pygame.Surface((tile.width, tile.height))
                        surface.fill(BGCOLOUR)
                        self.screen.blit(surface, (tile.x, tile.y))
                        tile.draw(self.screen)
                        pygame.display.flip()
                        self.clock.tick(FPS)
                    self.add_letter()
                break

    def reveal_animation(self, tile, colour):
        # reveal colours animation when user inputs the entire word
        screen_copy = self.screen.copy()

        while True:
            surface = pygame.Surface((tile.width + 5, tile.height + 5))

            surface.fill(BGCOLOUR)
            screen_copy.blit(surface, (tile.x, tile.y))
            self.screen.blit(screen_copy, (0, 0))
            if self.flip:
                tile.y += 6
                tile.height -= 12
                tile.font_y += 4
                tile.font_height = max(tile.font_height - 8, 0)
            else:
                tile.colour = colour
                tile.y -= 6
                tile.height += 12
                tile.font_y -= 4
                tile.font_height = min(tile.font_height + 8, tile.font_size)
            if tile.font_height == 0:
                self.flip = False

            tile.draw(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)

            if tile.font_height == tile.font_size:
                self.flip = True
                break

    def check_letters(self):
        # algorithm to determine if letters correspond to the letters in the actual word
        # and to assign a color GREY, YELLOW, or GREEN.
        copy_word = [x for x in self.word]
        for i, user_letter in enumerate(self.text):
            colour = DARKGREY
            self.darkgrey_letters.append(user_letter)
            for j, letter in enumerate(copy_word):
                if user_letter == letter:
                    colour = YELLOW
                    self.yellow_letters.append(user_letter)
                    if i == j:
                        colour = GREEN
                        self.green_letters.append(user_letter)
                    copy_word[j] = ""
                    break
            # reveal animation
            self.reveal_animation(self.tiles[self.current_row][i], colour)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(self.text) == 5:
                    
                        # check if the word is in the accepted words 'allwords'
                        if self.text.lower() in self.allwords_list:
                            
                            # check all letters and place colors
                            self.check_letters()

                            # check if the text is correct or the player has used all the turns
                            if self.text == self.word or self.current_row + 1 == 6:
                                #player loses and losing message is sent
                                if self.text != self.word:
                                    self.end_screen_text = UIElement(110, 720, f'THE WORD WAS "{self.word}"', CYAN, 35)

                                # player wins and send winning message
                                else:
                                    self.end_screen_text = UIElement(220, 720, "YOU WON!", BRIGHTYELLOW, 40)

                                # restart the game
                                self.playing = False
                                self.end_screen()
                                break

                            self.current_row += 1
                            self.text = ""

                        else:
                             # reject word and display not_valid message
                            self.not_valid_word = True
                            self.row_animation()

                    else:
                        # row animation, not enough letters message
                        self.not_enough_letters = True
                        self.row_animation()
                        

                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]

                else:
                    if len(self.text) < 5 and event.unicode.isalpha():
                        self.text += event.unicode.upper()
                        self.box_animation()

    def end_screen(self):
        play_again = UIElement(110, 780, "PRESS [ENTER] TO PLAY AGAIN", WHITE, 25)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.darkgrey_letters = []
                        yellow_letters   = []
                        green_letters    = []

                        return

            self.screen.fill(BGCOLOUR)
            self.draw_tiles()
            self.end_screen_text.fade_in()
            self.end_screen_text.draw(self.screen)
            play_again.fade_in()
            play_again.draw(self.screen)
            self.title_text.fade_in()
            self.title_text.draw(self.screen)
            self.title_subtext.fade_in()
            self.title_subtext.draw(self.screen)

            pygame.display.flip()

game = Game()
while True:
    game.new()
    game.run()

    
