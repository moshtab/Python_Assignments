'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Deck of cards”
'''
import random


class Card:
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value
    def show(self):
        print("{} of {}".format(self.value, self.suit))
class Deck:
    def __init__(self):
        self.cards =[]
        self.build()
    def build(self):
        for s in ["Spades","Clubs","Daimonds","Hearts"]:
            for v in range(1,14):
                self.cards.append(Card(s,v))
    def show(self):
        for c in self.cards:
            c.show()
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r=random.randint(0,i)
            self.cards[i],self.cards[r]=self.cards[r],self.cards[i]
deck = Deck()
deck.shuffle()
deck.show()