import time
import turtle
window = turtle.Screen()
tim=turtle.Turtle()
tim.speed(100)

def grid():
    for x in range (2):
        tim.left(90)
        tim.forward(100)
        tim.left(90)
        tim.forward(100)
        for x in range(4):
            tim.forward(100)
            for x in range(4):
                tim.right(90)
                tim.forward(200)
                for x in range(4):
                    tim.right(90)
                    tim.forward(100)
                    

                    


