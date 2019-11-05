from PIL import Image

ORIGINAL_IMAGE_FILENAME = './assets/domi.jpg'


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
    image = open_image(ORIGINAL_IMAGE_FILENAME)


if __name__ == '__main__':
    main()
