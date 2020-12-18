from vec import Vector

class Ray():
    def __init__(self, origin, direction):
        self.origin, self.direction = origin, direction

    def at(self, t):
        return self.origin + self.direction*t;

