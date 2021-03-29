
class Power_up(object):
    def __init__(self,x,y,type_value,start_time,x_velocity,y_velocity):
        self.type = type_value
        self._x  = x
        self._y = y
        self._state = 1 
        self._start_time = start_time
        self._x_velocity = x_velocity
        self._y_velocity = y_velocity
        
        
    def move_powerup(self):
        return
    
    def set_state(self,value):
        return
    
    def get_type(self):
        return 
    
    def get_x(self):
        return 
    
    def get_y(self):
        return 
    
    def get_shape(self):
        return
        
    def get_state(self):
        return 
    
    def get_start_time(self):
        return 
    
    def check_collision_with_paddle(self,paddle_instance):
        return
    
    def get_reached_bottom(self):
        return
    
    def set_reached_bottom(self):
        return
    
    def set_start_time(self,value):
        return
    
    def activate_powerup(self,value):
        return
    
    
    
    def change_x_velocity(self, final_value):
        self._x_velocity = final_value

    def change_y_velocity(self, final_value):
        self._y_velocity = final_value