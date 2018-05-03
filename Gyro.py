from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    gyro_pitch = "{pitch}".format(**sense.get_gyroscope())
    gyro_roll = "{roll}".format(**sense.get_gyroscope())
    gyro_yaw = "{yaw}".format(**sense.get_gyroscope())
    
    print(gyro_pitch, gyro_roll, gyro_yaw)
    sleep(1)
