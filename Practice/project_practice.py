import dudraw

dudraw.set_canvas_size(400, 400)
x = 0
y = 0
r = 0.05
c = 255
while True:
    dudraw.set_pen_color_rgb(0, 0, c)
    if x + r > 1 or x - r < 0:
        y += 0.1
        x -= 0.1
    else:
        dudraw.filled_square(x + r, y + r, r)
        x += 0.1
        c -= 1
        dudraw.show(100)
