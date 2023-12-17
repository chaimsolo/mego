from random import randint
class Color:

    def __init__(self):
        self.rgb = []
        for i in range(3):
            self.color = randint(1, 255)
            self.rgb.append(self.color)
        self.rgb = tuple(self.rgb)