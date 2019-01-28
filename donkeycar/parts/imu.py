import time
from Adafruit_BNO055 import BNO055


class Mpu6050:
    '''
    Installation:
    sudo apt install python3-smbus
    or
    sudo apt-get install i2c-tools libi2c-dev python-dev python3-dev
    git clone https://github.com/pimoroni/py-smbus.git
    cd py-smbus/library
    python setup.py build
    sudo python setup.py install

    pip install mpu6050-raspberrypi
    '''

    def __init__(self, addr=0x68, poll_delay=0.0166):
        from mpu6050 import mpu6050
        self.sensor = mpu6050(addr)
        self.accel = { 'x' : 0., 'y' : 0., 'z' : 0. }
        self.gyro = { 'x' : 0., 'y' : 0., 'z' : 0. }
        self.temp = 0.
        self.poll_delay = poll_delay
        self.on = True

    def update(self):
        while self.on:
            self.poll()
            time.sleep(self.poll_delay)
                
    def poll(self):
        try:
            self.accel, self.gyro, self.temp = self.sensor.get_all_data()
        except:
            print('failed to read imu!!')
            
    def run_threaded(self):
        return self.accel['x'], self.accel['y'], self.accel['z'], self.gyro['x'], self.gyro['y'], self.gyro['z'], self.temp

    def run(self):
        self.poll()
        return self.accel['x'], self.accel['y'], self.accel['z'], self.gyro['x'], self.gyro['y'], self.gyro['z'], self.temp

    def shutdown(self):
        self.on = False


class Bno055:
    def __init__(self, serial_port='/dev/input/serial0', rst=18, poll_delay=0.0166):
        print("BNO Constructor {} => rst = {}".format(serial_port, rst))
        self.bno = BNO055(serial_port=serial_port, rst = rst)
        self.accel = {'x': 0., 'y': 0., 'z': 0.}
        self.gyro = {'x': 0., 'y': 0., 'z': 0.}
        self.temp = 0.
        self.poll_delay = poll_delay
        self.on = True
        if not self.bno.begin():
            raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

    def update(self):
        while self.on:
            self.poll()
            time.sleep(self.poll_delay)

    def poll(self):
        try:
            accx, accy, accz = self.bno.read_accelerometer()
            gyrx, gyry, gyrz = self.bno.read_gyroscope()
            self.temp = self.bno.read_temp

            self.accel['x'] = accx
            self.accel['y'] = accy
            self.accel['z'] = accz

            self.gyro['x'] = gyrx
            self.gyro['y'] = gyry
            self.gyro['z'] = gyrz
        except:
            print('failed to read imu!!')

    def run_threaded(self):
        return self.accel['x'], self.accel['y'], self.accel['z'], self.gyro['x'], self.gyro['y'], self.gyro[
            'z'], self.temp

    def run(self):
        self.poll()
        return self.accel['x'], self.accel['y'], self.accel['z'], self.gyro['x'], self.gyro['y'], self.gyro[
            'z'], self.temp

    def shutdown(self):
        self.on = False


if __name__ == "__main__":
    iter = 0
#    p = Mpu6050(
    bno = Bno055()
    while iter < 100:
        data = p.run()
        print(data)
        time.sleep(0.1)
        iter += 1
