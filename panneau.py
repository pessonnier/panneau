import time
import math
from neopixel import *

# LED strip configuration:
LED_COUNT      = 300      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

def off():
  for i in range(LED_COUNT):
    strip.setPixelColor(i,Color(0,0,0))
  strip.show()

def r(a):
  return int(math.fabs(math.sin(a/100*6.83)*128))

def v(a):
  return int(math.fabs(math.sin((a+33)/100*6.83)*128))

def b(a):
  return int(math.fabs(math.sin((a+66)/100*6.83)*128))

def t1():
  for ang in range(100):
    for x in range(30):
      for y in range(10):
        strip.setPixelColor(x+y*30,Color(r(ang),v(ang),b(ang)))
    strip.show()
    time.sleep(0.1)

if __name__ == '__main__':
  # Create NeoPixel object with appropriate configuration.
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
  strip.begin()
  try:
    while True:
      t1()
  except:
    off()
