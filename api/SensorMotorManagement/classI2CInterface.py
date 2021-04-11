from smbus import SMBus

class I2CInterface(object):
    def __init__(self, addr: int):
        self.bus = SMBus(1)         # indicates /dev/i2c-1
        self.addr = addr
        self.errormsg = "Sensor device offline or incorrect address set"
        self.formatted_data = ""

    def write_byte(self, data: int):
        """
        Writes a single byte of data
        """
        try:
            self.bus.write_byte(self.addr, data)
        except OSError as e:
            print(e)
            print(self.errormsg)
    
    def read_byte(self):
        """
        Reads a single byte of data
        """
        try:
            data = self.bus.read_byte(self.addr)
            return data
        except OSError as e:
            print(e)
            print(self.errormsg)

    def read_data_chunk(self, number_of_bytes: int):
        """
        Reads and returns data chunk of size <number_of_bytes> bytes
        """
        try:
            data = self.bus.read_i2c_block_data(self.addr, 0, number_of_bytes)
            return data
        except OSError as e:
            print(e)
            print(self.errormsg)




