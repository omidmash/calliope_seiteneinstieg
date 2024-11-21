# from cpglow import *
#
# makeGlow()
#
# setSpeed(90)
# showTrace(False)
# a = 0
# while a <= 360:
#     forward()
#     forward()
#     back()
#     back()
#     left(45)
#     a = a + 45
#

from cpglow import *

makeGlow()

def square():
    repeat 4:
        forward()
        forward()
        left(90)

clear()
setSpeed(90)
showTrace(False)
setPos(2, 0)
left(45)
while True:
    square()