import numpy as np
from colorama import Back
class ufo():
    def __init__ (self,x,y):
        self._x = x
        self._y = y 
        self.life_energy = 100
        self._shape = np.array([[Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+'.',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' '],
                        [Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ '.',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',
                         Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ '.',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' '],
                        [Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ '.', Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',
                         Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ '.',Back.BLACK+ ' ',Back.BLACK+ ' ', Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' '],

                        [Back.BLACK+' ', Back.BLACK+' ', Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',
                         Back.BLACK+'.',Back.BLACK+ '.',Back.BLACK+ '.', Back.BLACK+'.',Back.BLACK+ '.', Back.BLACK+'.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ ' ',Back.BLACK+ ' ', Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ', Back.BLACK+' ',Back.BLACK+ ' '],
                        [Back.BLACK+' ',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.',Back.BLACK+ '.', Back.BLACK+'(', Back.BLACK+'_',Back.BLACK+ '_', Back.BLACK+'_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_', Back.BLACK+'_',Back.BLACK+ '_', Back.BLACK+'_',
                         Back.BLACK+'_', Back.BLACK+'_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ ')', Back.BLACK+'.', Back.BLACK+'.', Back.BLACK+'.', Back.BLACK+'.',Back.BLACK+ '.',Back.BLACK+ ' '],
                        [Back.BLACK+'\ ',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ '_',Back.BLACK+ ' ',Back.BLACK+ ' ', Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',
                         Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ '_', Back.BLACK+'_',Back.BLACK+ '_', Back.BLACK+'_', Back.BLACK+'_', Back.BLACK+'_',Back.BLACK+ '_', Back.BLACK+'_',Back.BLACK+ '_', Back.BLACK+'_',Back.BLACK+ '/'],
                        [Back.BLACK+' ', Back.BLACK+' ',Back.BLACK+ ' ', Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ', Back.BLACK+' ', Back.BLACK+' ', Back.BLACK+' ',Back.BLACK+ '\ ', Back.BLACK+'_', Back.BLACK+'_',Back.BLACK+ '_',Back.BLACK+ ' ',
                         Back.BLACK+' ',Back.BLACK+ '_', Back.BLACK+'_',Back.BLACK+ '_',Back.BLACK+ '/',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' '],

                       

                       
                        [Back.BLACK+' ', Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ', Back.BLACK+' ',Back.BLACK+ ' ', Back.BLACK+' ', Back.BLACK+' ', Back.BLACK+' ', Back.BLACK+' ', Back.BLACK+' ', Back.BLACK+' ', Back.BLACK+' ',Back.BLACK+ ' ', Back.BLACK+' ', Back.BLACK+'|',Back.BLACK+ '|', Back.BLACK+' ', Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ', Back.BLACK+' ', Back.BLACK+' ',Back.BLACK+ ' ', Back.BLACK+' ', Back.BLACK+' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ',Back.BLACK+ ' ', Back.BLACK+' ', Back.BLACK+' ']])
    
    
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_shape(self):
        return self._shape
    
    
    def set_y(self,value):
        self._y = value
        
    
    def get_life_energy(self):
        return self.life_energy
    
    def dec_life_energy(self):
        self.life_energy = self.life_energy - 5
        
     
                    
    
        