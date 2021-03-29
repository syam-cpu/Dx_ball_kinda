import os
import colorama
from colorama import Fore, Back, Style
import numpy as np
import random
from time import sleep
# colorama.init(autoreset=True)


class Ball():
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._x_velocity = 0
        self._y_velocity = 0
        self.shape1 = np.array([
            [Fore.WHITE + 'O']

        ])
        self.shape3 = np.array([
            [Fore.MAGENTA+ 'O']

        ])
        self.shape2 = np.array([
            [Fore.YELLOW + 'O']

        ])
        self.shape4 = np.array([
            [Fore.RED + 'O']

        ])
        
        
        self._type = 1

        self._state = False
        self.Reached_bottom = False
        self.Reached_ground = False
        self.Fast_ball = False

    def set_x(self, final_value):
        self._x = final_value

    def set_y(self, final_value):
        self._y = final_value

    def change_x_velocity(self, final_value):
        self._x_velocity = final_value

    def change_y_velocity(self, final_value):
        self._y_velocity = final_value

    def increase_x_velocity(self, final_value):
        if(self._x_velocity > 0):
            self._x_velocity = self._x_velocity + final_value
        else:
            self._x_velocity = self._x_velocity - final_value

    def increase_y_velocity(self, final_value):
        if(self._y_velocity > 0):
            self._y_velocity = self._y_velocity + 4
        else:
            self._y_velocity = self._y_velocity - 4

    def move_ball(self):
        self._x = self._x + (self._x_velocity * 1)
        self._y = self._y + (self._y_velocity * 1)
        if(self._x <= 0):
            self.change_x_velocity(-self._x_velocity)
            os.system('aplay -q ./sounds/ball_with_walls.wav&')
        if(self._x > 48-5):
            self.set_reached_bottom(True)
            # self.change_x_velocity(-self._x_velocity)
            # if(self.get_state() == True):
            #os.system('aplay -q ./sounds/pad_final.wav&')
        if(self._x >= 47):
            self.set_reached_ground(True)

        if(self._y >= 202-30 or self._y <= 1 + 30):
            self.change_y_velocity(-self._y_velocity)
            os.system('aplay -q ./sounds/ball_with_walls.wav&')

    def get_state(self):
        return self._state

    def set_state(self, value):
        self._state = value

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_shape(self):
        if(self._type == 1):
            return self.shape1
        if(self._type == 2):
            return self.shape2
        if(self._type == 3):
            return self.shape3
        if(self._type == 4):
            return self.shape4
        
    def set_type_value(self,powerup_status):
        if(powerup_status[3] == 1 and powerup_status[4] == 1):
            self._type = 4
        elif(powerup_status[3] == 1):
            self._type = 2
        elif(powerup_status[4] == 1):
            self._type = 3
        else:
            self._type = 1
        

    def set_reached_bottom(self, value):
        self.Reached_bottom = value

    def get_reached_bottom(self):
        return self.Reached_bottom

    def set_reached_ground(self, value):
        self.Reached_ground = value

    def get_reached_ground(self):
        return self.Reached_ground

    def check_collision_with_paddle(self, paddle_instance,powerup_status):
        if(self.get_reached_bottom() == True):
            (heigth, width) = paddle_instance.get_shape().shape
            heigth = heigth + 1
            size_of_each_region = (width - 2)/5
            if(self.get_y() >= paddle_instance.get_y() + 1 and self.get_y() <= paddle_instance.get_y() + width-2):
                os.system('aplay -q ./sounds/pad.wav&')
                self.set_x(42)
                if(powerup_status[5] == 0):
                    self.change_x_velocity(-self._x_velocity)
                    change = (
                        ((self.get_y() - (paddle_instance.get_y()+1))/size_of_each_region) - 2) * 0.05
                    value = self._y_velocity + change
                    self.change_y_velocity(value)
                    self.set_reached_bottom(False)
                else:
                    self.next_life(paddle_instance)
                return 1

            else:
                return 0
                #os.system('aplay -q ./sounds/lose_life.wav&')
                # self.set_reached_bottom(False)
                # self.set_reached_ground(True)
                # self.set_x(46)

                '''self.change_x_velocity(0)
                self.change_y_velocity(0)
                self.set_x(x_paddle)
                self.set_y(y_paddle+random.randint(1,10))'''

    def next_life(self, paddle_instance):
        x_paddle = paddle_instance.get_x()
        y_paddle = paddle_instance.get_y()
        (heigth, width) = paddle_instance.get_shape().shape
        heigth = heigth
        #os.system('aplay -q ./sounds/lose_life.wav&')
        self.set_state(False)
        self.set_reached_bottom(False)
        self.set_reached_ground(False)
        self.change_x_velocity(0)
        self.change_y_velocity(0)
        self.set_x(x_paddle)
        self.set_y(y_paddle+random.randint(1, width-2))

    def check_collision_with_Brick(self, game_object):
        x_ball = self.get_x()
        y_ball = self.get_y()
        x_brick = game_object.get_x()
        y_brick = game_object.get_y()
        if(round(x_ball) == x_brick+1 and (round(y_ball) == y_brick or int(y_ball) == y_brick + 4)):
            # print("ll")
            #sleep(1)
            if(self._y_velocity < 0):
                self.set_y(self._y + 2)
            if(self._y_velocity > 0):
                self.set_y(self._y - 2)
            self.change_y_velocity(-self._y_velocity)
            os.system('aplay -q ./sounds/brick.wav&')
            return True

        elif(round(x_ball) == x_brick or round(x_ball) == x_brick+2):
            if(round(y_ball) >= y_brick and round(y_ball) <= y_brick+4):
                #sleep(1)
                if(self._x_velocity < 0):
                    self.set_x(self._x + 2)
                if(self._x_velocity > 0):
                    self.set_x(self._x - 2)
                self.change_x_velocity(-self._x_velocity)
                os.system('aplay -q ./sounds/brick.wav&')
                return True

        else:
            return False

    def change_x_when_power_up_down(self, value):
        if(self.Fast_ball == True):
            if(value == 1):
                self.Fast_ball = False
                if(self._x_velocity > 0):
                    self._x_velocity = self._x_velocity - 0.5
                else:
                    self._x_velocity = self._x_velocity + 0.5

        elif(self.Fast_ball == False):
            if(value == 2):
                self.Fast_ball = True
                if(self._x_velocity > 0):
                    self._x_velocity = self._x_velocity + 0.5
                else:
                    self._x_velocity = self._x_velocity - 0.5

    def get_yvel(self):
        return self._y_velocity

    def get_xvel(self):
        return self._x_velocity

    def ufo_ball_collision(self,ufo):
        x_ball = self.get_x()
        y_ball = self.get_y()
        y_ufo = ufo.get_y()
        if(int(x_ball) == 8 and int(y_ball) >= int(y_ufo) and int(y_ball) <= int(y_ufo) + 32 and self._x_velocity  < 0):
            if(self._x_velocity < 0):
                    self.set_x(self._x + 2)
            if(self._x_velocity > 0):
                self.set_x(self._x - 2)
            self.change_x_velocity(-self._x_velocity)
            ufo.dec_life_energy()
            os.system('aplay -q ./sounds/brick.wav&')
        
        elif(int(x_ball) <  8 and ((round(y_ball) == y_ufo and y_ball<=y_ufo and self._y_velocity > 0) or (int(y_ball) == y_ufo + 32 and self._y_velocity < 0))):
            print(y_ufo,y_ball)
            sleep(1)
            if(self._y_velocity < 0):
                self.set_y(self._y + 4)
            if(self._y_velocity > 0):
                self.set_y(self._y - 4)
            self.change_y_velocity(-self._y_velocity)
            ufo.dec_life_energy()
            os.system('aplay -q ./sounds/brick.wav&')
        
        # elif(int(x_ball) <  8 and (round(y_ball) == y_ufo and y_ball<=y_ufo and self._y_velocity < 0) or (int(y_ball) == y_ufo + 32 and self._y_velocity > 0)):
        #     if(self._y_velocity < 0):
        #         self.set_y(self._y - 4)
        #     if(self._y_velocity > 0):
        #         self.set_y(self._y + 4)
        #     ufo.dec_life_energy()
        #     os.system('aplay -q ./sounds/brick.wav&')
            
            
        
       
    def layer_collision(self,Bricks_protect):
        for game_object in Bricks_protect:
            if(game_object.get_state() == True and game_object.get_strength() >= 1):
                if(self.check_collision_with_Brick(game_object)):
                    if(game_object.get_strength() == 1):
                        game_object.set_state(False)
                    if(game_object.get_strength() == 2):
                        game_object.dec_strength()
                    if(game_object.get_strength() == 3):
                        game_object.dec_strength()
                    if(game_object.get_type() == 4):
                        # sleep(1)
                        game_object.dec_strength()
                        game_object.dec_strength()
                        game_object.dec_strength()
                        game_object.dec_strength()
                    if(game_object.get_type() == 5):
                        game_object.set_type(game_object.get_strength())
            
        