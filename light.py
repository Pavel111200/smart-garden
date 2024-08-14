import smbus
import time

class Light():
    def __init__(self, turn_on_value = 400):
        self.bus = smbus.SMBus(1)
        self.turn_on_value = turn_on_value
    
    def get_sensor_value(self):
        self.bus.write_byte(0x23, 0x10)
        time.sleep(0.18)
        data = self.bus.read_i2c_block_data(0x23, 0x10, 2)
        result = (data[1] + (256 * data[0])) / 1.2
        return format(result,'.0f') + " lx"
    
    def should_turn_on_lights(self):
        turn_on = False
        if(int(self.get_sensor_value().replace(" lx", "")) <= self.turn_on_value):
            turn_on = True
        return turn_on