from time import sleep
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
    def talk(self):
        input_string = 'Hey my name is Henrik and Edward.'
        character_scanner = {' ' : sleep(1),
                             '.' : sleep(2),
                             ',' : sleep(1),
                             'a' : sleep(1)}

        while True:
            self.animator.read_letter()
            sleep(1)
            
    #Idle animation.
    def idle(self, seconds):
        counter = 0
        while counter < seconds * 2:
            self.animator.idle()
            counter += 1
            sleep(0.5)
