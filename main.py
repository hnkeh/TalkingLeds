from sense_hat import SenseHat
from time import sleep
from eyes import *
from mouth import *

sense = SenseHat()
sense.low_light = True

black = [0, 0, 0]
white = [255, 255, 255]
green = [0, 255, 0]
red = [255, 0, 0]

black_matris = [[black for x in range(8)] for y in range(8)]

#Private functions.
#Convert matris to sensehat grid.
def _matris_converter(matris):
    output_list = []

    for x in range(8):
        for y in range(8):
            output_list.append(matris[x][y])

    return output_list

def main():
    eyes = Eyes(white, red, black)
    mouth = Mouth(white, red, black)

    while True:
        spiral_matris = eyes.open_eyes() + mouth.open_mouth()
        sense.set_pixels(_matris_converter(spiral_matris))
        sleep(30)
        black_matris = [[black for x in range(8)] for y in range(4)]
        spiral_matris = eyes.blink() + black_matris
        sense.set_pixels(_matris_converter(spiral_matris))
        sleep(0.4)
        black_matris = [[black for x in range(8)] for y in range(4)]
        spiral_matris = eyes.open_eyes() + black_matris
        sense.set_pixels(_matris_converter(spiral_matris))
        sleep(3)
        black_matris = [[black for x in range(8)] for y in range(4)]
        spiral_matris = eyes.blink() + black_matris
        sense.set_pixels(_matris_converter(spiral_matris))
        sleep(0.1)
        index = 0
        while index < 3:
            black_matris = [[black for x in range(8)] for y in range(4)]
            spiral_matris = eyes.happy() + black_matris
            sense.set_pixels(_matris_converter(spiral_matris))
            sleep(0.5)
            black_matris = [[black for x in range(8)] for y in range(4)]
            spiral_matris = eyes.blink() + black_matris
            sense.set_pixels(_matris_converter(spiral_matris))
            sleep(0.5)
            index += 1
        black_matris = [[black for x in range(8)] for y in range(4)]
        spiral_matris = eyes.open_eyes() + black_matris
        sense.set_pixels(_matris_converter(spiral_matris))
        sleep(2)
        index = 0
        while index < 3:
            black_matris = [[black for x in range(8)] for y in range(4)]
            spiral_matris = eyes.left_blink() + black_matris
            sense.set_pixels(_matris_converter(spiral_matris))
            sleep(0.5)
            black_matris = [[black for x in range(8)] for y in range(4)]
            spiral_matris = eyes.open_eyes() + black_matris
            sense.set_pixels(_matris_converter(spiral_matris))
            sleep(2)
            black_matris = [[black for x in range(8)] for y in range(4)]
            spiral_matris = eyes.right_blink() + black_matris
            sense.set_pixels(_matris_converter(spiral_matris))
            sleep(0.5)
            black_matris = [[black for x in range(8)] for y in range(4)]
            spiral_matris = eyes.open_eyes() + black_matris
            sense.set_pixels(_matris_converter(spiral_matris))
            sleep(2)
            index += 1
