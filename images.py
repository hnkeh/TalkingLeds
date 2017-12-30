class Images():
    def __init__(self, color, background_color):
        #Values.
        self.color = color
        self.background_color = background_color
        self.matris = [[self.background_color for x in range(8)] for y in range(4)]

    #Value settings.
    #Maincolor.
    def change_color(self, color):
        self.color = color

    #Background.
    def change_background_color(self, new_background_color):
        self.background_color = new_background_color

    #Private functions.    
    #Adding dots to matris from cordinate-list.
    def _spawn_dots(self, color, cordinates):
        index = 0
        while index < len(cordinates):
            for width in cordinates[index]:
                self.matris[index][width] = color
            index += 1
                
    #Resets matris to black.
    def _reset_matris(self):
        self.matris = [[self.background_color for x in range(8)] for y in range(4)]
