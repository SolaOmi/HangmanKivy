#!/usr/bin/env python3

# Hangman
# By Bisola Bruno solaocodes@gmail.com

import os
import sys
from random import randint

from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout

FPS = 1 / 60
WINDOWWIDTH = 500
WINDOWHEIGHT = 600
NUM_OF_GUESSES = 5
INNER_MARGIN = 15
OUTER_MARGIN = 10
BACKGROUND_COLOR = '#963e48'
BORDER_LINE_COLOR = '#FFD700'

class HangmanBoard(BoxLayout):

    files = list(filter(lambda x: x.endswith('.txt'), os.listdir()))
    file_in = files[randint(0,len(files)-1)]
    with open(file_in, 'r') as f:
        words = f. readlines()

    words = [i.strip() for i in words]
    category = words[0].upper()
    full_word = words[randint(1, len(words)-1)]
    empty_word = ['_' if i.isalpha() else i for i in full_word]
    misses = []

    def letter_click(self, letter):

        letter.disabled = True
        letter.disabled_color = [1,1,1,1]
        letter.background_disabled_normal = ''

        guess = letter.text.lower()
        answer = self.full_word.lower()

        letter.background_color = [1,0,0,0.5]
        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    self.empty_word[i] = self.full_word[i]
                    letter.background_color = [0,1,0,0.5]
        else:
            self.misses.append(guess)

    def update(self, dt):

        self.ids['category'].text = self.category
        self.ids['empty_word'].text = ' '.join(self.empty_word)

        self.win_or_lose()

    def win_or_lose(self):
        if self.full_word == ''.join(self.empty_word):
            self.ids['animation'].text = 'YOU WIN!'
            self.disable_letters()
            Clock.schedule_once(sys.exit, 5)
        elif NUM_OF_GUESSES == len(self.misses):
            self.ids['animation'].text = 'YOU LOSE!'
            self.disable_letters()
            Clock.schedule_once(sys.exit, 5)

    def disable_letters(self):
        for k,v in self.ids.items():
            if k[0:6] == 'letter':
                v.disabled = True



class HangmanApp(App):

    Config.set('graphics', 'resizable', 0)
    Config.set('graphics', 'width', WINDOWWIDTH)
    Config.set('graphics', 'height', WINDOWHEIGHT)

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
