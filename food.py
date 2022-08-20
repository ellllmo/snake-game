from turtle import Turtle
import random

# make small green food
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.6,0.6)
        self.color("green")
        self.penup()
        self.goto(random.randint(-270,270),random.randint(-270,270))

    def new(self,barrier): 
        """new location for new food"""
        x_locatin = random.randint(-270,270)
        y_location =random.randint(-270,270)
        if barrier == 0:
            self.goto(x_locatin,y_location)
        else:
            # check the location of foood that not in barrier!
            self.hideturtle()
            self.goto(x_locatin,y_location)
            check=True
            while check:
                change_loc=False
                for every in  (barrier.barrierlist):
                    if self.distance(every) < 40 :
                        x_locatin = random.randint(-270,270)
                        y_location =random.randint(-270,270)
                        change_loc=True
                        break
                if change_loc==False:
                    self.goto(x_locatin,y_location)
                    self.showturtle()
                    check=False



# make big red food
class BigFood(Turtle):
    
    def __init__(self):
        super().__init__()


    def make_big_food(self):
        self.shape("circle")
        self.shapesize(1,1)
        self.color("red")
        self.penup()
        self.goto(random.randint(-270,270),random.randint(-270,270))

    # clear food
    def new(self):
        self.goto(-350,-350)

    # make it blink
    def wink(self,food_size):
        if food_size==True:
            self.shapesize(0.7,0.7)
        else:
            self.shapesize(1,1)
        return not food_size

        