import colorama
from colorama import Back
import numpy as np


class Brick(object):
    def __init__(self,x,y,type_value):
        self._x = x
        self._y = y
        self._state = True
        self._type = type_value
        self._strength = type_value
        self._shape1 = np.array(
            [
                [' ', '_', '_', '_', ' '],
                [Back.BLUE+'|', Back.BLUE + '_', Back.BLUE +
                    '_', Back.BLUE + '_', Back.BLACK + '|'],


            ])
        self._shape2 = np.array(
            [
                [' ', '_', '_', '_', ' '],
                [Back.GREEN+'|', Back.GREEN + '_', Back.GREEN +
                    '_', Back.GREEN + '_', Back.BLACK+ '|'],


            ]

        )
        self._shape3 = np.array(
            [
                [' ', '_', '_', '_', ' '],
                [Back.RED+'|', Back.RED + '_', Back.RED +
                    '_', Back.RED + '_', Back.BLACK + '|'],


            ]

        )
        self.shape4 = np.array(
            [
                [' ', '_', '_', '_', ' '],
                [Back.YELLOW+'|', Back.YELLOW + '_', Back.YELLOW +
                    '_', Back.YELLOW + '_', Back.BLACK+ '|'],


            ]

        )
        
        
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    
    def set_x(self,value):
        self._x = value
        
    def set_y(self,value):
        self._y = value
        
    def set_state(self,value):
        self._state = value
        
    def get_state(self):
        return self._state
    
  
    
    def get_strength(self):
        return 4
    
    def get_shape(self,value):
        if(value == 1):
            return self._shape1
        if(value == 2):
            return self._shape2
        if(value == 3):
            return self._shape3
        if(value == 4):
            return self.shape4
        
        
    
        
    def get_type(self):
        return self._type
    
    def set_type(self,value):
        self._type = value
    
    
    def set_strength(self,value):
        self._strength = value