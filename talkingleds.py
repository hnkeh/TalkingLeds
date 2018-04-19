#Python imports.
import pyttsx3
import _thread
from time import sleep
from random import randint

#Talkingleds imports.
from animator import *
from colors import *

#Main class.
class TalkingLeds():
    def __init__(self):
        #Standard values.
        self.background_color = black
        self.eye_color = red
        self.pupil_color = white
        self.lips_color = red
        self.teeth_color = white
        self.tongue_color = pink
        self.idle_timer = 0.5
        self.warm_chance = 100

        #Pyttsx3 values.
        self.voice = pyttsx3.init()
        self.voice.setProperty('rate', self.voice.getProperty('rate') - 10)

        #Talkingleds main animator.
        self.animator = Animator(self.background_color, self.pupil_color, self.eye_color,  self.teeth_color, self.tongue_color, self.lips_color, 300, 300)

    #Public functions.
    #Translating string into talkingleds.
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
            sleep(self.idle_timer)
