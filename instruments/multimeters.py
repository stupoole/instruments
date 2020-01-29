import visa
import numpy as np

__all__ = ['K2000']


class K2000:
    # On object creation, the buffer length is set to 500. This should be editable.
    def __init__(self):
        self.buffer_length = 500

    # connect to a k2000 set up using an rs232 at 19.2k baud rate with given port.
    # The range is the measurement range (0 is auto).
    def connect(self, port):
        rm = visa.ResourceManager('@ni')
        self.k2000 = rm.open_resource(f'COM{port}', baud_rate=19200)
        self.k2000.close()
        self.k2000.open()
        self.k2000.baud_rate = 19200
        self.k2000.timeout = 5000
        self.k2000.write_termination = '\r\n'
        self.k2000.read_termination = '\r\n'
        self.k2000.write('*rst')
        self.k2000.write('*cls')

        print(self.k2000.query('*IDN?'))

    # Initiates the measurement set up in measure_n
    def trigger(self):
        self.k2000.write('init')
        self.k2000.write('*wai')

    # reads the data from buffer. For use with measure_n and trigger.
    def read_buffer(self):
        # self.k2000.write('form:data ASCII')  #  read doesn't work without this line ?
        data = self.k2000.query_ascii_values('trac:data?')

        data = np.array(data)

        return data

    # Sets up the instrument ready to measure Rxy given a probe current from a sourcemeter
    def measure_n(self, num, volt_range, nplc):
        self.k2000.write('sens:func "volt"')  # measure volts
        self.k2000.write(f'sens:volt:nplc {nplc}')  # level of averaging min, 0.01 -> 10 ish Power line cycle:
        # 50hz 2-> 25hz measurement
        self.k2000.write(f'sens:volt:rang {volt_range}')  # auto-ranging
        self.k2000.write(f'trig:count {num}')  # number of points to measure
        self.k2000.write('trac:clear')  # clear buffer
        self.k2000.write(f'trac:poin {num}')  # size of buffer
        self.k2000.write('trac:feed sens')  # what goes in buffer
        self.k2000.write('trac:feed:cont next')  # doesn't overwrite previous data until full
        # self.k2000.write('init')

    # sets up measurement for one single values. For use with a source meter to provide current and use
    # read_one to take readings
    def measure_one(self, volt_range, nplc):
        self.k2000.write('sens:func "volt"')  # measure volts
        self.k2000.write(f'sens:volt:nplc {nplc}')  # level of averaging min, 0.01 -> 10 ish Power line cycle:
        # 50hz 2-> 25hz measurement
        self.k2000.write(f'sens:volt:rang {volt_range}')  # auto-ranging


    # reads as single value from the k2000. Use after measure_one to read the value.
    def read_one(self):
        data = np.array([self.k2000.query_ascii_values('sens:data?')])
        return data[0][0]

    def close(self):
        self.k2000.close()

    # TODO: Set up k2000 to be able to measure 2 and 4 wire on it's own 