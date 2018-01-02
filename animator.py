from sense_hat import SenseHat
from time import sleep
from random import randint
from eyes import *
from mouth import *

class Animator():
    def __init__(self, background_color, pupil_color, eye_color,  teeth_color, tongue_color, lips_color, blink_chance, smile_chance):
        #Values.
        self.eyes = Eyes(pupil_color, eye_color, background_color)
        self.mouth = Mouth(teeth_color, tongue_color, lips_color, background_color)
        self.sense = SenseHat()
        self.sense.low_light = True
        
        self.blink_chance = blink_chance
        self.smile_chance = smile_chance
        self.blinked = False
        
    #Private functions.
    #Convert matris to self.sensehat grid.
    def _matris_converter(self, matris):
        output_list = []

        for x in range(8):
            for y in range(8):
                output_list.append(matris[x][y])

        return output_list

    #Idle eye animation.
    def _eye_idle(self):
        lets_roll = randint(0, self.blink_chance)
        if self.blinked:
            self.blinked = not self.blinked
            return self.eyes.open()
        else:
            if lets_roll >= 50:
                return self.eyes.open()
            elif lets_roll >= 25:
                if lets_roll >= 25:
                    return self.eyes.blink()
                elif lets_roll >= 15:
                    return self.eyes.happy()
                elif lets_roll >= 10:
                    return self.eyes.left_blink()
                else:
                    return self.eyes.right_blink()
                self.blinked = not self.blinked
            else:
                self.blinked = not self.blinked
                return self.eyes.half_closed()
            
    #Idle eye animation.
    def _mouth_idle(self):
        lets_roll = randint(0, self.smile_chance)
        if lets_roll >= 50:
            return self.mouth.smile()
        elif lets_roll >= 25:
            return self.mouth.neutral()
        elif lets_roll >= 20:
            return self.mouth.sad()
        elif lets_roll >= 15:
            return self.mouth.s_letter()
        elif lets_roll >= 10:
            return self.mouth.o_letter()
        else:
            return self.mouth.long()
    
    #Public functions.
    #Reset board.
    def reset(self):
        self.sense.set_pixels(_matris_converter(black_matris))

    #Idle animation.
    def idle(self):
        _matris = self._eye_idle() + self._mouth_idle()
        self.sense.set_pixels(self._matris_converter(_matris))

    #Warm animation.
    def warm_anime(self):
        self.sense.set_pixels(self._matris_converter(self.eyes.blink() + self.mouth.warm_0()))
        sleep(0.5) 
        self.sense.set_pixels(self._matris_converter(self.eyes.happy() + self.mouth.warm_1()))
        sleep(0.5)
        self.sense.set_pixels(self._matris_converter(self.eyes.blink() + self.mouth.warm_0()))
        sleep(0.5)
        
    #Animates face to fit letter.
    def read_letter(self):    
        pass
    
    def a(self):
        print('a')

    def b(self):
        print('b')
