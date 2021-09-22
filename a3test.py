""" 
Unit Test for Assignment A3

This module implements several test cases for a3.  It is complete.  You should look 
though this file for places to add tests.

Phil Cipollina(pjc272) and Luke Marcinkiewicz
October 4th, 2017
""" 
import cornell
import a3


def test_complement():
    """
    Test function complement
    """
    cornell.assert_equals(cornell.RGB(255-250, 255-0, 255-71),
                          a3.complement_rgb(cornell.RGB(250, 0, 71)))


def test_round():
    """
    Test function round (a3 version)
    """
    cornell.assert_equals(130.6,   a3.round(130.59,1))
    cornell.assert_equals(130.5,   a3.round(130.54,1))
    cornell.assert_equals(100.0,   a3.round(100,1))
    cornell.assert_equals(100.6,   a3.round(100.55,1))
    cornell.assert_equals(99.57,   a3.round(99.566,2))
    cornell.assert_equals(99.99,   a3.round(99.99,2))
    cornell.assert_equals(100.00,  a3.round(99.995,2))
    cornell.assert_equals(22.00,   a3.round(21.99575,2))
    cornell.assert_equals(21.99,   a3.round(21.994,2))
    cornell.assert_equals(10.01,   a3.round(10.013567,2))
    cornell.assert_equals(10.00,   a3.round(10.000000005,2))
    cornell.assert_equals(10.00,   a3.round(9.9999,3))
    cornell.assert_equals(9.999,   a3.round(9.9993,3))
    cornell.assert_equals(1.355,   a3.round(1.3546,3))
    cornell.assert_equals(1.354,   a3.round(1.3544,3))
    cornell.assert_equals(0.046,   a3.round(.0456,3))
    cornell.assert_equals(0.045,   a3.round(.0453,3))
    cornell.assert_equals(0.006,   a3.round(.0056,3))
    cornell.assert_equals(0.001,   a3.round(.0013,3))
    cornell.assert_equals(0.000,   a3.round(.0004,3))
    cornell.assert_equals(0.001,   a3.round(.0009999,3))
    cornell.assert_equals(1590.0,  a3.round(1593.3, -1))
    cornell.assert_equals(160.00,  a3.round(160, 2))                      
    cornell.assert_equals(22.00,   a3.round(21.99575,2))
    cornell.assert_equals(1.123E2, a3.round(1.12345E2, 1))
    cornell.assert_equals(24.0,    a3.round(23.864,0))
    cornell.assert_equals(8.4648,  a3.round(8.46479254,4))

def test_str5():
    """
    Test function str5
   """
    cornell.assert_equals('130.6',  a3.str5(130.59))
    cornell.assert_equals('130.5',  a3.str5(130.54))
    cornell.assert_equals('100.0',  a3.str5(100))
    cornell.assert_equals('100.6',  a3.str5(100.55))
    cornell.assert_equals('99.57',  a3.str5(99.566))
    cornell.assert_equals('99.99',  a3.str5(99.99))
    cornell.assert_equals('100.0',  a3.str5(99.995))
    cornell.assert_equals('22.00',  a3.str5(21.99575))
    cornell.assert_equals('21.99',  a3.str5(21.994))
    cornell.assert_equals('10.01',  a3.str5(10.013567))
    cornell.assert_equals('10.00',  a3.str5(10.000000005))
    cornell.assert_equals('10.00',  a3.str5(9.9999))
    cornell.assert_equals('9.999',  a3.str5(9.9993))
    cornell.assert_equals('1.355',  a3.str5(1.3546))
    cornell.assert_equals('1.354',  a3.str5(1.3544))
    cornell.assert_equals('0.046',  a3.str5(.0456))
    cornell.assert_equals('0.045',  a3.str5(.0453))
    cornell.assert_equals('0.006',  a3.str5(.0056))
    cornell.assert_equals('0.001',  a3.str5(.0013))
    cornell.assert_equals('0.000',  a3.str5(.0004))
    cornell.assert_equals('0.001',  a3.str5(.0009999))
    cornell.assert_equals('1.000',  a3.str5(1))
    cornell.assert_equals('0.000',  a3.str5(0.00000001))
    cornell.assert_equals('360.0',  a3.str5(359.999999999))


def test_str5_color():
    """
    Test the str5 functions for cmyk and hsv.
    """
    cornell.assert_equals('(98.45, 25.36, 72.80, 1.000)',
                          a3.str5_cmyk(cornell.CMYK(98.448, 25.362, 72.8, 1.0)))
    cornell.assert_equals('(0.000, 0.000, 0.000, 0.000)',
                          a3.str5_cmyk(cornell.CMYK(0.000001,0.00000009,0.0,0)))
    cornell.assert_equals('(22.00, 44.00, 1.000, 100.0)',
                          a3.str5_cmyk(cornell.CMYK(21.999999,44.000001,.99999,
                                                    99.999999)))
    
    # Tests for str5_hsv (add two)
    cornell.assert_equals('(155.0, 0.457, 0.457)',
                          a3.str5_hsv(cornell.HSV(155.04,0.4567,0.45719)))
    cornell.assert_equals('(0.000, 1.000, 1.000)',
                          a3.str5_hsv(cornell.HSV(0.0,.999999999,1.0000000)))

def test_rgb_to_cmyk():
    """
    Test translation function rgb_to_cmyk
    """
    # We use a3.str5 to handle round-off error in comparisons
    rgb = cornell.RGB(255, 255, 255);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornell.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornell.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornell.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornell.assert_equals('0.000', a3.str5(cmyk.black))
    
    rgb = cornell.RGB(0, 0, 0);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornell.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornell.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornell.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornell.assert_equals('100.0', a3.str5(cmyk.black))
        
    rgb = cornell.RGB(217, 43, 164);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornell.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornell.assert_equals('80.18', a3.str5(cmyk.magenta))
    cornell.assert_equals('24.42', a3.str5(cmyk.yellow))
    cornell.assert_equals('14.90', a3.str5(cmyk.black))
    
    rgb = cornell.RGB(100, 150, 125);
    cmyk=a3.rgb_to_cmyk(rgb);
    cornell.assert_equals('33.33', a3.str5(cmyk.cyan))
    cornell.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornell.assert_equals('16.67', a3.str5(cmyk.yellow))
    cornell.assert_equals('41.18', a3.str5(cmyk.black))
    
    rgb = cornell.RGB(0, 72, 186);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornell.assert_equals('100.0', a3.str5(cmyk.cyan))
    cornell.assert_equals('61.29', a3.str5(cmyk.magenta))
    cornell.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornell.assert_equals('27.06', a3.str5(cmyk.black))
    
    
    rgb = cornell.RGB(89, 34, 91);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornell.assert_equals('2.198', a3.str5(cmyk.cyan))
    cornell.assert_equals('62.64', a3.str5(cmyk.magenta))
    cornell.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornell.assert_equals('64.31', a3.str5(cmyk.black))
    
    rgb = cornell.RGB(255, 255, 0);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornell.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornell.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornell.assert_equals('100.0', a3.str5(cmyk.yellow))
    cornell.assert_equals('0.000', a3.str5(cmyk.black))
    
    rgb = cornell.RGB(125, 125, 125);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornell.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornell.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornell.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornell.assert_equals('50.98', a3.str5(cmyk.black))    
    
    
def test_cmyk_to_rgb():
    """
    Test translation function cmyk_to_rgb
    """
    cmyk = cornell.CMYK(0.0,80.18,24.42,14.90)
    rgb = a3.cmyk_to_rgb(cmyk)
    cornell.assert_equals('217',   str(rgb.red))
    cornell.assert_equals('43',    str(rgb.green))
    cornell.assert_equals('164',   str(rgb.blue))
    
    cmyk = cornell.CMYK(100.0,100.0,99.9999,100.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    cornell.assert_equals('0',   str(rgb.red))
    cornell.assert_equals('0',    str(rgb.green))
    cornell.assert_equals('0',   str(rgb.blue))
    
    cmyk = cornell.CMYK(100.0,100.0,100.0,0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    cornell.assert_equals('0',   str(rgb.red))
    cornell.assert_equals('0',    str(rgb.green))
    cornell.assert_equals('0',   str(rgb.blue))
    
    cmyk = cornell.CMYK(0.0,0.0,0.0,0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    cornell.assert_equals('255',   str(rgb.red))
    cornell.assert_equals('255',    str(rgb.green))
    cornell.assert_equals('255',   str(rgb.blue))
    
    
    cmyk = cornell.CMYK(25,25,25,25)
    rgb = a3.cmyk_to_rgb(cmyk)
    cornell.assert_equals('143',   str(rgb.red))
    cornell.assert_equals('143',    str(rgb.green))
    cornell.assert_equals('143',   str(rgb.blue))

def test_rgb_to_hsv():
    """
    Test translation function rgb_to_hsv
    """
    rgb=cornell.RGB(0,0,0)
    hsv=a3.rgb_to_hsv(rgb)
    cornell.assert_equals('0.000',    a3.str5(hsv.hue))
    cornell.assert_equals('0.000',    a3.str5(hsv.saturation))
    cornell.assert_equals('0.000',    a3.str5(hsv.value))
    
    rgb=cornell.RGB(255,255,255)
    hsv=a3.rgb_to_hsv(rgb)
    cornell.assert_equals('0.000',    a3.str5(hsv.hue))
    cornell.assert_equals('0.000',    a3.str5(hsv.saturation))
    cornell.assert_equals('1.000',    a3.str5(hsv.value))
    
    rgb=cornell.RGB(215,150,20)
    hsv=a3.rgb_to_hsv(rgb)
    cornell.assert_equals('40.00',    a3.str5(hsv.hue))
    cornell.assert_equals('0.907',    a3.str5(hsv.saturation))
    cornell.assert_equals('0.843',    a3.str5(hsv.value))
    
    rgb=cornell.RGB(200,30,100)
    hsv=a3.rgb_to_hsv(rgb)
    cornell.assert_equals('335.3',    a3.str5(hsv.hue))
    cornell.assert_equals('0.850',    a3.str5(hsv.saturation))
    cornell.assert_equals('0.784',    a3.str5(hsv.value))
    
    rgb=cornell.RGB(30,220,50)
    hsv=a3.rgb_to_hsv(rgb)
    cornell.assert_equals('126.3',    a3.str5(hsv.hue))
    cornell.assert_equals('0.864',    a3.str5(hsv.saturation))
    cornell.assert_equals('0.863',    a3.str5(hsv.value))
    
    rgb=cornell.RGB(50,150,200)
    hsv=a3.rgb_to_hsv(rgb)
    cornell.assert_equals('200.0',    a3.str5(hsv.hue))
    cornell.assert_equals('0.750',    a3.str5(hsv.saturation))
    cornell.assert_equals('0.784',    a3.str5(hsv.value))
    
    rgb=cornell.RGB(50,150,150)
    hsv=a3.rgb_to_hsv(rgb)
    cornell.assert_equals('180.0',    a3.str5(hsv.hue))
    cornell.assert_equals('0.667',    a3.str5(hsv.saturation))
    cornell.assert_equals('0.588',    a3.str5(hsv.value))
    
    rgb=cornell.RGB(127,127,127)
    hsv=a3.rgb_to_hsv(rgb)
    cornell.assert_equals('0.000',    a3.str5(hsv.hue))
    cornell.assert_equals('0.000',    a3.str5(hsv.saturation))
    cornell.assert_equals('0.498',    a3.str5(hsv.value))


def test_hsv_to_rgb():
    """
    Test translation function hsv_to_rgb
    """
    hsv=cornell.HSV(0,0,0)
    rgb=a3.hsv_to_rgb(hsv)
    cornell.assert_equals('0',        str(rgb.red))
    cornell.assert_equals('0',        str(rgb.green))
    cornell.assert_equals('0',        str(rgb.blue))
    
    
    hsv=cornell.HSV(59.99,0.999,0.999)
    rgb=a3.hsv_to_rgb(hsv)
    cornell.assert_equals('255',        str(rgb.red))
    cornell.assert_equals('255',        str(rgb.green))
    cornell.assert_equals('0',        str(rgb.blue))
    
    hsv=cornell.HSV(75,0.95218,0.23456)
    rgb=a3.hsv_to_rgb(hsv)
    cornell.assert_equals('46',        str(rgb.red))
    cornell.assert_equals('60',        str(rgb.green))
    cornell.assert_equals('3',        str(rgb.blue))
    
    hsv=cornell.HSV(159.9,0.87,0.1)
    rgb=a3.hsv_to_rgb(hsv)
    cornell.assert_equals('3',        str(rgb.red))
    cornell.assert_equals('26',        str(rgb.green))
    cornell.assert_equals('18',        str(rgb.blue))
    
    hsv=cornell.HSV(190,.5,.5)
    rgb=a3.hsv_to_rgb(hsv)
    cornell.assert_equals('64',        str(rgb.red))
    cornell.assert_equals('117',        str(rgb.green))
    cornell.assert_equals('128',        str(rgb.blue))
    
    hsv=cornell.HSV(270.555555,.555555,.5555555)
    rgb=a3.hsv_to_rgb(hsv)
    cornell.assert_equals('103',        str(rgb.red))
    cornell.assert_equals('63',        str(rgb.green))
    cornell.assert_equals('142',        str(rgb.blue))
    
    hsv=cornell.HSV(300,.888,.78009)
    rgb=a3.hsv_to_rgb(hsv)
    cornell.assert_equals('199',        str(rgb.red))
    cornell.assert_equals('22',        str(rgb.green))
    cornell.assert_equals('199',        str(rgb.blue))
    
    hsv=cornell.HSV(359.99999,.75,.25)
    rgb=a3.hsv_to_rgb(hsv)
    cornell.assert_equals('64',        str(rgb.red))
    cornell.assert_equals('16',        str(rgb.green))
    cornell.assert_equals('16',        str(rgb.blue))
    
    
    
# Script Code
# THIS PREVENTS THE TESTS RUNNING ON IMPORT
if __name__ == '__main__':
    test_complement()
    test_round()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsv()
    test_hsv_to_rgb()
    print('Module a3 is working correctly')
