from brick import Brick
import colorama
from colorama import Back, Style
import numpy as np
#colorama.init(autoreset=True)


class Brick1(Brick):
    def _init_(self, x, y,type_value):
        #super().__init__(x,y)
        self._x = x
        self._y = y
       
    
        super().__init__(self._x,self._y,type_value)
        self._strength = 1
        self._shape = np.array(
            [
                [' ', '_', '_', '_', ' '],
                [Back.BLUE+'|', Back.BLUE + '_', Back.BLUE +
                    '_', Back.BLUE + '_', Back.BLUE + '|'],


            ])
        #@Brick.__init__(self,x,y)
       

    def get_strength(self):
        return self._strength
    
    def dec_strength(self):
        self._strength = self._strength -1 

    '''def get_shape(self):
        return np.array(
            [
                [' ', '_', '_', '_', ' '],
                [Back.BLUE+'|', Back.BLUE + '_', Back.BLUE +
                    '_', Back.BLUE + '_', Back.BLUE + '|'],


            ])'''
