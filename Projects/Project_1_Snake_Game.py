from DLL import DoublyLinkedList
from random import randint
import dudraw

class Game:
    def draw(self):
        dudraw.filled_square(self.x_pos, self.y_pos, self.size)
class Food(Game):
    def __init__(self, x_pos:int, y_pos:int):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = 1

x_scale = 10
y_scale = 10
dudraw.set_x_scale(0, x_scale)
dudraw.set_y_scale(0, y_scale)
dudraw.set_canvas_size(400, 400)

limit = 20 #number of frames to allow to pass before snake moves
timer = 0  #a timer to keep track of number of frames that passed
while True:
    timer += 1
    #process keyboard press here
    key = dudraw.next_key()
    if timer == limit:
        timer = 0

        # fruit = Food((randint(0, x_scale)), (randint(0, y_scale)))
        fruit = Food(randint(1, x_scale - 1), randint(1, y_scale - 1))
        fruit.draw()
        #draw and move the snake
        #check to see if snake ate the fruit
        #check if the snake self intersects

    dudraw.show(40)