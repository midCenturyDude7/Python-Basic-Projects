"""
File: henry_warhol.py
This program will generate the Warhol effect based on the original image in the
practice_image.py file
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 525
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/henry-sweetness-v2.jpg'


def main():
    
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    for row in range(N_ROWS):
        for col in range(N_COLS):
            patch = make_recolored_patch(1, 1.75*row, 1.75*col)
            final_image = make_last_image(patch, final_image, row, col)

    final_image.show()

def make_recolored_patch(red_scale, green_scale, blue_scale):
    
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch

def make_last_image(image, final_image, row, col):

    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            final_image.set_pixel(x + (col) * PATCH_SIZE, y + (row) * PATCH_SIZE, pixel)
    return final_image


if __name__ == '__main__':
    main()