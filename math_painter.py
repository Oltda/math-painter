from canvas import Canvas
from shapes import Square, Rectangle

'''
data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]


#make a red patch
data[1:, 1:4] = [255, 0, 0]

#make a green patch
data[3:, 2:4] = [0, 255, 0]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')

'''






width_canv = input("Width of canvas: ")
height_canv = input("Height of canvas: ")
color_canvas = input("What color? (black/white)")


platno = Canvas(width=int(width_canv), height=int(height_canv), color=color_canvas)

while True:
    choose_shape = input("What do you want to draw? (square/rectangle) or press q to quit ")


    if choose_shape.lower() == "square":
        x = input("value X: ")
        y = input("value Y: ")
        side = input("side: ")
        red = input("how much red? ")
        green = input("how much green? ")
        blue = input("how much blue? ")
        ctverec = Square(int(x), int(y), int(side), (red, green, blue))
        ctverec.draw(platno)

    if choose_shape.lower() == "rectangle":
        x = input("value X: ")
        y = input("value Y: ")
        width = input("height: ")
        height = input("width: ")
        red = input("how much red? ")
        green = input("how much green? ")
        blue = input("how much blue? ")
        obdelnik = Rectangle(int(x), int(y), int(width), int(height), (red, green, blue))
        obdelnik.draw(platno)

    if choose_shape == "q":
        break
platno.make("obrazek2")








