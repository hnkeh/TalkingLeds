from time import sleep
from random import randint
from animator import *
from colors import *

class TalkingLeds():
    def __init__(self):
        #Standard values.
        self.background_color = black
        self.eye_color = red
        self.pupil_color = white
        self.lips_color = red
        self.teeth_color = white
        self.tongue_color = pink

        self.warm_chance = 100

        self.animator = Animator(self.background_color, self.pupil_color, self.eye_color,  self.teeth_color, self.tongue_color, self.lips_color, 300, 300)
        

    #Public functions.
    #Translating string to talkingleds.
    def talk(self, input_string):
        character_scanner = {' ' : sleep(1),
                             '.' : sleep(2),
                             ',' : sleep(1),
                             'a' : self.animator.a,
                             'b' : self.animator.b}

    #TODO: Add all mouth animations to c_scanner.

        for l in input_string:
            character_scanner[l]()
            sleep(0.5)

    #Idle animation.
    def idle(self, seconds):
        warm_chance = randint(0, 100)
        counter = 0
        while counter < seconds * 2:
            if warm_chance <= 90:
                self.animator.idle()
            else:
                self.animator.warm_anime()
            counter += 1
            sleep(0.5)
