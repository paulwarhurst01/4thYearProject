from .classI2CInterface import I2CInterface

class SensorInterface(I2CInterface):
    def __init__(self, addr:int, sensorid: int):
        I2CInterface.__init__(self, addr)
        self.sensorid = sensorid
        self.data = []    # initialised to empty array

    def get_data(self):
        self.write_byte(self.sensorid)
        data = self.read_data_7Bchunk()
        return data

    def format_data(self)->float: 
        """
        Converts ASCII characters received to a float
        Creates a string from ASCII characters received in data chunk
        Converts this string to a float and returns float
        """ 
        try:
            formatted = chr(self.data[0])
            for i in range(1, len(self.data)):                  
                formatted = formatted + (chr(self.data[i])) 
            return str(formatted)
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)

    def update(self):
        self.data = self.get_data()
        self.formatted_data = self.format_data()    