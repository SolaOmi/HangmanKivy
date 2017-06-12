#!/usr/bin/env python3

# Hangman
# By Bisola Bruno solaocodes@gmail.com

import os
import sys
from random import randint

from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.anchorlayout import AnchorLayout

FPS = 1 / 60 # frames per second
WINDOWWIDTH = 500 # size of window's with in pixels
WINDOWHEIGHT = 600 # size of window's height in picels
NUM_OF_GUESSES = 5 # number of guesses before game over
INNER_MARGIN = 15
OUTER_MARGIN = 10
BACKGROUND_COLOR = '#963e48'
BORDER_LINE_COLOR = '#FFD700'

class HangmanBoard(AnchorLayout):
    # Class that contains the Hangman game

    # open up a text file with a category and words.
    files = list(filter(lambda x: x.endswith('.txt'), os.listdir()))
    file_in = files[randint(0,len(files)-1)]
    with open(file_in, 'r') as f:
        words = f. readlines()

    words = [i.strip() for i in words] # potential list of words to guess
    category = words[0].upper() # category of word to guess
    word = words[randint(1, len(words)-1)] # word to guess
    hidden_word = ['_' if i.isalpha() else i for i in word] # word to guess obscured with '_'
    misses = 0 # number of wrong guesses

    def letter_click(self, letter):
        # Checks if clicked letter is in the word or not

        letter.disabled = True
        letter.disabled_color = [1,1,1,1]
        letter.background_disabled_normal = ''

        guess = letter.text.lower()
        answer = self.word.lower()

        # sets letter background to red
        letter.background_color = [1,0,0,0.5]

        # checks for match, and turns letter background green if correct
        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    self.hidden_word[i] = self.word[i]
                    letter.background_color = [0,1,0,0.5]
        else:
            self.misses += 1

    def update(self, dt):
        # renders updates of guesses and hidden word, and checks if the game is
        # won or not

        self.ids['category'].text = self.category
        self.ids['hidden'].text = ' '.join(self.hidden_word)

        self.win_or_lose()

    def win_or_lose(self):
        # checks if the game is won or not

        if self.word == ''.join(self.hidden_word):
            self.ids['animation'].text = 'YOU WIN!'
            self.disable_letters()
            Clock.schedule_once(sys.exit, 5)
        elif NUM_OF_GUESSES == self.misses:
            self.ids['animation'].text = 'YOU LOSE!'
            self.disable_letters()
            Clock.schedule_once(sys.exit, 5)

    def disable_letters(self):
        # disables all remaining letters immediately after game is won or lost.

        for k,v in self.ids.items():
            if k[0:6] == 'letter':
                v.disabled = True



class HangmanApp(App):
    # App that runs Hangman game.

    # Configuration Settings
    Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
    Config.set('graphics', 'resizable', 0)
    Config.set('graphics', 'width', WINDOWWIDTH)
    Config.set('graphics', 'height', WINDOWHEIGHT)

    # Makes constant variables avaiable to hangman.kv file
    IM = INNER_MARGIN
    OM = OUTER_MARGIN
    BGCOLOR = BACKGROUND_COLOR
    BLCOLOR = BORDER_LINE_COLOR

    def build(self):
        game = HangmanBoard()
        Clock.schedule_interval(game.update, FPS)
        return game


if __name__ == '__main__':
    HangmanApp().run()
