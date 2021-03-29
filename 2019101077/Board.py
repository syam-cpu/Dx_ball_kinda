import colorama
from colorama import Fore, Back, Style
import numpy as np
import time as time
import os
colorama.init(autoreset=True)


class Board():
    def __init__(self, ttyrows, ttycolumns):
        self._ttyrows = ttyrows
        self._ttycolumns = ttycolumns
        self._grid = np.full(
            (self._ttyrows, self._ttycolumns), Back.BLACK + " ")

    def print_grid(self):
        for row in self._grid:
            print("".join(row))

    def place_in_grid(self, start_x, start_y, game_object):
        (heigth, width) = game_object.shape
        self._grid[start_x: start_x + heigth,
                   start_y:start_y + width] = game_object

    def cleargrid(self):
        self._grid = np.full(
            (self._ttyrows, self._ttycolumns), Back.BLACK + " ")

    def print_header(self, lives, score, start_time, level):
        CURSOR_0 = "\033[0;0H"
        print(CURSOR_0)
        k = int(time.time() - start_time)
        stats = str("LEVEL: " + str(level) + "|  LIVES: "+str(lives) +
                    "  |  SCORE:" + str(score)+"  |  TIME: " + str(k))
        print(Fore.WHITE + Back.YELLOW + Style.BRIGHT + stats.center(204))
        self.cleargrid()

    def place_sidebars(self):
        for i in range(self._ttyrows):
            self._grid[i][0+29] = Back.WHITE+" "
            self._grid[i][203-30] = Back.WHITE+" "
            self._grid[i][1+29] = Back.WHITE+" "
            self._grid[i][202-30] = Back.WHITE+" "

    def layoutclear(self, Bricks_list):
        for game_object in Bricks_list:
            x = game_object.get_x()
            y = game_object.get_y()
            if(game_object.get_strength() >0 and x <=40):
                game_object_shape = game_object.get_shape(
                    game_object.get_strength())
                (heigth, width) = game_object_shape.shape
                if(heigth == 2 and width ==5):
                    self._grid[x: x + heigth,
                                y:y + width] = np.array(
                        [
                            [Back.BLACK+' ', Back.BLACK + ' ', Back.BLACK +
                                ' ', Back.BLACK + ' ', Back.BLACK + ' '],
                            [Back.BLACK+' ', Back.BLACK + ' ', Back.BLACK +
                                ' ', Back.BLACK + ' ', Back.BLACK + ' '],


                        ]

                    )

    def move_layout(self, Bricks_list):
        for game_object in Bricks_list:
            x = game_object.get_x()
            game_object.set_x(x+2)
        self.print_layout(Bricks_list)

    def print_layout(self, Bricks_list):
        for i in range(len(Bricks_list)):
            game_object = Bricks_list[i]
            if(game_object.get_state() == True and game_object.get_strength() >= 1):
                self.place_in_grid(game_object.get_x(), game_object.get_y(
                ), game_object.get_shape(game_object.get_strength()))

        self.layout_paddle_collision(Bricks_list)

    def layout_paddle_collision(self, Bricks_list):
        max_x = 0
        for game_object in Bricks_list:
            if(game_object.get_state() == True and game_object.get_strength() >= 1):
                x = game_object.get_x()
                if(x > max_x):
                    max_x = x

        if(max_x >= 43):
            print(Style.RESET_ALL, end='')
            os.system('clear')
            print(Style.RESET_ALL + "Game over".center(202))
            os.system('aplay -q ./sounds/gameover.wav&')

            raise SystemExit

    def place_rem_time(self, rem_time):
        string = str(rem_time)
        for i in range(len(string)):
            self._grid[10][0+18+i] = Back.BLACK + string[i]
            
        #self._grid[10][0+18] = Back.BLACK + str(rem_time)
        self._grid[10][9] = Back.BLACK + 'T'
        self._grid[10][10] = Back.BLACK + 'i'
        self._grid[10][11] = Back.BLACK + 'm'
        self._grid[10][12] = Back.BLACK + 'e'
        self._grid[10][13] = Back.BLACK + 'R'
        self._grid[10][14] = Back.BLACK + 'e'
        self._grid[10][15] = Back.BLACK + 'm'
        self._grid[10][16] = Back.BLACK + ':'

    def place_ufo(self, ufo_instance):
        # ufo = np.array([[Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+'.',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' '],
        #                 [Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ '.',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',
        #                  Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ '.',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' '],
        #                 [Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ '.', Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',
        #                  Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ '.',Back.BLACK+ ' ',Back.BLACK+ ' ', Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' '],

        #                 [Back.BLACK+' ', Back.BLACK+' ', Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',
        #                  Back.BLACK+'.',Back.BLACK+ '.',Back.BLACK+ '.', Back.BLACK+'.',Back.BLACK+ '.', Back.BLACK+'.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ ' ',Back.BLACK+ ' ', Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ', Back.BLACK+' ',Back.BLACK+ ' '],
        #                 [Back.BLACK+' ',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.', Back.BLACK+'(', Back.BLACK+'_',Back.BLACK+ '_', Back.BLACK+'_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_', Back.BLACK+'_',Back.BLACK+ '_', Back.BLACK+'_',
        #                  Back.BLACK+'_', Back.BLACK+'_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ ')', Back.BLACK+'.', Back.BLACK+'.', Back.BLACK+'.', Back.BLACK+'.',Back.BLACK+ '.',Back.BLACK+ ' '],
        #                 [Back.BLACK+'\ ',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ ' ',Back.BLACK+ ' ', Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',
        #                  Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ '_', Back.BLACK+'_',Back.BLACK+ '_', Back.BLACK+'_', Back.BLACK+'_', Back.BLACK+'_',Back.BLACK+ '_', Back.BLACK+'_',Back.BLACK+ '_', Back.BLACK+'_',Back.BLACK+ '/'],
        #                 [Back.BLACK+' ', Back.BLACK+' ',Back.BLACK+ ' ', Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ', Back.BLACK+' ', Back.BLACK+' ', Back.BLACK+' ',Back.BLACK+ '\ ', Back.BLACK+'_', Back.BLACK+'_',Back.BLACK+ '_',Back.BLACK+ ' ',
        #                  Back.BLACK+' ',Back.BLACK+ '_', Back.BLACK+'_',Back.BLACK+ '_',Back.BLACK+ '/',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' '],

        #                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
        ufo = ufo_instance.get_shape()
        x = 0
        y = int(ufo_instance.get_y())
        if(y + 32 > 170):
            # print("ffsf")
            y = 170-33
            ufo_instance.set_y(y)
        if(y <= 32):
            # print("fafafa")
            y = 35
            ufo_instance.set_y(y)
        self.place_in_grid(x, y, ufo)
        string = str(ufo_instance.get_life_energy())
        for i in range(len(string)):
            self._grid[20][0+18+i] = Back.BLACK + \
                str(ufo_instance.get_life_energy())[i]
        self._grid[20][9] = Back.BLACK + 'E'
        self._grid[20][10] = Back.BLACK + 'n'
        self._grid[20][11] = Back.BLACK + 'e'
        self._grid[20][12] = Back.BLACK + 'r'
        self._grid[20][13] = Back.BLACK + 'g'
        self._grid[20][14] = Back.BLACK + 'y'
        self._grid[20][15] = Back.BLACK + ':'
        
    def place_cannons(self,x,y,width):
        self._grid[x][y]= Back.BLACK+'^'
        self._grid[x][y+width] = Back.BLACK +'^' 
    
    def place_energy_bar(self,ufo_instance):
        e = ufo_instance.get_life_energy()/5
        for i in range(int(e)):
            self._grid[21][9+i] = Back.BLACK + '/'
        
    