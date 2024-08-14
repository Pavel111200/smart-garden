from gpiozero import MCP3008

class Air_quality():
    def __init__(self):
        self.sensor = MCP3008(7)
        
    def get_sensor_value(self):
        return self.sensor.value
    
    def should_turn_on_ventilation(self):
        turn_on = False
        if(self.get_sensor_value() > 0.5):
            turn_on = True
        return turn_on