from cpglow import *
makeGlow()
def square():
    repeat 4:
        forward()
        forward()
        left(90)

setSpeed(80)
repeat 4:
    square()
    right(90)