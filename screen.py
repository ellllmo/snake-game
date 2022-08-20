from re import S
from turtle import Screen , Turtle
import time

# bgcolor for level up
color=["black","Darkorange2","aquamarine3","DarkOrchid4","burlywood3","DarkRed","Darksalmon","DarkGray","palegreen","plum"]

class MyScreen():

    def __init__(self):
        self.myscreen=Screen()
        self.myscreen.setup(width=600, height=600 )
        self.myscreen.bgcolor("black")
        self.myscreen.title("SNAKE GAME")
        self.myscreen.tracer(0)
    

    def listen(self,snake):
        self.myscreen.listen()
        self.myscreen.onkey(snake.up,"Up")
        self.myscreen.onkey(snake.down,"Down")
        self.myscreen.onkey(snake.left,"Left")
        self.myscreen.onkey(snake.right,"Right")


    # when you eat food and must be increase your size it must be update
    def update(self):
        self.myscreen.update()
        time.sleep(0.09)


    def change(self,level):
        """we are in next leve so want change backgrand color"""
        self.myscreen.bgcolor(color[level])
            

    def new_level(self):
        """write in screen next level"""
        show_level=Turtle()
        show_level.penup()
        show_level.hideturtle()
        show_level.goto(0,0)
        show_level.color("DarkGoldenrod1")
        show_level.write("NEW LEVEL",align="center",font=('Amaranth',32,'normal'))
        time.sleep(1)
        show_level.clear()

    def reset(self):
        self.myscreen.bgcolor(color[0])


    def exit(self):
        self.myscreen.exitonclick()
