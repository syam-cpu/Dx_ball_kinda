import os
import colorama
from colorama import Fore, Back, Style
import numpy as np
import time
from time import sleep
from kbhit import KBHit
from alarmexception import AlarmException
import signal
import random
from Ball import Ball
from paddle import paddle
from Board import Board
from brick1 import Brick1
from brick2 import Brick2
from brick3 import Brick3
from brick4 import Brick4
from brick5 import Brick5
from power_up1 import Power_up1
from power_up2 import Power_up2
from power_up3 import Power_up3
from power_up4 import Power_up4
from power_up5 import Power_up5
from power_up6 import Power_up6
from power_up7 import Power_up7
from bricks_and_intro import bricks_and_intro
from power_up_manager import power_up_manager
from bullets import Bullet
from ufo import ufo


colorama.init(autoreset=True)
kb = KBHit()

ttycolumns = 204
ttyrows = 52-5

rows, columns = os.popen('stty size', 'r').read().split()
rows, columns = int(rows), int(columns)

if(rows < ttyrows or columns < ttycolumns):
    print(Fore.RED + 'Fatal Error: Not enough legroom. Try playing with a larger terminal window.')
    raise SystemExit
os.system("clear")

bricks_and_intro = bricks_and_intro(1)
bricks_and_intro.intro()
os.system('clear')


initial_pad_coord = ttycolumns - 110
start_time = time.time()
position = random.randint(1, 10)


Board_instace = Board(ttyrows, ttycolumns)
Ball_instance = Ball(ttyrows-4, initial_pad_coord+position)
Paddle_instance = paddle(ttyrows-4, initial_pad_coord)
Bricks_list = []

Power_ups = []
start = 60
brick_start = ttyrows-30
Bricks_list = bricks_and_intro.bricks(
    Bricks_list, brick_start, Brick1, Brick2, Brick3, Brick4, Brick5)
Power_up_status = [0, 0, 0, 0, 0, 0, 0]
Ball_instance2 = 10
power_up_manager = power_up_manager(
    Ball_instance, Ball_instance2, Power_up_status, Power_ups)
initial_x_vel = random.uniform(-0.11, -0.10)
initial_y_vel = random.uniform(0.10, 0.11)


prev = start_time
score = 0
lives = 10
level = 1
level_start_time = start_time
temp = 0
flag = True         #paddle
flag1 = True        #for ufo
latest_shoot_time = 0   #for paddle
latest_shoot_time1 = 0 #for ufo
Bullets = []
ufo_instance = 0
Bullets_ufo = []
Bricks_protect = []
flag_bricks = True
flag_bricks1 = True

# Ball_instance2 = 10
while(1):
   #Power_up_status[6] = 1
    ''' To check lives'''
    if(lives == 0):
        print(Style.RESET_ALL, end='')
        os.system('clear')
        print(Style.RESET_ALL + "YOUR LIVES COMPLETED!".center(202))
        print(("Your Score   :    " + str(score)).center(202))
        os.system('aplay -q ./sounds/gameover.wav&')
        raise SystemExit

    '''To check for expired power_ups'''
    for i in range(len(Power_ups)):
        game_object = Power_ups[i]
        k = int(time.time() - game_object.get_start_time())
        if(game_object.get_state() == 2):
            power_up_type = game_object.get_type()
            if(power_up_type == 7):
                # print(int(time.time()-game_object.get_start_time()))
                temp = game_object.get_start_time()
            if(k > 10):
                game_object.set_state(3)
                if(power_up_type == 4 and Power_up_status[4] == 1 and Ball_instance.get_state() == True):
                    Ball_instance.increase_x_velocity(-0.05)
                Power_up_status[power_up_type-1] = 0

    '''To move all the born powerups'''
    for i in range(len(Power_ups)):
        game_object = Power_ups[i]
        if(game_object.get_state() == 1):
            game_object.change_x_velocity(game_object.get_xvel()+0.0000001)
            game_object.move_powerup()

    '''To activate a power_up if its type is currently off'''

    Ball_instance2, Power_up_status = power_up_manager.activate_power_ups(
        Ball_instance, Ball_instance2, Power_up_status, Power_ups)

    '''To have Paddle type as determined by '''
    Paddle_instance.set_paddle_type(Power_up_status[1], Power_up_status[0])

    '''To check collisions of powerups with paddle'''
    for i in range(len(Power_ups)):
        game_object = Power_ups[i]
        if(game_object.get_reached_bottom() == True and game_object.get_state() == 1):
            game_object.check_collision_with_paddle(Paddle_instance)

    '''To move Ball'''
    Ball_instance.move_ball()

    x_Ball = Ball_instance.get_x()
    y_Ball = Ball_instance.get_y()
    x_paddle = Paddle_instance.get_x()
    y_paddle = Paddle_instance.get_y()

    '''To check collision of Ball with paddle'''
    if(Ball_instance.get_state() == True and Ball_instance.get_reached_bottom() == True):
        state = Ball_instance.check_collision_with_paddle(
            Paddle_instance, Power_up_status)
        # print(int(time.time() - level_start_time))
        if(state == 1 and int(time.time() - level_start_time) > 20):
            Board_instace.layoutclear(Bricks_list)
            Board_instace.move_layout(Bricks_list)
            os.system('aplay -q ./sounds/falling_bricks.wav&')

    '''To check collision of second ball Paddle'''
    if(Power_up_status[2] == 1):
        Ball_instance2.move_ball()
        if(Ball_instance2.get_state() == True and Ball_instance2.get_reached_bottom() == True):
            state = Ball_instance2.check_collision_with_paddle(
                Paddle_instance, Power_up_status)

    x_Ball = Ball_instance.get_x()
    y_Ball = Ball_instance.get_y()

    '''To place the elements in the Grid'''
    Board_instace.print_header(lives, score, start_time, level)
    Board_instace.place_sidebars()
    Board_instace.place_in_grid(Paddle_instance.get_x(
    ), Paddle_instance.get_y(), Paddle_instance.get_shape())

    if(Power_up_status[6] == 1 and temp != 0):
        Board_instace.place_rem_time(10 - int(time.time()-temp))
    else:
        Board_instace.place_rem_time(0)
    '''To check for a collison with Brick and generating a power_up randomly'''
    for i in range(len(Bricks_list)):
        game_object = Bricks_list[i]
        if(game_object.get_state() == True and game_object.get_strength() >= 1):
            tells_if_collided = Ball_instance.check_collision_with_Brick(
                game_object)
            tells_if_collided_1 = False
            if(Power_up_status[2] == 1):
                tells_if_collided_1 = Ball_instance2.check_collision_with_Brick(
                    game_object)
            if(tells_if_collided or tells_if_collided_1):
                if(game_object.get_strength() == 1):
                    score = score + 1
                    r = random.choice([1,2,2,2])
                    if(r == 1):

                        power_up_instance = Paddle_instance.extra_suport_provide_power_up(
                            game_object, Power_up_status, Ball_instance)
                        if(power_up_instance):
                            Power_ups.append(power_up_instance)

                    game_object.set_state(False)
                if(game_object.get_strength() == 2):
                    score = score + 1
                    game_object.dec_strength()
                if(game_object.get_strength() == 3):
                    score = score + 1
                    game_object.dec_strength()
                if(game_object.get_type() == 4 and Power_up_status[4] == 1):
                    # sleep(1)
                    game_object.dec_strength()
                    game_object.dec_strength()
                    game_object.dec_strength()
                    game_object.dec_strength()
                if(game_object.get_type() == 5):
                    game_object.set_type(game_object.get_strength())

    '''Printing all the active bricks'''
    bricks_and_intro.rainbow_color_change(Bricks_list)
    for i in range(len(Bricks_list)):
        game_object = Bricks_list[i]
        if(game_object.get_state() == True and game_object.get_strength() >= 1):
            Board_instace.place_in_grid(game_object.get_x(), game_object.get_y(
            ), game_object.get_shape(game_object.get_strength()))
        # else:
            # Board_instace.place_in_grid(game_object.get_x(),game_object.get_y(),game_object.get_shape(5))
            
    '''checking ball collison with ufo'''
    if(ufo_instance !=0):
        Ball_instance.ufo_ball_collision(ufo_instance)

    

    ''' Printing and moving paddle Bullets'''
    for i in Bullets:
        if(i.get_state() == 2):
                # print(i.get_x())
            Board_instace.place_in_grid(int(i.get_x()), int(i.get_y(
            )), i.get_shape())
            # print(i.get_shape().shape)
            i.move_bullet(1)

    for i in Bullets:
        if(i.get_state() == 2):
            score = i.all_bricks(Bricks_list, score)
            
    ''' Printing and moving ufo Bullets'''
    for i in Bullets_ufo:
        if(i.get_state() == 2):
                # print(i.get_x())
            Board_instace.place_in_grid(int(i.get_x()), int(i.get_y(
            )), i.get_shape())
            # print(i.get_shape().shape)
            i.move_bullet(0)

    '''Checnking ufo bulletes collision with paddle'''
    for i in Bullets_ufo:
        if(i.get_state() == 2):
            if(i.check_collision_with_paddle(Paddle_instance) == True):
                Ball_instance.next_life(Paddle_instance)
                lives = lives - 1
                os.system('aplay -q ./sounds/lose_life.wav&')
                break            
            
    '''printing and moving ufo'''
    (heigth, width) = Paddle_instance.get_shape().shape
    y = Paddle_instance.get_y() + width/2 - 16
    if(ufo_instance == 0 and level == 3):
        ufo_instance = ufo(0,y)
    elif(level == 3):
        ufo_instance.set_y(y)
        Board_instace.place_ufo(ufo_instance)
        energy = ufo_instance.get_life_energy()
        if(energy  <= 90 and flag_bricks):
            flag_bricks = False
            cur_cor  =  33
            Bricks_protect.clear()
            for i in range(34):
                Bricks_protect.append(Brick1(8,cur_cor,1))
                cur_cor = cur_cor + 4
        if(energy < 80 and flag_bricks1):
            flag_bricks = True
            flag_bricks1 = False
    
    for i in Bricks_protect:
        if(i.get_state() == True and i.get_strength() >= 1):
            Board_instace.place_in_grid(i.get_x(),i.get_y(),i.get_shape(1))
    if(ufo_instance != 0):
        Ball_instance.layer_collision(Bricks_protect)
   
    '''Setting the type of Ball based on power_up'''
    Ball_instance.set_type_value(Power_up_status)
   

    ''' Placing Both balls on Board'''
    Board_instace.place_in_grid(int(x_Ball), int(
        y_Ball), Ball_instance.get_shape())

    if(Power_up_status[2] == 1):
        Board_instace.place_in_grid(int(Ball_instance2.get_x()), int(
            Ball_instance2.get_y()), Ball_instance2.get_shape())

    '''Placing Power_ups on Board'''
    for i in range(len(Power_ups)):
        game_object = Power_ups[i]
        if(game_object.get_state() == 1):
            Board_instace.place_in_grid(int(game_object.get_x()), int(
                game_object.get_y()), game_object.get_shape())

    ''' bringing up cannons at end'''
    if(Power_up_status[6] == True):
        width = Paddle_instance.get_shape().shape[1]
        x = Paddle_instance.get_x()
        y = Paddle_instance.get_y()
        Board_instace.place_cannons(x,y,width)
        
    if(ufo_instance != 0):
        Board_instace.place_energy_bar(ufo_instance)

    '''printing Grid'''
    Board_instace.print_grid()

    '''To Handle Things when Ball reches the ground'''
    if(Ball_instance.get_reached_ground() == True):
        Paddle_instance.set_paddle_type(0, 0)
        Ball_instance.next_life(Paddle_instance)
        lives = lives - 1
        k = Power_up_status[2]
        Power_ups.clear()
        for i in range(7):
            Power_up_status[i] = 0
        # if(k):
            # Power_up_status[2] = 1
    if(Power_up_status[2] == 1):
        if(Ball_instance2.get_reached_ground() == True):
            Power_up_status[2] = 0

    '''Checking for keyboard input'''

    (heigth, width) = Paddle_instance.get_shape().shape

    c = kb.getinput()
    if(c == 'd'):
        if(Paddle_instance.get_y()+width < ttycolumns-2-30-1-1):
            Paddle_instance.move_paddle_rigth()

    if(c == 'a'):
        if(Paddle_instance.get_y() > 32+1+1):
            Paddle_instance.move_paddle_left()

    if(c == 'a' or c == 'd'):
        if(Ball_instance.get_state() == False):
            Ball_instance.set_x(ttyrows-4)
            Ball_instance.set_y(Paddle_instance.get_y()+position)

    if(c == ' '):
        if(Ball_instance.get_state() == False):
            Ball_instance.set_state(True)
            os.system('aplay -q ./sounds/shoot2.wav&')

            # x_vel_value = random.randint(-4,0)
            # y_vel_value = random.randint(-4,4)
            # print(x_vel_value,y_vel_value)

            Ball_instance.change_x_velocity(initial_x_vel)
            Ball_instance.change_y_velocity(initial_y_vel)
    elif(c == 'q'):

        print(Style.RESET_ALL, end='')
        os.system('clear')
        print(Style.RESET_ALL + "You quit by pressing q!".center(202))
        print(("Your Score   :    " + str(score)).center(202))
        raise SystemExit

    elif(c == 'v'):
        level = bricks_and_intro.set_level()
        Board_instace.layoutclear(Bricks_list)
        Ball_instance.next_life(Paddle_instance)
        os.system('aplay -q ./sounds/success.wav&')
        Bricks_list.clear()
        Bricks_list = bricks_and_intro.bricks(
            Bricks_list, brick_start, Brick1, Brick2, Brick3, Brick4, Brick5)
        level_start_time = time.time()
        for i in range(7):
            Power_up_status[i] = 0
        Power_ups.clear()
        Bullets.clear()
        Bullets_ufo.clear()
        

    elif(c == 'f'):
        if(Power_up_status[6] == 1):
            if(flag == True):
                os.system('aplay -q ./sounds/shoot2.wav&')
                latest_shoot_time = time.time()
                #print("holibaba")
                for i in range(2):
                    if(i == 0):
                        y = Paddle_instance.get_y()
                    else:
                        y = y + Paddle_instance.get_shape().shape[1]
                    bullet = Bullet(38, y, 1)
                    flag = False
                    bullet.set_state(2)
                    Bullets.append(bullet)
     
     
     
    ''' genrating ufo bullets'''
    if(flag1 == True and level == 3 ):
        os.system('aplay -q ./sounds/shoot2.wav&')
        latest_shoot_time1 = time.time()
        y = Paddle_instance.get_y()
        (h,w) = Paddle_instance.get_shape().shape
        bullet = Bullet(8, int(y+(w/2)), 1)
        flag1 = False
        bullet.set_state(2)
        Bullets_ufo.append(bullet)
        
    '''enabling shhot from time after a delay'''
    if(float(time.time() - latest_shoot_time)>0.5):
        latest_shoot_time = time.time()
        flag = True
    
    if(float(time.time() - latest_shoot_time1)>1 and level == 3):
        latest_shoot_time1 = time.time()
        flag1 = True    
    # flag = True
    
    
    ''' for mving to next level'''
    active_bricks = 0
    for i in Bricks_list:
        if(i.get_state() == True and i.get_strength() >= 1):
            active_bricks = active_bricks + 1
            
    if(active_bricks == 0):
        level = bricks_and_intro.set_level()
        Board_instace.layoutclear(Bricks_list)
        Ball_instance.next_life(Paddle_instance)
        os.system('aplay -q ./sounds/success.wav&')
        Bricks_list.clear()
        Bricks_list = bricks_and_intro.bricks(
            Bricks_list, brick_start, Brick1, Brick2, Brick3, Brick4, Brick5)
        level_start_time = time.time()
        for i in range(7):
            Power_up_status[i] = 0
        Power_ups.clear()
        Bullets.clear()
        Bullets_ufo.clear()
        
        
    
    
        
    
  