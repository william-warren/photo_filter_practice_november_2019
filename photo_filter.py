import os
from PIL import Image
from random import randint


ORIGINAL_IMAGE_FILENAME = "./assets/domi.jpg"
UPDATED_IMAGE_FILENAME = "./assets/filtered_image.jpg"


def clear_screen():
    """ () -> None
    clears the terminal screen for the user.
    determines what type of os is being used
    and clears the screen accordingly
    """
    if os.name == "nt":
        os.system("cls")        # windows
    else:
        os.system("clear")      # linux / mac


# Applies grey_scale filter to image.

def grey_scale(pixel):
    r, g, b = pixel
    color = (r + g + b) // 3
    return (color, color, color)

# Applies correspond color filter to image.

def red_boi(pixel):
    r, g, b = pixel
    color = (randint(0, 255), g, b)
    return (color, color, color)

def green_boi(pixel):
    r, g, b = pixel
    color = (r, randint(0, 255), b)
    return (color, color, color)

def blue_boi(pixel):
    r, g, b = pixel
    color = (r, g, randint(0, 255))
    return (color, color, color)


def open_image(filename):
    """ (str filename) -> PIL Image object
    opens an image and loads it as a PIL Image object,
    the colors in the image are simplified to 256
    colors to make it easier to manipulate the data,
    and the image is converted to RGB

    the returned Image is a list-like object
    of r, g, b tuples
    """
    image = Image.open(filename)
    image = image.quantize(256).convert("RGB")
    return image


def change_image(image):
    """ (PIL Image object) -> PIL Image object
    deconstructs the current image object into a list of RGB tuples
    and modifies the data to create a new image
    """
    height, width = image.size          # get the current image size
    rgb_list = list(image.getdata())    # create a list of rgb tuples
                                        # modify the rgb data here!
    number = randint(1, 5)
    if number == 1:
        new_data = [(b, g, r) for r, g, b in rgb_list]
    elif number == 2:
        new_data = list(map(red_boi, rgb_list))
    elif number == 3:
        new_data = list(map(grey_scale, rgb_list))
    elif number == 4:
        new_data = list(map(green_boi, rgb_list))
    elif number == 5:
        new_data = list(map(blue_boi, rgb_list))
    # create the new image
    new_image = Image.new("RGB", (height, width))
    new_image.putdata(new_data)
    return new_image


def save_image(image, filename):
    # this function is likely unnecessary,
    # but it is used as an example on
    # how file I/O should be handled in other
    # or similar applications
    """ (PIL Image object, str filename) -> None
    saves the PIL Image object on the machine
    with the string filename
    """
    image.save(filename)
    return None


def main():
    clear_screen()
    print("welcome to the photo editor 📷")
    print("\topening image...")
    image = open_image(ORIGINAL_IMAGE_FILENAME)
    print("\tupdating image...")
    new_image = change_image(image)
    print("\tdisplaying new image...")
    new_image.show()                              # show the new image
    print("\tsaving image...")
    save_image(new_image, UPDATED_IMAGE_FILENAME)
    print("thank you and have a nice day!")


if __name__ == "__main__":
    main()
