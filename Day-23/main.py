import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
scoreboard = Scoreboard()
carmanager = CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move_car()
    # Detect Car collision with turtle
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    # Detect successfull crossing
    if player.ycor() > 280:

        player.refresh()
        carmanager.level_up()

        scoreboard.increase_level()


screen.exitonclick()
