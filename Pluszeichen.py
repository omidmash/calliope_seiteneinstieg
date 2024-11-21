from cpglow import *

makeGlow()

setSpeed(80)


def cross():
    setPos(-2, 0)
    right(90)
    repeat
    4:
    forward()


setPos(0, -2)
left(90)
repeat
4:
forward()

cross()