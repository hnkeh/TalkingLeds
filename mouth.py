from random import randint

class Mouth:
    def __init__(self, mouth_color, background_color, sclera_color):
        #Values.
        self.mouth_color = mouth_color
        self.sclera_color = sclera_color
        self.background_color = background_color
        self.mouth_matris = [[self.background_color for x in range(8)] for y in range(4)]

    #Private functions.
    
    #Adding dots to matris from cordinate-list.
    def _spawn_dots(self, color, cordinates):
        index = 0
        while index < len(cordinates):
            for width in cordinates[index]:
                self.mouth_matris[index][width] = color
            index += 1
                
    #Resets matris to black.
    def _reset_matris(self):
        self.mouth_matris = [[self.background_color for x in range(8)] for y in range(4)]

    #Value settings.
    #Sclera.
    def change_sclera_color(self, new_sclera_color):
        self.sclera_color = new_sclera_color

    #Mouths.
    def change_mouth_color(self, new_mouth_color):
        self.mouth_color = new_mouth_color

    #Background.
    def change_background_color(self, new_background_color):
        self.background_color = new_background_color

    
    #Animation states.
    #Happy mouth.
    def happy(self):
        self._reset_matris()
        dots = [[0, 1, 2, 5, 6, 7], [0, 2, 5, 7], [0, 1, 2, 5, 6, 7]]
        self._spawn_dots(self.mouth_color, dots)
        self._sclera()
        return self.mouth_matris

    #Halfclosed mouths.
    def halfclosed_mouths(self):
        self._reset_matris()
        dots = [[], [0, 2, 5, 7], []]
        self._spawn_dots(self.mouth_color, dots)
        self.sclera()
        return self.mouth_matris

    #Closed mouths.
    def blink(self):
        self._reset_matris()
        dots = [[], [0, 1, 2, 5, 6, 7], []]
        self._spawn_dots(self.mouth_color, dots)
        return self.mouth_matris
    
    #Closed left mouth.
    def left_blink(self):
        self._reset_matris()
        dots = [[5, 6, 7], [0, 1, 2, 5, 7], [5, 6, 7]]
        self._spawn_dots(self.mouth_color, dots)
        self._right_sclera()
        return self.mouth_matris
    
    #Closed right mouth.
    def right_blink(self):
        self._reset_matris()
        dots = [[0, 1, 2], [0, 2, 5, 6, 7], [0, 1, 2]]
        self._spawn_dots(self.mouth_color, dots)
        self._left_sclera()
        return self.mouth_matris
    
    #Happy mouths.
    def happy(self):
        self._reset_matris()
        dots = [[1, 2, 5, 6], [0, 3, 4, 7], []]
        self._spawn_dots(self.mouth_color, dots)

        return self.mouth_matris

    #Get crazy.
    def acid(self):
        self._reset_matris()
        dots = [[0, 1, 2, 5, 6, 7], [0, 2, 5, 7], [0, 1, 2, 5, 6, 7]]
        self._spawn_dots(self.mouth_color, dots)
        self._sclera()
        return self.mouth_matris
        
