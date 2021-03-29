import numpy as np
import os
import colorama
from colorama import Fore, Back, Style
import time
from time import sleep
from kbhit import KBHit
from alarmexception import AlarmException
import signal
import random
from Ball import Ball
from paddle import paddle
from Board import Board
colorama.init(autoreset=True)


kb = KBHit()

n = np.array(
    [
        [Fore.GREEN + ' ', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN+'_',
            Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN+' '],
        [Fore.GREEN + '(', Fore.GREEN + '_', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN+'_', Fore.GREEN+'_',
                        Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN+')'],

    ])
b = np.array(
    [
        [Fore.GREEN + ' ', Fore.GREEN + '_____', Fore.GREEN + '_____', Fore.GREEN +
            '_____', Fore.GREEN + '_____', Fore.GREEN + '_____', Fore.GREEN + ' '],
        [Fore.GREEN + '(', Fore.GREEN + '_____', Fore.GREEN + '_____', Fore.GREEN +
                        '_____', Fore.GREEN + '_____', Fore.GREEN + '_____', Fore.GREEN + ')'],

    ])
s = np.array(
    [
        [Fore.GREEN + ' ', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN +
            '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + ' '],
        [Fore.GREEN + '(', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN +
                        '_', Fore.GREEN + '_', Fore.GREEN + '_', Fore.GREEN + ')'],

    ])
brick = np.array(
    [
        [' ','_','_','_',' '],
        [ Back.GREEN+'|',Back.GREEN+ '_',Back.GREEN+ '_',Back.GREEN+ '_',Back.GREEN+ '|'],
         
        
    ]
    
)
brick2 = np.array(
    [
        [' ','_','_','_',' '],
        [ Back.BLUE+'|' ,Back.BLUE+ '_',Back.BLUE+ '_',Back.BLUE+ '_',Back.BLUE+ '|'],
         
        
    ]
    
)
brick3 = np.array(
    [
        [' ','_','_','_',' '],
        [ Back.RED+'|' ,Back.RED+ '_',Back.RED+ '_',Back.RED+ '_',Back.RED+ '|'],
         
        
    ]
    
)
#print(s.shape)
'''for row in n:
    print("".join(row))
for row in b:
    print("".join(row))
for row in s:
    print("".join(row))'''
ttyrows, ttycolumns = os.popen('stty size', 'r').read().split()
ttyrows, ttycolumns = int(ttyrows), int(ttycolumns)
if(ttyrows < 52-5 or ttycolumns < 204):
    print(Fore.RED + 'Fatal Error: Not enough legroom. Try playing with a larger terminal window.')
    raise SystemExit 
ttycolumns = 204
ttyrows  = 52-5
os.system('clear')
k = np.full((ttyrows, ttycolumns), Back.BLACK + " ")
for i in range(ttyrows):
    k[i][0+30] = Back.WHITE+" "
    k[i][203-30] = Back.WHITE+" "
    k[i][1+30] = Back.WHITE+" "
    k[i][202-30] = Back.WHITE+" "






cur = ttycolumns- 50
'''def ever():
    grid = []
    for i in range(ttyrows):
        temp=[]
        for j in range(ttyrows):
            temp.append(" ")
            grid.append(temp)
    for i in range(ttyrows-4,ttyrows-2):
        for j in range(cur,cur+7+5):
            grid[i][j]=n[i-(ttyrows-4)][j-(cur)]
    
    for i in range(ttyrows):
                for j in range (ttycolumns):
                    
                    # print(Back.LIGHTBLACK_EX +self.grid[i][j] + Back.RESET, end='')
                    print(grid[i][j],end='')
                    
                print()'''

k[ttyrows-4: ttyrows - 2, ttycolumns-50: ttycolumns-50+7+5] = n
position = random.randint(1,10)
k[ttyrows-4][cur+position] = 'O'
Ball_instance = Ball(ttyrows-4,cur+position)
Paddle_instance = paddle(ttyrows-4,cur)


'''for row in k:
   print("".join(row))'''


'''k[ttyrows-1, ttycolumns-100] = '----'
k[ttyrows-1, ttycolumns-101] = '----'
k[ttyrows-1, ttycolumns-102] = '----'
k[ttyrows-1, ttycolumns-103] = '----'
k[ttyrows-1, ttycolumns-104] = '----'
cur = ttycolumns - 104'''

cur = ttycolumns- 50

initial_time = time.time()

while(1):
    #sleep(0.0175)
    #sleep(1)
    #sleep(0.04)
    Ball_instance.move_ball()
    x = Ball_instance.get_x()
    y = Ball_instance.get_y()
    #sprint(int(x),int(y))
    #print("\033[%d;%dH" % (0, 0))
    CURSOR_0 = "\033[0;0H"
    print(CURSOR_0)
    stats = str("LIVES: "+str("lives ayya") + "  |  SCORE:" + str("scoreayya")+"  |  TIME: " + str( ))
    print(Fore.WHITE + Back.LIGHTRED_EX + Style.BRIGHT + stats.center(204))
    
    k = np.full((ttyrows, ttycolumns), Back.BLACK + " ")
    
    for i in range(ttyrows):
        k[i][0+30] = Back.WHITE+" "
        k[i][203-30] = Back.WHITE+" "
        k[i][1+30] = Back.WHITE+" "
        k[i][202-30] = Back.WHITE+" "
    k[ttyrows-4: ttyrows - 2, Paddle_instance.get_y(): Paddle_instance.get_y()+7+5] = n
    k[ttyrows -20:ttyrows-18 ,ttycolumns-50 : ttycolumns-45] = brick
    k[ttyrows -21:ttyrows-19,ttycolumns-50 : ttycolumns-45] = brick2
    k[ttyrows -21:ttyrows-19,ttycolumns-46 : ttycolumns-41] = brick

   
  
   
    k[round(x)][round(y)] = Fore.YELLOW +'O'
    for row in k:
        print("".join(row))
    
    
        
    c = kb.getinput()
    if(c == 'd'):
        if(Paddle_instance.get_y()+12 != ttycolumns-2-30):
            Paddle_instance.move_paddle_rigth()

            
    if(c == 'a'):
        if(Paddle_instance.get_y() != 3+30+1):
            Paddle_instance.move_paddle_left()
            
            
    if(c=='a' or c=='d'):
        CURSOR_0 = "\033[0;0H"
        print(CURSOR_0)
    
        
    
        #print("\033[%d;%dH" % (0, 0))
        stats = str("LIVES: "+str("lives ayya") + "  |  SCORE:" + str("scoreayya")+"  |  TIME: " + str(int(time.time()-initial_time)) )
        print(Fore.WHITE + Back.LIGHTRED_EX + Style.BRIGHT + stats.center(204))
        k = np.full((ttyrows, ttycolumns),Back.BLACK+" ")
        k[ttyrows-4: ttyrows - 2, Paddle_instance.get_y(): Paddle_instance.get_y()+7+5] = n
        k[ttyrows -20:ttyrows-18 ,ttycolumns-50 : ttycolumns-45] = brick
        k[ttyrows -21:ttyrows-19,ttycolumns-50 : ttycolumns-45] = brick2
        k[ttyrows -21:ttyrows-19,ttycolumns-46 : ttycolumns-41] = brick
        
        
       
        if(Ball_instance.get_state() == False):
            Ball_instance.set_x(ttyrows-4)
            Ball_instance.set_y(Paddle_instance.get_y()+position)
        x = Ball_instance.get_x()
        y = Ball_instance.get_y()
        k[round(x)][round(y)] = Fore.YELLOW + 'O'
        for i in range(ttyrows):
            k[i][0+30] = Back.WHITE+" "
            k[i][203-30] = Back.WHITE+" "
            k[i][1+30] = Back.WHITE+" "
            k[i][202-30] = Back.WHITE+" "


        for row in k:
            print("".join(row))
        
        
        #ever()
        
    if(c == ' '):
        if(Ball_instance.get_state() == False):
            Ball_instance.set_state(True)
            os.system('aplay -q ./sounds/shoot2.wav&')

            #x_vel_value = random.randint(-4,0)
            #y_vel_value = random.randint(-4,4) 
            #print(x_vel_value,y_vel_value)
            Ball_instance.change_x_velocity(-0.41)
            Ball_instance.change_y_velocity(0.41)
            
            
         
            
           
    
    
    
        
        
        
        
    
