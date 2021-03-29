from power_up import Power_up
import colorama
from colorama import Fore
import numpy as np
import os
import time

class Power_up4(Power_up):
    def __init__(self, x, y, type_value, start_time,x_velocity,y_velocity):

        super().__init__(x, y, type_value, start_time,x_velocity,y_velocity)
        self._shape = np.array([
            [Fore.WHITE + 'F']

        ])

        self._reached_bottom = False

    def move_powerup(self):
        self._x = self._x + self._x_velocity 
        self._y = self._y + self._y_velocity
        if(self._x <= 0):
            self.change_x_velocity(-self._x_velocity)
            os.system('aplay -q ./sounds/ball_with_walls.wav&')
        if(self._x > 42):
            self.set_reached_bottom(True)

        if(self._x >= 46):
            self.set_state(3)
        
        if(self._y >= 202-30 or self._y <= 1 + 30):
            self.change_y_velocity(-self._y_velocity)
            os.system('aplay -q ./sounds/ball_with_walls.wav&')

    def set_state(self, value):
        self._state = value

    def get_type(self):
        return self.type

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_shape(self):
        return self._shape

    def get_state(self):
        return self._state

    def get_start_time(self):
        return self._start_time

    def set_start_time(self, value):
        self._start_time = value

    def set_reached_bottom(self, value):
        self._reached_bottom = value

    def get_reached_bottom(self):
        return self._reached_bottom

    def check_collision_with_paddle(self, paddle_instance):
        (heigth, width) = paddle_instance.get_shape().shape
        heigth = heigth + 1
        if(self.get_y() >= paddle_instance.get_y() + 1 and self.get_y() <= paddle_instance.get_y() + width-2):
            os.system('aplay -q ./sounds/pad.wav&')
            # self.set_x(42)
            self.set_state(4)
            self.set_reached_bottom(False)

    
    def change_x_velocity(self, final_value):
        self._x_velocity = final_value

    def change_y_velocity(self, final_value):
        self._y_velocity = final_value
        
    def get_yvel(self):
        return self._y_velocity

    def get_xvel(self):
        return self._x_velocity

    # def activate_powerup(self, Ball_instance, Ball_instance2, Power_up_status, Power_ups):
    #     if(Power_up_status[3] == 0):
    #         for i in range(len(Power_ups)):
    #             game_object = Power_ups[i]
    #             if(game_object.get_type() == 4 and game_object.get_state() == 4 and Ball_instance.get_state() == True):
    #                 game_object.set_state(2)
    #                 Power_up_status[3] = 1
    #                 game_object.set_start_time(time.time())
    #                 Ball_instance.increase_x_velocity(0.05)
    #                 break
