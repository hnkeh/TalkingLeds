#Python imports.
import _thread
from subprocess import call
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

        #Talkingleds main animator.
        self.animator = Animator(self.background_color, self.pupil_color, self.eye_color,  self.teeth_color, self.tongue_color, self.lips_color, 300, 300)

    #Private functions.
    #Converts word to list. Call only works on one word for some reason.
    def _convert_string_to_list(self, input_string):
        output = input_string.split()
        return output

    #Start speaking voice output.
    def _speak(self, input_list):

        _cmd_beg = 'espeak '
        #To dump STD errors.
        _cmd_end = ' 2>/dev/null'
        
        for word in input_list:

            print(word)
            call([_cmd_beg + word + _cmd_end], shell = True)

            #Check for more pauses.
            if "." in word:
                sleep(0.5)
            elif "," in word:
                sleep(0.2)
        
    #Public functions.
    #Translating string into talkingleds.
    def talk(self, input_string):
        #Thread starting.
        try:
            _thread.start_new_thread(self.animator.animate_input, (input_string, ))
            _thread.start_new_thread(self._speak, (self._convert_string_to_list(input_string)), ))
        except as exception:
            print(exception)
            
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
