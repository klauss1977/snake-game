import time
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard


def game():
    screen = Screen()
    screen.clear()
    screen.setup(600, 600)
    screen.bgcolor("black")
    screen.title("My snake game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) < 15:
            scoreboard.score += 1
            snake.extend()
            food.refresh()
        scoreboard.update_score()

        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.set_the_new_highscore()
            scoreboard.update_score()

            scoreboard.game_over()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.set_the_new_highscore()
                scoreboard.update_score()
                scoreboard.game_over()


game()
new_screen = Screen()
replay_game = True
while replay_game:
    replay = new_screen.textinput("Game over", "Play again? ")
    if replay == 'yes':
        game()
    else:
        replay_game = False
        new_screen.bye()
