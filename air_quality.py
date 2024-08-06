from gpiozero import MCP3008

class Air_quality():
    def __init__(self):
        self.sensor = MCP3008(7)
    def get_sensor_value(self):
        return self.sensor.value