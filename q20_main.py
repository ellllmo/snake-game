from snake import Snake
from food import Food,BigFood
from scoreboard import Highscore, Score
from screen import MyScreen
from barrier import Barrier

screen=MyScreen()
food=Food()
snake=Snake()
score=Score()
highscore=Highscore()

screen.listen(snake)
keep_moving=True
big_food_exist=False
hardship=3
change_level=7
bigfood=0
new_barrier=0

def reset_game():
    score.game_over()
    highscore.updete_highscore(score.score)
    snake.reset()
    screen.reset()
    score.reset()
    if new_barrier:
        new_barrier.reset()

while keep_moving:
    screen.update()
    snake.move()


    # change level game
    if score.score % change_level == 5  and score.change_level:
        screen.new_level()
        screen.change(int(score.score/change_level)+1)
        new_barrier=Barrier()
        score.change_level=False
        food.new(new_barrier)


    # make and show big rad food
    if score.score != 0 and score.score % hardship == 0 :
        # for don't make object again
        if not big_food_exist:    
            bigfood=BigFood()
            bigfood.make_big_food()
            big_food_exist=True
            food_size=True
        else:
            # blink in time
            food_size=bigfood.wink(food_size)
    
    # after one score if you are not eat big red food it's disappear 
    if score.score % hardship != 0 and big_food_exist:
        bigfood.new()
        big_food_exist=False


    # if you eat big red food give more score and snake segment 
    if bigfood and snake.snake[0].distance(bigfood) < 17:
            bigfood.new()
            food.new(new_barrier)
            snake.add()
            snake.add()
            score.updete_score()
            score.updete_score()
            big_food_exist= False


    # if your head is near than 15 you eat food        
    if snake.snake[0].distance(food) < 16:
            food.new(new_barrier)
            snake.add()
            score.updete_score()


    # after level 8 we are have barrier and if your head hit it you .. 
    if new_barrier :
        for barrier in new_barrier.barrierlist:
            if snake.snake[0].distance(barrier) < 36 :
                reset_game()


    # if your head hit to var you game over        
    if snake.snake[0].xcor() > 297 or snake.snake[0].xcor() < -300 or snake.snake[0].ycor() > 300 or snake.snake[0].ycor() < -300 : 
        reset_game() 


    else:
    # if your head hit your self you game over
        for segment in snake.snake[1:]:
            if snake.snake[0].distance(segment) < 10 :
                reset_game()

screen.exit()