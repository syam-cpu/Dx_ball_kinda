import colorama
from colorama import Fore, Back, Style
import numpy as np
import random
import time
from power_up1 import Power_up1
from power_up2 import Power_up2
from power_up3 import Power_up3
from power_up4 import Power_up4
from power_up5 import Power_up5
from power_up6 import Power_up6
from power_up7 import Power_up7
# colorama.init(autoreset=True)


class paddle():
    def __init__(self, x, y):
        self._y = y
        self._x = x
        self._type = 2
        self._shape2 = np.array(
            [
                [Fore.GREEN + ' ', Fore.GREEN+'_', Fore.GREEN+'_', Fore.BLUE+'_', Fore.BLUE+'_', Fore.MAGENTA+'_',
                 Fore.MAGENTA + '_', Fore.BLUE + '_', Fore.BLUE + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN+' '],
                [Fore.GREEN + '(', Back.YELLOW + '_', Back.YELLOW+'_', Back.BLUE+'_', Back.BLUE+'_', Back.MAGENTA+'_',
                 Back.MAGENTA + '_', Back.BLUE + '_', Back.BLUE + '_', Back.YELLOW+'_', Back.YELLOW + '_', Back.BLACK+')'],

            ])
        self._shape3 = np.array(
            [
                [Fore.GREEN + ' ', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN+'_',
                 Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN +
                 '_', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN +
                 '_', Fore.GREEN+'_', Fore.GREEN+'_',
                 Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN+' '],
                [Fore.GREEN + '(', Fore.GREEN + '_', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN+'_',
                 Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN +
                 '_', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN +
                 '_', Fore.GREEN+'_', Fore.GREEN+'_',
                 Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN+')'],

            ])

        self._shape1 = np.array(
            [
                [Fore.GREEN + ' ', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN+'_',
                 Fore.GREEN+' '],
                [Fore.GREEN + '(', Fore.GREEN + '_', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN+'_',
                 Fore.GREEN+')'],

            ])

    def move_paddle_left(self):
        self._y = self._y - 3

    def move_paddle_rigth(self):
        self._y = self._y + 3

    def get_y(self):
        return self._y

    def get_x(self):
        return self._x

    def get_shape(self):
        if(self._type == 1):
            return self._shape1
        if(self._type == 2):
            # self._shape2[0][0] = '^'
            # self._shape2[0][11] = '^'
            return self._shape2
        if(self._type == 3):
            return self._shape3

    def set_type(self, value):
        self._type = value

    def set_paddle_type(self, S, E):
        if(S > 0 and E > 0):
            self.set_type(2)

        if(S > 0 and E == 0):
            self.set_type(1)

        if(S == 0 and E > 0):
            self.set_type(3)

        if(S == 0 and E == 0):
            self.set_type(2)

    def extra_suport_provide_power_up(self, game_object,Power_up_status,Ball_instance):
        r = random.choice([1, 2, 2, 4, 7, 7,7])
        x_vel = Ball_instance.get_xvel()
        y_vel = Ball_instance.get_yvel()
        if(r == 1):
            power_up_instance = Power_up1(int(game_object.get_x()), int(
                game_object.get_y()), 1, time.time(),x_vel,y_vel)
            return power_up_instance
        if(r == 2):
            power_up_instance = Power_up2(int(game_object.get_x()), int(
                game_object.get_y()), 2, time.time(),x_vel,y_vel)
            return power_up_instance
        if(r == 3):
            power_up_instance = Power_up3(int(game_object.get_x()), int(
                game_object.get_y()), 3, time.time(),x_vel,y_vel)
            if(Power_up_status[2] == 0):
                return power_up_instance
            else:
                return 0
              
        if(r == 4):
            power_up_instance = Power_up4(int(game_object.get_x()), int(
                game_object.get_y()), 4, time.time(),x_vel,y_vel)
            return power_up_instance
           
        if(r == 5):
            power_up_instance = Power_up5(int(game_object.get_x()), int(
                game_object.get_y()), 5, time.time(),x_vel,y_vel)
            return power_up_instance
        if(r == 6):
            power_up_instance = Power_up6(int(game_object.get_x()), int(
                game_object.get_y()), 6, time.time(),x_vel,y_vel)
            return power_up_instance
        
        if(r == 7):
            power_up_instance = Power_up7(int(game_object.get_x()), int(
                game_object.get_y()), 7, time.time(),x_vel,y_vel)
            return power_up_instance

           