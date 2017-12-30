from images import *

class Eyes():
    def __init__(self, eye_color, background_color, sclera_color):
        #Values.
        self.eye_color = eye_color
        self.sclera_color = sclera_color
        self.background_color = background_color
        self.eye_matris = [[self.background_color for x in range(8)] for y in range(4)]

    #Private functions.
    #Sclera on.
    def _sclera(self):
        self.eye_matris[1][1] = [255,255,255]
        self.eye_matris[1][6] = [255,255,255]

    def _left_sclera(self):
        self.eye_matris[1][1] = [255,255,255]

    def _right_sclera(self):
        self.eye_matris[1][6] = [255,255,255]

    #Adding dots to matris from cordinate-list.
    def _spawn_dots(self, color, cordinates):
        index = 0
        while index < len(cordinates):
            for width in cordinates[index]:
                self.eye_matris[index][width] = color
            index += 1
                
    #Resets matris to black.
    def _reset_matris(self):
        self.eye_matris = [[self.background_color for x in range(8)] for y in range(4)]

    #Value settings.
    #Sclera.
    def change_sclera_color(self, new_sclera_color):
        self.sclera_color = new_sclera_color

    #Eyes.
    def change_eye_color(self, new_eye_color):
        self.eye_color = new_eye_color

    #Background.
    def change_background_color(self, new_background_color):
        self.background_color = new_background_color

    
    #Animation states.
    #Opened eyes.
    def open_eyes(self):
        self._reset_matris()
        dots = [[0, 1, 2, 5, 6, 7], [0, 2, 5, 7], [0, 1, 2, 5, 6, 7]]
        self._spawn_dots(self.eye_color, dots)
        self._sclera()
        return self.eye_matris

    #Halfclosed eyes.
    def halfclosed_eyes(self):
        self._reset_matris()
        dots = [[], [0, 2, 5, 7], []]
        self._spawn_dots(self.eye_color, dots)
        self.sclera()
        return self.eye_matris

    #Closed eyes.
    def blink(self):
        self._reset_matris()
        dots = [[], [0, 1, 2, 5, 6, 7], []]
        self._spawn_dots(self.eye_color, dots)
        return self.eye_matris
    
    #Closed left eye.
    def left_blink(self):
        self._reset_matris()
        dots = [[5, 6, 7], [0, 1, 2, 5, 7], [5, 6, 7]]
        self._spawn_dots(self.eye_color, dots)
        self._right_sclera()
        return self.eye_matris
    
    #Closed right eye.
    def right_blink(self):
        self._reset_matris()
        dots = [[0, 1, 2], [0, 2, 5, 6, 7], [0, 1, 2]]
        self._spawn_dots(self.eye_color, dots)
        self._left_sclera()
        return self.eye_matris
    
    #Happy eyes.
    def happy(self):
        self._reset_matris()
        dots = [[1, 2, 5, 6], [0, 3, 4, 7], []]
        self._spawn_dots(self.eye_color, dots)

        return self.eye_matris

    #Get crazy.
    def acid(self):
        self._reset_matris()
        dots = [[0, 1, 2, 5, 6, 7], [0, 2, 5, 7], [0, 1, 2, 5, 6, 7]]
        self._spawn_dots(self.eye_color, dots)
        self._sclera()
        return self.eye_matris
        
