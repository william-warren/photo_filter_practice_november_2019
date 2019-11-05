import os
from PIL import Image


ORIGINAL_IMAGE_FILENAME = './assets/domi.jpg'


def clear_screen():
    ''' () -> None
    clears the terminal screen for the user.
    determines what type of os is being used
    and clears the screen accordingly
    '''
    if os.name == 'nt':
        os.system('cls')  # windows
    else:
        os.system('clear')  # linux / mac


def open_image(filename):
    ''' (str filename) -> PIL Image object
    opens an image and loads it as a PIL Image object,
    the colors in the image are simplified to 256
    colors to make it easier to manipulate the data,
    and the image is converted to RGB

    the returned Image is a list-like object
    of r, g, b tuples
    '''
    image = Image.open(filename)
    image = image.quantize(256).convert('RGB')
    return image


def main():
    clear_screen()
    print('welcome to the photo editor 📷')
    image = open_image(ORIGINAL_IMAGE_FILENAME)


if __name__ == '__main__':
    main()
