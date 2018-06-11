#Talkingleds imports.
from images import *

#Eye states.
class Eyes(Images):
    def __init__(self, pupil_color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Values.
        self.pupil_color = pupil_color

    #Value settings.
    #Pupil.
    def change_pupil_color(self, new_pupil_color):
        self.pupil_color = new_pupil_color

    #Private functions.
    #Pupil on.
    def _pupil(self):
        self.matris[1][1] = self.pupil_color
        self.matris[1][6] = self.pupil_color

    def _left_pupil(self):
        self.matris[1][1] = self.pupil_color

    def _right_pupil(self):
        self.matris[1][6] = self.pupil_color

    #Animation states.
    #Opened eyes.
    def open(self):
        self._reset_matris()
        dots = [[0, 1, 2, 5, 6, 7], [0, 2, 5, 7], [0, 1, 2, 5, 6, 7]]
        self._spawn_dots(self.color, dots)
        self._pupil()
        return self.matris

    #Halfclosed eyes.
    def half_closed(self):
        self._reset_matris()
        dots = [[], [0, 2, 5, 7], []]
        self._spawn_dots(self.color, dots)
        self._pupil()
        return self.matris

    #Closed eyes.
    def blink(self):
        self._reset_matris()
        dots = [[], [0, 1, 2, 5, 6, 7], []]
        self._spawn_dots(self.color, dots)
        return self.matris
    
    #Closed left eye.
    def left_blink(self):
        self._reset_matris()
        dots = [[5, 6, 7], [0, 1, 2, 5, 7], [5, 6, 7]]
        self._spawn_dots(self.color, dots)
        self._right_pupil()
        return self.matris
    
    #Closed right eye.
    def right_blink(self):
        self._reset_matris()
        dots = [[0, 1, 2], [0, 2, 5, 6, 7], [0, 1, 2]]
        self._spawn_dots(self.color, dots)
        self._left_pupil()
        return self.matris
    
    #Happy eyes.
    def happy(self):
        self._reset_matris()
        dots = [[1, 2, 5, 6], [0, 3, 4, 7], []]
        self._spawn_dots(self.color, dots)
        return self.matris

    #Get crazy.
    def acid(self):
        self._reset_matris()
        dots = [[0, 1, 2, 5, 6, 7], [0, 2, 5, 7], [0, 1, 2, 5, 6, 7]]
        self._spawn_dots(self.color, dots)
        self._pupil()
        return self.matris
