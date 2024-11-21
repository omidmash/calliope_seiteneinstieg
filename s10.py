from cpglow import *
makeGlow()
def square():
    repeat 4:
        forward()
        forward()
        right(90)

v = 30
showTrace(False)
setPos(-1, -1)

repeat 4:
    setSpeed(v)
    square()
    v = v + 20