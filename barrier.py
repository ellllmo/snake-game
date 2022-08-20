from turtle import Turtle
import random

class Barrier(Turtle):

    def __init__(self):
        super().__init__()
        self.barrierlist=[]
        self.make_barrier()


    def make_barrier(self):
        """make barrier for level be hard"""
        self.shape("square")
        self.shapesize(3,3,3)
        self.color("black")
        self.penup()
        self.goto(random.randint(-280,280),random.randint(-270,270))
        self.barrierlist.append(self)

    def reset(self):
        for any in self.barrierlist :
            any.goto(800,800)
        self.barrierlist=[]

    
       
    
        