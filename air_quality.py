from gpiozero import MCP3008
from sensor import Sensor

class Air_quality(Sensor):
    def __init__(self, turn_on_value = 0.5):
        self.sensor = MCP3008(7)
        # self.turn_on_value = 0.5
        super().__init__(turn_on_value)
        
    def get_sensor_value(self):
        return self.sensor.value
    
    def should_turn_on_actuator(self):
        should_turn_on = False
        if(self.get_sensor_value() > self.turn_on_value):
            should_turn_on = True
        return should_turn_on