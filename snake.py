from turtle import Turtle
from food import Food

class Snake():

    # make 3 segment for snake
    def __init__(self):
        self.snake=[]
        for q in range (3):
            newsnake=Turtle()
            newsnake.shape("square")
            newsnake.penup()
            newsnake.color("white")
            newsnake.goto((q*-20,0))
            self.snake.append(newsnake)
    

    def add(self):
        """add segment when eat food"""
        newsnake=Turtle()
        newsnake.shape("square")
        newsnake.penup()
        newsnake.color("white")
        newsnake.goto(((self.snake[-1].xcor())-20,(self.snake[-1].ycor())))
        self.snake.append(newsnake)
    


    def move(self):
        """keep moving"""
        for q in range (len(self.snake)-1,0,-1):
            self.snake[q].goto(self.snake[q-1].xcor(),self.snake[q-1].ycor())
            # the segment follow front segment

        self.snake[0].forward(20)

# for change direction and check that if you are keep moving north cant go sourth..
    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)


    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)


    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)


    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def reset(self):
        for q in (self.snake):
            q.clear()
            q.hideturtle()
        self.__init__()