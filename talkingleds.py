#Python imports.
import pyttsx3
import _thread
from time import sleep
from random import randint

#Talkingleds imports.
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
        
        self.voice = pyttsx3.init()
        self.voice.setProperty('rate', self.voice.getProperty('rate') - 10)
        self.animator = Animator(self.background_color, self.pupil_color, self.eye_color,  self.teeth_color, self.tongue_color, self.lips_color, 300, 300)
        

    #Public functions.
    #Translating string to talkingleds.
    def talk(self, input_string):
        _thread.start_new_thread(self.animator.animate_input, (input_string,))
        self.voice.say(input_string)
        self.voice.runAndWait()
        
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
