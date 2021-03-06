""" 
Functions for Assignment A3

This file contains the functions for the assignment.  You should replace the stubs
with your own implementations.

Phil Cipollina(pjc272) and Luke Marcinkiewicz
October 4th, 2017
"""
import cornell
import math


def complement_rgb(rgb):
    """
    Returns: the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    red=255- rgb.red
    green= 255- rgb.green
    blue= 255- rgb.blue
    
    return cornell.RGB(red,green,blue)


def round(number, places):
    """
    Returns: the number rounded to the given number of decimal places.
    
    The value returned is a float.
    
    This function is more stable than the built-in round.  The built-in round
    has weird behavior where round(100.55,1) is 100.5 while round(100.45,1) is
    also 100.5.  We want to ensure that anything ending in a 5 is rounded UP.
    
    It is possible to write this function without the second precondition on
    places. If you want to do that, we leave that as an optional challenge.
    
    Parameter number: the number to round to the given decimal place
    Precondition: number is an int or float
    
    Parameter places: the decimal place to round to
    Precondition: places is an int; 0 <= places <= 3
    """
    # To get the desired output, do the following
    #   1. Shift the number "to the left" so that the position to round to is left of 
    #      the decimal place.  For example, if you are rounding 100.556 to the first 
    #      decimal place, the number becomes 1005.56.  If you are rounding to the second 
    #      decimal place, it becomes 10055.6.  If you are rounding 100.556 to the nearest 
    #      integer, it remains 100.556.
    conv1=number*(10**places)
    #print('conv1 is ' + str(conv1)) 
    #   2. Add 0.5 to this number
    conv2=conv1+0.5
    #print('conv2 is ' + str(conv2)) 
    #   3. Convert the number to an int, cutting it off to the right of the decimal.
    conv3=int(conv2)
    #print('conv3 is ' + str(conv3)) 
    #   4. Shift the number back "to the right" the same amount that you did to the left.
    #      Suppose that in step 1 you converted 100.556 to 1005.56.  In this case, 
    #      divide the number by 10 to put it back.
    conv4=conv3/(10**places)
    #print('conv4 is ' + str(conv4)) 
    return conv4    # Stub


def str5(value):
    """
    Returns: value as a string, but expand or round to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Note:Obviously, you want to use the function round() that you just defined. 
    # However, remember that the rounding takes place at a different place depending 
    # on how big value is. Look at the examples in the specification.
    val = str(value)
    #print(val +'1')
    dec = val.find('.')
    #print(dec)
    length = len(val)
    #print(length)
   
    if length<5 and dec== -1:
        val = round(value,4-length)
        val= str(val)
        
        #print(val+ ' if final')
    else:
        val=round(value, 4-dec)
        val= str(val)
    if len(val)==4:
        val=val+'0'
    if len(val)==3:
        val=val+'00'
    if len(val)==2:
        val=val+'000'    
    
    return val    # Stub


def str5_cmyk(cmyk):
    """
    Returns: String representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    a=str5(cmyk.cyan)
    b=str5(cmyk.magenta)
    c=str5(cmyk.yellow)
    d=str5(cmyk.black)
    return '('+ a +', ' +b+ ', ' +c+', ' +d +')'    # Stub


def str5_hsv(hsv):
    """
    Returns: String representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """
    a=str5(hsv.hue)
    b=str5(hsv.saturation)
    c=str5(hsv.value)
    return '('+ a +', ' +b+ ', ' +c+')'    # Stub


def rgb_to_cmyk(rgb):
    """
    Returns: color rgb in space CMYK, with the most black possible.
    
    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change the RGB numbers to the range 0..1 by dividing them by 255.0.
    nr = rgb.red/255.0
    ng = rgb.green/255.0
    nb = rgb.blue/255.0
    C1 = 1-nr
    Y1 = 1-nb
    M1 = 1-ng
    if C1 == 1 and M1 == 1 and Y1 == 1:
        C = 0
        M = 0
        Y = 0
        K = 1
    else:
        K = min(C1,M1,Y1)
        C = (C1-K)/(1-K)
        M = (M1-K)/(1-K)
        Y = (Y1-K)/(1-K)
    return cornell.CMYK(C*100.0,M*100.0,Y*100.0,K*100.0)  


def cmyk_to_rgb(cmyk):
    """
    Returns : color CMYK in space RGB.
    
    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0.  Deal with them in the 
    # same way as the RGB numbers in rgb_to_cmyk()
    C = cmyk.cyan/100.0
    M = cmyk.magenta/100.0
    Y = cmyk.yellow/100.0
    K = cmyk.black/100.0
    r = (1-C)*(1-K)
    g = (1-M)*(1-K)
    b = (1-Y)*(1-K)
    R = int(round(r*255.0,0))
    G = int(round(g*255.0,0))
    B = int(round(b*255.0,0))
    return cornell.RGB(R,G,B)


def rgb_to_hsv(rgb):
    """
    Return: color rgb in HSV color space.
    
    Formulae from wikipedia.org/wiki/HSV_color_space.
   
    Parameter rgb: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    R=rgb.red/255.0
    G=rgb.green/255.0
    B=rgb.blue/255.0
    MAX=max(R,G,B)
    MIN=min(R,G,B)
    if MAX==MIN:
        H=0
    elif MAX==R and G>=B:
        H=60.0*(G-B)/(MAX-MIN)
    elif MAX==R and G<B:
        H=60.0*(G-B)/(MAX-MIN) + 360.0
    elif MAX==G:
        H= 60*(B-R)/(MAX-MIN) + 120.0
    elif MAX==B:
        H = 60*(R-G)/(MAX-MIN) + 240.0
    if MAX==0:
        S=0
    else:
        S=1-(MIN/MAX)
    V=MAX
    return cornell.HSV(H,S,V)  # Stub


def hsv_to_rgb(hsv):
    """
    Returns: color in RGB color space.
    
    Formulae from http://en.wikipedia.org/wiki/HSV_color_space.
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """
    H=hsv.hue
    S=hsv.saturation
    V=hsv.value
    Hi=math.floor(H/60)
    f = H/60 - Hi
    p = V*(1-S)
    q = V*(1-f*S)
    t = V*(1-(1-f)*S)
    if Hi==0:
        R=V
        G=t
        B=p
    elif Hi==1:
        R=q
        G=V
        B=p
    elif Hi==2:
        R=p
        G=V
        B=t
    elif Hi==3:
        R=p
        G=q
        B=V
    elif Hi==4:
        R=t
        G=p
        B=V
    elif Hi==5:
        R=V
        G=p
        B=q
    R=round(R*255.0,0)
    G=round(G*255.0,0)
    B=round(B*255.0,0)
    
    return cornell.RGB(int(R),int(G),int(B))  # Stub
