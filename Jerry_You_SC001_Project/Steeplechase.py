"""
File: Steeplechase.py
Name: Jerry_You
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():

    for i in range(11):
            if front_is_clear():
                move()
            else:
                jump()




def jump():
    """
    Karel is on the left, facing East
    Karel is on the right
    """
    up()
    cross()
    down()

    while not front_is_clear():
        turn_left()
        move()
        turn_right()


def up():
    """
    Karel is on the left, facing East
    Karel is at the upper left, facing North
    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def cross():
    move()
    turn_right()


def down():
    while front_is_clear():
        move()
    else:
        turn_left()









# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
