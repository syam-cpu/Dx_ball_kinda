from brick import Brick
import colorama
from colorama import Fore, Back, Style
import numpy as np
#colorama.init(autoreset=True)


class Brick4(Brick):
    def _init_(self, x, y,type_value):
        #super().__init__(x, y)
        
        self._x = x
        self._y = y
        super().__init__(self._x,self._y,type_value)
        self._strength = 1
        
        self._shape = np.array(
            [
                [' ', '_', '_', '_', ' '],
                [Back.YELLOW+'|', Back.YELLOW + '_', Back.YELLOW +
                    '_', Back.YELLOW + '_', Back.YELLOW + '|'],


            ]

        )
        #Brick.__init__(self,x,y)
      

    def get_strength(self):
        return self._strength
    
    def dec_strength(self):
        self._strength = self._strength -1 
    '''def get_shape(self):
        return np.array(
            [
                [' ', '_', '_', '_', ' '],
                [Back.GREEN+'|', Back.GREEN + '_', Back.GREEN +
                    '_', Back.GREEN + '_', Back.GREEN + '|'],


            ]

        )'''