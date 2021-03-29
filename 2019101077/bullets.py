from power_up import Power_up
import colorama
from colorama import Fore
import numpy as np
import os
import time

class Bullet():
    def __init__(self, x, y,state):

        
        self._shape = np.array([
            [Fore.MAGENTA+'@']

        ])
        self.state = state
        self.x = x
        self.y = y

    def move_bullet(self,value):
        if(value == 1):
            self.x = self.x - 0.06
       
            if(self.x <= 0):
                self.set_state(3)
                os.system('aplay -q ./sounds/ball_with_walls.wav&')
        else:
            self.x = self.x + 0.06
       
            if(self.x >= 44):
                self.set_state(3)
                os.system('aplay -q ./sounds/ball_with_walls.wav&')
            
        
        

    def set_state(self, value):
        self.state = value

   

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_shape(self):
        return self._shape

    def get_state(self):
        return self.state

    def check_collision_with_Brick(self, game_object):
        x_ball = self.get_x()
        y_ball = self.get_y()
        x_brick = game_object.get_x()
        y_brick = game_object.get_y()
        

        if(round(x_ball) == x_brick):
            if(round(y_ball) >= y_brick and round(y_ball) <= y_brick+4):
                #sleep(1)
                self.set_state(3)
                os.system('aplay -q ./sounds/brick.wav&')
                return True

        else:
            return False
        
    def all_bricks(self,bricks_list,score):
        for game_object in bricks_list:
            if(game_object.get_state() == True and game_object.get_strength() >= 1):
                if(self.check_collision_with_Brick(game_object)):
                    if(game_object.get_strength() == 1):
                        score = score + 1
                        game_object.set_state(False)
                    if(game_object.get_strength() == 2):
                        score = score + 1
                        game_object.dec_strength()
                    if(game_object.get_strength() == 3):
                        score = score + 1
                        game_object.dec_strength()
                    if(game_object.get_type() == 4):
                        # sleep(1)
                        game_object.dec_strength()
                        game_object.dec_strength()
                        game_object.dec_strength()
                        game_object.dec_strength()
                    if(game_object.get_type() == 5):
                        game_object.set_type(game_object.get_strength())
                    
                    return score
        return score
    
    def check_collision_with_paddle(self,paddle_instance):
        if(int(self.get_x()) == 42 and int(paddle_instance.get_y())<=int(self.get_y()) and int(paddle_instance.get_y()+paddle_instance.get_shape().shape[1])>=int(self.get_y()) ):
            self.set_state(3)
            return True
        return False
        



    # def activate_powerup(self, Ball_instance, Ball_instance2, Power_up_status, Power_ups):
    #     if(Power_up_status[0] == 0):
    #         for i in range(len(Power_ups)):
    #             game_object = Power_ups[i]
    #             if(game_object.get_type() == 1 and game_object.get_state() == 4):
    #                 game_object.set_state(2)
    #                 Power_up_status[0] = 1
    #                 game_object.set_start_time(time.time())
    #                 break

