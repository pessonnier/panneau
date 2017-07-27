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

def ledposition(x,y):
  sens = 0 if y % 2 == 0 else 1
  return x + sens * (29 - 2 * x) + y * 30

def t1():
  for ang in range(100):
    for x in range(30):
      for y in range(10):
        strip.setPixelColor(ledposition(x,y),Color(r(ang),v(ang),b(ang)))
    strip.show()
    time.sleep(0.1)

def t2():
  for y in range(10):
    strip.setPixelColor(ledposition(0,y),Color(0,0,128))
    strip.setPixelColor(ledposition(5,y),Color(0,128,0))
    strip.setPixelColor(ledposition(29,y),Color(128,0,0))
  strip.show()

def t3():
  for x in range(30):
    for y in range(10):
      strip.setPixelColor(ledposition(x,y),Color(0,0,128))
    strip.show()
  for x in range(30):
    for y in range(10):
      strip.setPixelColor(ledposition(x,y),Color(0,128,0))
    strip.show()
  for x in range(30):
    for y in range(10):
      strip.setPixelColor(ledposition(x,y),Color(128,0,0))
    strip.show()
  for x in range(30):
    for y in range(10):
      strip.setPixelColor(ledposition(x,y),Color(0,0,0))
    strip.show()

# montre un manque tention dans le dernier tier du panneau
def t4():
  for h in range(256):
    for x in range(30):
      for y in range(10):
        strip.setPixelColor(ledposition(x,y),Color(h,h,h))
    strip.show()

def t5(r,v,b):
  for h in range(256):
    for x in range(30):
      for y in range(10):
        strip.setPixelColor(ledposition(x,y),Color(r*h,v*h,b*h))
    strip.show()

def t6():
  t5(1,0,0)
  t5(0,1,0)
  t5(0,0,1)

alpha={'a' : [[ 0,1,1,0,0 ],
              [ 1,0,0,1,0 ],
              [ 1,1,1,1,0 ],
              [ 1,0,0,1,0 ],
              [ 1,0,0,1,0 ]],
       'b' : [[ 1,1,1,0,0 ],
              [ 1,0,0,1,0 ],
              [ 1,1,1,0,0 ],
              [ 1,0,0,1,0 ],
              [ 1,1,1,0,0 ]],
       ' ' : [[ 0,0,0,0,0 ],
              [ 0,0,0,0,0 ],
              [ 0,0,0,0,0 ],
              [ 0,0,0,0,0 ],
              [ 0,0,0,0,0 ]],
       '0' : [[ 0,1,1,0,0 ],
              [ 1,0,0,1,0 ],
              [ 1,0,0,1,0 ],
              [ 1,0,0,1,0 ],
              [ 0,1,1,0,0 ]],
       '1' : [[ 0,0,1,0,0 ],
              [ 0,1,1,0,0 ],
              [ 0,0,1,0,0 ],
              [ 0,0,1,0,0 ],
              [ 0,1,1,1,0 ]],
       'o' : [[ 0,0,0,0,0 ],
              [ 0,1,1,0,0 ],
              [ 1,0,0,1,0 ],
              [ 1,0,0,1,0 ],
              [ 0,1,1,0,0 ]],
       'z' : [[ 1,1,1,1,0 ],
              [ 0,0,1,0,0 ],
              [ 0,1,0,0,0 ],
              [ 1,0,0,0,0 ],
              [ 1,1,1,1,0 ]]}

def copy(x, y, char):
  for xchar in range(5):
    for ychar in range(5):
      strip.setPixelColor(ledposition(xchar+x, ychar+y), Color(255,255,255) if char[ychar][xchar] == 1 else Color(0,0,0))

def t7():
  copy(0,0, alpha['a'])
  strip.show()
  copy(10,0, alpha['b'])
  strip.show()
  copy(20,0, alpha['a'])
  strip.show()
      
def t8():
  p = 0
  for c in ['b','o','b','1','0','1']:
    copy(p,0, alpha[c])
    p += 5
  strip.show()

if __name__ == '__main__':
  # Create NeoPixel object with appropriate configuration.
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
  strip.begin()
  try:
    while True:
      t8()
  except KeyboardInterrupt:
    off()
