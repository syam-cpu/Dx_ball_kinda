import random
import time
from Ball import Ball

class power_up_manager():
    def __init__(self, Ball_instance, Ball_instance2, Power_up_status, Power_ups):
        self.Ball_instance = Ball_instance
        self.Ball_instance2 = Ball_instance2
        self.Power_up_status = Power_up_status
        self.Power_ups = Power_ups

    def activate_power_ups(self, Ball_instance, Ball_instance2, Power_up_status, Power_ups):
        if(Power_up_status[5] == 0):
            for i in range(len(Power_ups)):
                game_object = Power_ups[i]
                if(game_object.get_type() == 6 and game_object.get_state() == 4):
                    game_object.set_state(2)
                    Power_up_status[5] = 1
                    # Ball_instance.next_life(Paddle_instance)
                    #Power_up_status[5] = 0
                    game_object.set_start_time(time.time())
                    break

        if(Power_up_status[0] == 0):
            for i in range(len(Power_ups)):
                game_object = Power_ups[i]
                if(game_object.get_type() == 1 and game_object.get_state() == 4):
                    game_object.set_state(2)
                    Power_up_status[0] = 1
                    game_object.set_start_time(time.time())
                    break

        if(Power_up_status[1] == 0):
            for i in range(len(Power_ups)):
                game_object = Power_ups[i]
                if(game_object.get_type() == 2 and game_object.get_state() == 4):
                    game_object.set_state(2)
                    Power_up_status[1] = 1
                    game_object.set_start_time(time.time())
                    break

        if(Power_up_status[2] == 0):
            for i in range(len(Power_ups)):
                game_object = Power_ups[i]
                if(game_object.get_type() == 3 and game_object.get_state() == 4):
                    game_object.set_state(3)
                    Power_up_status[2] = 1
                    Ball_instance2 = Ball(
                        Ball_instance.get_x(), Ball_instance.get_y())
                    Ball_instance2.change_x_velocity(random.uniform(-0.17, -0.16))
                    Ball_instance2.change_y_velocity(random.uniform(0.16, 0.17))
                    Ball_instance2.set_state(True)
                    game_object.set_start_time(time.time())
                    break

        if(Power_up_status[3] == 0):
            for i in range(len(Power_ups)):
                game_object = Power_ups[i]
                if(game_object.get_type() == 4 and game_object.get_state() == 4 and Ball_instance.get_state() == True):
                    game_object.set_state(2)
                    Power_up_status[3] = 1
                    game_object.set_start_time(time.time())
                    Ball_instance.increase_x_velocity(0.05)
                    break

        if(Power_up_status[4] == 0):
            for i in range(len(Power_ups)):
                game_object = Power_ups[i]
                if(game_object.get_type() == 5 and game_object.get_state() == 4):
                    game_object.set_state(2)
                    Power_up_status[4] = 1
                    game_object.set_start_time(time.time())
                    break
        
        if(Power_up_status[6] == 0):
            for i in range(len(Power_ups)):
                game_object = Power_ups[i]
                if(game_object.get_type() == 7 and game_object.get_state() == 4):
                    game_object.set_state(2)
                    Power_up_status[6] = 1
                    game_object.set_start_time(time.time())
                    break

                    
        return Ball_instance2,Power_up_status