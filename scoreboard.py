from time import sleep
from turtle import Turtle

class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.score=0
        self.change_level=True
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write("Score= 0",align="center",font=('Comic Sans MS',20,'normal'))
        

    def updete_score(self):
        """increase score after eat food"""
        self.score+=1
        if self.score % 5 == 4 :
            self.change_level=True
        self.clear()
        self.write("Score= "+str(self.score),align="center",font=('Comic Sans MS',20,'normal'))

    
    def game_over(self):
        """write game over"""
        self.goto(0,0)
        self.color("white")
        self.write("GAME OVER",align="center",font=('Apple Chancery',38,'underline'))
        self.clear()
        sleep(1)


    def reset(self):
        self.clear()
        self.__init__()

class Highscore(Turtle):
        

    def __init__(self):
        global file
        super().__init__()
        with open("highscore.txt") as file:
            self.highscore=int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,-270)
        self.write(f"HighScore= {self.highscore}",align="center",font=('Comic Sans MS',20,'normal'))


    def updete_highscore(self,score):
        """increase highscore after eat food"""
        if score > self.highscore :
            self.highscore=score
            with open("highscore.txt",mode="w") as file:
                file.write(str(score))
        self.clear()
        self.write("HighScore= "+str(self.highscore),align="center",font=('Comic Sans MS',20,'normal'))

        


   

   