"""
File: practice_image.py
This file is an opportunity to practice the basics related to loading an image
in a Python file and converting the image to an object for the purposes
of manipulation. Fun times.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/henry-sweetness.jpg'

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before the transform
    image.show()

    # Apply the filter
    for pixel in image:
        pixel.red *= 1.5
        pixel.green *= 0.7
        pixel.blue *= 1.5

    # Show the image after the transform
    image.show()

def get_file():
    # Read image file path from user, or use the default file
    filename = input("Enter the image file (or press enter for default): ")
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()