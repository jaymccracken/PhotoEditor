""" SYSC 1005 A Fall 2017.

Filters for a photo-editing application.
"""

from Cimpl import *

def grayscale(image,height):
    """ (Cimpl.Image) -> None
    
    Convert image into shades of gray based on the brightness
    of the 3 rgb values.
    
    >>> image = load_image(choose_file()) 
    >>> grayscale(image)
    >>> show(image)    
    """
    black = create_color(0,0,0)
    for  x, y, (r, g, b) in image:

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)
        set_color(image, x, y, gray)

            
        
def weighted_grayscale(image):
    """ (Cimpl.Image) -> None
    
    Convert image into shades of gray based on the brightness
    of the 3 rgb values however the values are weighted.
    
    >>> image = load_image(choose_file()) 
    >>> grayscale(image)
    >>> show(image)    
    """
    for  x, y, (r, g, b) in image:

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = r * 0.299 + g * 0.587 + b * 0.114
        gray = create_color(brightness, brightness, brightness)
        set_color(image, x, y, gray)


def solarize(image, threshold):
    """ (Cimpl.Image, int) -> None
    
    Solarize image, modifying the RGB components that
    have intensities that are less than threshold.
    Parameter threshold is in the range 0 to 256, inclusive.
    
    >>> image = load_image(choose_file()) 
    >>> solarize(image)
    >>> show(image)     
    """
    for x, y, (red, green, blue) in image:

        # Invert the values of all RGB components that are less than 128,
        # leaving components with higher values unchanged.

        if red < threshold:
            red = 255 - red

        if green < threshold:
            green = 255 - green

        if blue < threshold:
            blue = 255 - blue

        solarized = create_color(red, green, blue)
        set_color(image, x, y, solarized)


def black_and_white(image):
    """ (Cimpl.Image) -> None
    
    Convert image to a black-and-white (two-tone) image.
    
    >>> image = load_image(choose_file()) 
    >>> black_and_white(image)
    >>> show(image)     
    """
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on 
    # whether its brightness is in the lower or upper half of this range.       

    for x, y, (red, green, blue) in image:
        brightness = (red + green + blue) // 3      
        
        if brightness < 128:
            set_color(image, x, y, black)
        else:     # brightness is between 128 and 255, inclusive
            set_color(image, x, y, white)


def black_and_white_and_gray(image):
    """ (Cimpl.Image) -> None
    
    Convert image to a black-and-white-and-gray (three-tone) image.
    
    >>> image = load_image(choose_file()) 
    >>> black_and_white_and_gray(image)
    >>> show(image)     
    """
    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255. Change the colours of
    # pixels whose brightness is in the lower third of this range to black,
    # in the upper third to white, and in the middle third to medium-gray.

    for x, y, (red, green, blue) in image:      
        brightness = (red + green + blue) // 3

        if brightness < 85:
            set_color(image, x, y, black)
        elif brightness < 171: # brightness is between 85 and 170, inclusive
            set_color(image, x, y, gray)
        else:                  # brightness is between 171 and 255, inclusive
            set_color(image, x, y, white)
         
            
def negative(image):
    """ (cimpl.image) -> none
    
    Creating a negative replication of the picture
    minusing the value of the componet from 255
    
    >>> image = load_image(choose_file()) 
    >>> negative(image)
    >>> show(image)     
    """
    for x, y, ( r, g, b) in image:
        new_color = create_color(255 - r, 255 - g, 255 - b)
        set_color(image,x,y,new_color)
        
        
def extreme_contrast(image):
    """ (Cimpl.Image) -> None
    
    Modify image, maximizing the contrast between the light
    and dark pixels.
    
    >>> image = load_image(choose_file())
    >>> extreme_contrast(image)
    >>> show(image)
    """
    for x, y, ( r, g, b) in image:
        if r < 127:
            r = 0
        else: r = 255
        
        if g < 127:
            g = 0
        else: g = 255
        
        if b < 127:
            b = 0
        else: b = 255
        
        color = create_color( r, g, b)
        set_color( image, x, y, color)
        
        
def sepia_tint(image):
    """ (Cimpl.Image) -> None
    
    Convert image given to sepia tones.
    
    >>> image = load_image(choose_file())
    >>> sepia_tint(image)
    >>> show(image)
    """
    grayscale(image)

    for x, y, ( r, g, b) in image:
        if b < 63:
            b = b * 0.9
            r = r * 1.1
        elif b > 63 and b < 191:
            b = b * 0.85
            r = r * 1.15
        else:
            b = b * 0.93
            r = r * 1.08    
            
        color = create_color( r, g, b)
        set_color(image, x, y, color)
        
        
def adjust_component(amount):
    """ (int) -> int
    
    Divide the range 0..255 into 4 equal-size quadrants,
    and return the midpoint of the quadrant in which the
    specified amount lies.
    
    >>> _adjust_component(10)
    31
    >>> _adjust_component(85)
    95
    >>> _adjust_component(142)
    159
    >>> _adjust_component(230)
    223
    """
    if amount < 63:
        return 31
    elif 64 < amount < 127:
        return 95
    elif 128 < amount < 191:
        return 159
    else: 
        return 223
    
    
def posterize(img):
    """ (Cimpl.Image) -> None
    
    "Posterize" the specified image.
    
    >>> image = load_image(choose_file())
    >>> posterize(image)
    >>> show(image)
    """
    
    for x, y, ( r, g, b) in image:
        r = adjust_component(r)
        g = adjust_component(g)
        b = adjust_component(b)
        
        color = create_color( r, g, b)
        set_color( image, x, y, color)
    
    
def blur(source):
    """ (Cimpl.Image) -> Cimpl.Image 
    
    Return a new image that is a blurred copy of source. 
    
    >>>original = load_image(choose_file())
    >>>blurred = blur(original)
    >>>show(original)
    >>>show(blurred)    
    """

    # We modify a copy of the original image, because we don't want blurred
    # pixels to affect the blurring of subsequent pixels.
    
    target = copy(source)
    
    # Recall that the x coordinates of an image's pixels range from 0 to
    # get_width() - 1, inclusive, and the y coordinates range from 0 to
    # get_height() - 1.
    #
    # To blur the pixel at location (x, y), we use that pixel's RGB components,
    # as well as the components from the four neighbouring pixels located at
    # coordinates (x - 1, y), (x + 1, y), (x, y - 1) and (x, y + 1).
    #
    # When generating the pixel coordinates, we have to ensure that (x, y)
    # is never the location of pixel on the top, bottom, left or right edges
    # of the image, because those pixels don't have four neighbours.
    #
    # As such, we can't use this loop to generate the x and y coordinates:
    #
    # for y in range(0, get_height(source)):
    #     for x in range(0, get_width(source)):
    #
    # With this loop, when x or y is 0, subtracting 1 from x or y yields -1, 
    # which is not a valid coordinate. Similarly, when x equals get_width() - 1 
    # or y equals get_height() - 1, adding 1 to x or y yields a coordinate that
    # is too large.
    
    for y in range(1, get_height(source) - 1):
        for x in range(1, get_width(source) - 1):

            # Grab the pixel @ (x, y) and its four neighbours
            top_red, top_green, top_blue = get_color(source, x, y - 1)
            left_red, left_green, left_blue = get_color(source, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(source, x, y + 1)
            right_red, right_green, right_blue = get_color(source, x + 1, y)
            center_red, center_green, center_blue = get_color(source, x, y)
            rightTop_red, rightTop_green, rightTop_blue = get_color(source, x + 1, y - 1)
            rightBot_red, rightBot_green, rightBot_blue = get_color(source, x + 1, y + 1)
            leftTop_red, leftTop_green, leftTop_blue = get_color(source, x - 1, y - 1)
            leftBot_red, leftBot_green, leftBot_blue = get_color(source, x - 1, y + 1)

            # Average the red components of the five pixels
            new_red = (top_red + left_red + bottom_red + right_red + center_red + rightTop_red + rightBot_red + leftTop_red + leftBot_red) // 9

            # Average the green components of the five pixels
            new_green = (top_green + left_green + bottom_green + right_green + center_green + rightTop_green + rightBot_green + leftTop_green + leftBot_green) // 9

            # Average the blue components of the five pixels
            new_blue = (top_blue + left_blue + bottom_blue + right_blue + center_blue + rightTop_blue + rightBot_blue + leftTop_blue + leftBot_blue) // 9

            new_color = create_color(new_red, new_green, new_blue)
            
            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)

    return target


def detect_edges(image, threshold):
    """ (Cimpl.Image, float) -> None
    
    Takes the brightness of the pixel and the pixel below it, 
    subtracts them to create a value contrast, when the value
    is greater then the threshold the pixel will be set to black
    else it will be white.
    
    >>> image = load_image(choose_file())
    >>> detect_edges(image, 10.0)
    >>> show(image)
    """
    black = create_color(0,0,0)
    white = create_color(255,255,255)
    
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):    
           
            top_red, top_green, top_blue = get_color(image, x, y)
            brightnessTop = (top_red + top_green + top_blue) / 3
            
            bot_red, bot_green, bot_blue = get_color(image, x, y +1)
            brightnessBot = (bot_red + bot_green + bot_blue) / 3            
            
            contrast = abs(brightnessTop - brightnessBot)
            
            if contrast > threshold:
                set_color(image, x, y, white)
            else:
                set_color(image, x, y, black)                
         
                
def detect_edges_better(image, threshold):
    """ (Cimpl.Image, float) -> None
    
    Takes the brightness of the pixel and the pixel below it, 
    subtracts them to create a value contrast and gets value for the pixel 
    and the pixel to the right, when either of the values
    are greater then the threshold the pixel will be set to black
    else it will be white.
    
    >>> image = load_image(choose_file())
    >>> detect_edges(image, 10.0)
    >>> show(image)
    """
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):    
            
            top_red, top_green, top_blue = get_color(image, x, y)
            brightnessTop = (top_red + top_green + top_blue) / 3
            
            bot_red, bot_green, bot_blue = get_color(image, x, y + 1)
            brightnessBot = (bot_red + bot_green + bot_blue) / 3    
            
            right_red, right_green, right_blue = get_color(image, x + 1, y)
            brightnessRight = (right_red + right_green + right_blue) / 3                
            
            contrastVert = abs(brightnessTop - brightnessBot)
            contrastHor = abs(brightnessTop - brightnessRight)
            
            if contrastVert > threshold or contrastHor > threshold:
                set_color(image, x, y, black)
            else:
                set_color(image, x, y, white)     
                

def gray_region(img):
    height = get_height(img)
    width = get_width(img)

    for y in range(height // 4, 3*height//4 -1):
        for x in range(width//4, 3*width//4 -1):
            r, g, b = get_color (img,x,y)
            bright = (r + g + b)//3
                
            set_color(img, x, y,(bright,bright,bright))