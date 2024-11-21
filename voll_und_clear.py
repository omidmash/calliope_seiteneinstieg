from calliope_mini import *

for y in range(5):
    for x in range(5):
        display.set_pixel(x, y, 9)
        sleep(20)

sleep(1000)
display.clear()