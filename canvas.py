
import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width

        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        if self.color == "white":
            self.data[:] = [255, 255, 255]
        elif self.color == "black":
            self.data[:] = [0, 0, 0]



    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(f'{imagepath}.png')
