from gpiozero import MCP3008

class Air_quality():
    def get_sensor_value(self):
        value = MCP3008(7).value
        print("Air quality sensor:")
        print(value)
        print("*"*25)
        return value