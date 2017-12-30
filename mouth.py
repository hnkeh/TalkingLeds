from images import *

class Mouth(Images):
    def __init__(self, teeth_color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Values.
        self.teeth_color = teeth_color

    #Value settings.
    #Teeths.
    def change_teeth_color(self, new_teeth_color):
        self.teeth_color = new_teeth_color

    #Private functions.

    #Animation states.
    #Opened mouth.
    def open_mouth(self):
        self._reset_matris()
        dots = [[0, 1, 2, 3, 4, 5, 6, 7], [0, 7], [1, 6], [2, 3, 4, 5]]
        self._spawn_dots(self.color, dots)
        return self.matris
