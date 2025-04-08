# _786_

import curses as curs
from random import randint
from time import sleep

world = curs.initscr()

class character:
    def __init__(self, x, y, symb):
        self.x = x
        self.y = y
        self.symb = symb

    def move(self, dirc):
        pass

class players(character):

    def move(self, dirc):
        if dirc == "up":
            self.y -= 1
        elif dirc == "left":
            self.x -= 1
        elif dirc == "down":
            self.y += 1
        elif dirc == "right":
            self.x += 1
            
class enemys(character):
     def move(self):
        dirc = randint(0, 4)

        if dirc == 0:
            self.y -= 1
        elif dirc == 1:
            self.x -= 1
        elif dirc == 2:
            self.y += 1
        elif dirc == 3:
            self.x += 1




def main(world):
    stdscr = curs.initscr()
    curs.curs_set(0)
    curs.noecho()
    curs.cbreak()
    stdscr.keypad(True)

    player = players(10, 10, "!")
    
    while True:
        wave = 1
        world.clear()
        world.addch(player.y, player.x, player.symb)

        for i in range(wave):
            enemy = enemys(randint(1, 30), randint(1, 30), "*")
            world.addch(enemy.y, enemy.x, enemy.symb)
        enemy.move()


        key = world.getch()
        if key == ord("q"):
            break
        elif key == ord("w"):
            player.move("up")
        elif key == ord("a"):
            player.move("left")
        elif key == ord("s"):
            player.move("down")
        elif key == ord("d"):
            player.move("right")
        world.refresh()

curs.wrapper(main)
