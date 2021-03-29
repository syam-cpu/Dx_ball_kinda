from brick import Brick
import colorama
from colorama import Fore, Back, Style
import numpy as np
#colorama.init(autoreset=True)


class Brick3(Brick):
    def _init_(self, x, y,type_value):
        self._type = 3
        super().__init__(x, y,type_value)
        self._strength = 3
        self._x = x
        self._y = y
        
        self._shape = np.array(
            [
                [' ', '_', '_', '_', ' '],
                [Back.RED+'|', Back.RED + '_', Back.RED +
                    '_', Back.RED + '_', Back.RED + '|'],


            ]

        )
       
    def get_strength(self):
        return self._strength
    
    
    def dec_strength(self):
        self._strength = self._strength -1 
    '''def get_shape(self):
        return np.array(
            [
                [' ', '_', '_', '_', ' '],
                [Back.RED+'|', Back.RED + '_', Back.RED +
                    '_', Back.RED + '_', Back.RED + '|'],


            ]

        )'''