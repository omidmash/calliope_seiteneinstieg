from calliope_mini import *

cardinal = list('ARROW_NW ARROW_NE ARROW_SW ARROW_SE'.split())

for direction in cardinal:
    display.show(getattr(Image, direction))
    sleep(500)
