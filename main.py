#!/usr/bin/env python3

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from random import randint


class HangmanBoard(BoxLayout):
    words = {"Random": ["food", "boy", "animal", "zebra"], "Numbers": ["one", "two", "three"]}
    categories = list(words.keys())
    misses = []
    guesses = []
    category = categories[randint(0, len(categories)-1)]
    word = words[category][randint(0, len(words[category])-1)]
    empty = ["_"]*len(word)
    nguess = 0

    # widgets

    #category_label = self.ids['label1']
    #empty_word_label = self.ids['label2A']
    #empty_word = self.ids['label2B']
    #misses_label = self.ids['label2D']
    #misses = self.ids['label2E']
    #last_guess_label = self.ids['label2F']
    #last_guess = self.ids['label2G']
    #illustration = self.ids['label3']
    #letter_input = self.ids['label4']

    def label_names(self, *args):
        category_label = self.ids['label1']
        empty_word_label = self.ids['label2A']
        misses_label = self.ids['label2D']
        last_guess = self.ids['label2F']

        category_label.text = self.category
        empty_word_label.text = 'WORD'
        misses_label.text = 'MISSES'
        last_guess.text = 'LAST GUESS'

    def update(self, *args):
        empty_word = self.ids['label2B']
        misses = self.ids['label2E']
        #last_guess = self.ids['label2G']
        #illustration = self.ids['label3']
        letter_input = self.ids['label4']

        empty_word.text = ' '.join(self.empty)
        misses.text =  ' '.join(self.misses)

        if self.nguess < 5:

            guess = letter_input.text

            if guess in self.word:
                for i in range(len(self.word)):
                    if guess == self.word[i]:
                        self.empty[i] = guess
            else:
                self.misses.append(guess)
                self.nguess += 1

            if self.word == "".join(self.empty):
                #print("\nYou win!")
                exit(0)

        #if self.nguess >= 5:
            #exit(0)

class HangmanApp(App):

    def build(self):
        game = HangmanBoard()
        game.label_names()
        Clock.schedule_interval(game.update, 1/60)
        return game


if __name__ == '__main__':
    HangmanApp().run()
