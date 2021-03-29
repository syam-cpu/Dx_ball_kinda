import random
import os
from colorama import Fore, Back, Style
class bricks_and_intro():
    
    def __init__(self,level):
        self.level = level
    
    
    def set_level(self):
        self.level = self.level + 1
        if(self.level == 4):
            print(Style.RESET_ALL, end='')
            os.system('clear')
            print(Style.RESET_ALL + "Game over".center(202))
            os.system('aplay -q ./sounds/gameover.wav&')
            raise SystemExit
        return self.level
            
    def intro(self):
        print("...       .   .      ....      .     .      .    ".center(200))
        print(".   .      . .       .   .    . .    .      .    ".center(200))
        print(".    .      .   ...  .  .    .   .   .      .    ".center(200))
        print(".   .      . .       .   .   .....   .      .    ".center(200))
        print("...       .   .      ....    .   .   .....  .....".center(200))
        os.system('aplay -q ./sounds/initial.wav')
    
    
    def add_layout(self,Bricks_list,Brick1):
        Bricks_list.append(Brick1(25,56,1))
        Bricks_list.append(Brick1(24,52,1))
        Bricks_list.append(Brick1(23,48,1))
        Bricks_list.append(Brick1(22,44,1))
        Bricks_list.append(Brick1(22,56+90,1))
        Bricks_list.append(Brick1(23,52+90,1))
        Bricks_list.append(Brick1(24,48+90,1))
        Bricks_list.append(Brick1(25,44+90,1))
        return Bricks_list
        
        
    def bricks(self,Bricks_list,brick_start,Brick1,Brick2,Brick3,Brick4,Brick5):
        if(self.level == 2):
            Bricks_list = self.add_layout(Bricks_list,Brick1)
            
        for j in range(4):
            if(j % 2 == 0):
                start = 60 
                count = 20
            else:
                if(self.level == 2 or self.level == 1):
                    start = 60+20
                    count = 20-10
                else:
                    start = 60
                    count = 20
            cur  = start
            for i in range(10):
                #cur = start + (i*4)
                brick_type = random.choice([1, 1, 1, 2, 2, 2, 3, 3, 3, 4,5,5])
                if(brick_type == 1):
                    Bricks_list.append(Brick1(brick_start, cur, 1))

                if(brick_type == 2):
                    Bricks_list.append(Brick2(brick_start, cur, 2))

                if(brick_type == 3):
                    Bricks_list.append(Brick3(brick_start, cur, 3))
                if(brick_type == 4):
                    Bricks_list.append(Brick4(brick_start, cur, 4))
                if(brick_type == 5):
                    Bricks_list.append(Brick5(brick_start, cur, 5))
                cur = cur + 8
                
            
            if(self.level == 1 or self.level == 2):
                brick_start = brick_start - 2
            else:
                brick_start = brick_start - 2
        return Bricks_list
    
    
    def rainbow_color_change(self,Bricks_list):
        for i in Bricks_list:
            if(i.get_type() == 5):
                s  = i.get_strength()
                if(s ==1 or s==5):
                    i.set_strength(3)
                else:
                    i.set_strength(s - 1)
    
                    
            
        