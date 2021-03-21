from smbus import SMBus

class I2CInterface(object):
    def __init__(self, addr: int):
        self.bus = SMBus(1)         # indicates /dev/i2c-1
        self.addr = addr
        self.errormsg = "Sensor device offline or incorrect address set"
        self.formatted_data = ""

    def write_byte(self, data: int):
        try:
            self.bus.write_byte(self.addr, data)
        except OSError as e:
            print(e)
            print(self.errormsg)
    
    def read_byte(self):
        try:
            data = self.bus.read_byte(self.addr)
            return data
        except OSError as e:
            print(e)
            print(self.errormsg)

    def read_data_7Bchunk(self):
        """
        Reads and returns a 7-byte data chunk
        """
        try:
            data = self.bus.read_i2c_block_data(self.addr, 0, 7)
            return data
        except OSError as e:
            print(e)
            print(self.errormsg)
