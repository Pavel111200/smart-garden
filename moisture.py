from gpiozero import MCP3008

class Moisture():
    def __init__(self, water_value = 38, air_value = 78):
        self.water_value = water_value
        self.air_value = air_value
        self.intervals = (air_value - water_value) / 3

    def get_sensor_value(self):
        moisture = MCP3008(0).value * 100
        print("Moisture sensor value:")
        if(moisture > self.water_value and moisture < (self.water_value + self.intervals)):
            print("Very Wet")
            print(moisture)
        elif(moisture < self.air_value and moisture > (self.water_value + self.intervals)):
            print("Wet")
            print(moisture)
        else:
            print("Dry")
            print(moisture)
        print("*"*25)
        return moisture