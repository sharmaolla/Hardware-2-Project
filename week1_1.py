import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C


SW0 = Pin(9, pull=Pin.PULL_UP, mode=Pin.IN)
SW2 = Pin(7, pull=Pin.PULL_UP, mode=Pin.IN)


i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)
oled.fill(0)

x = 51
y = 55
z = 1
x_max = 127-8*3
oled.text('<=>', x, y, 1)
oled.show()


while True:
     if SW0.value() == 0:
         if x <= x_max:
            x += 1
            #time.sleep(0.05)
            oled.fill(0)
            oled.text('<=>',x , y, 1)
            z += 1
          
     elif SW2.value() == 0:
         if x >= 0:
            x -= 1
            #time.sleep(0.05)
            oled.fill(0)
            oled.text('<=>',x , y, 1)
            z += 1
            
     if z % 8 == 0:
        z =1
        oled.show()
        
        




