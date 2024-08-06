import smbus

class Light():
    def __init__(self):
        self.bus = smbus.SMBus(1)
    def get_sensor_value(self):
        data = self.bus.read_i2c_block_data(0x23, 0x10, 2)
        result = (data[1] + (256 * data[0])) / 1.2
        return format(result,'.0f') + " lx"