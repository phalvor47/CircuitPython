import board #pylint: disable=import-error
import time #pylint: disable=import-error
import pulseio #pylint: disable=import-error
from digitalio import DigitalInOut, Direction, Pull #pylint: disable=import-error



class RGB(object):
    def __init__(self, r, g, b):
        self.r = DigitalInOut(r)
        self.r.direction = Direction.OUTPUT
        self.g = DigitalInOut(g)
        self.g.direction = Direction.OUTPUT
        self.b = DigitalInOut(b)
        self.b.direction = Direction.OUTPUT
    def red(self):
        self.r.value = False
        self.g.value = True
        self.b.value = True
    def green(self):
        self.g.value = False
        self.b.value = True
        self.r.value = True
    def blue(self):
        self.b.value = False
        self.g.value = True
        self.r.value = True
    def cyan(self):
        self.g.value = False
        self.b.value = False
        self.r.value = True
    def magenta(self):
        self.r.value = False
        self.b.value = False
        self.g.value = True
    def yellow(self):
        self.b.value = True
        self.g.value = False
        self.r.value = False