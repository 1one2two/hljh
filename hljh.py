import time
from grove.i2c import Bus

import math
import RPi.GPIO as GPIO

ADC_DEFAULT_IIC_ADDR = 0X04

ADC_CHAN_NUM = 8

REG_RAW_DATA_START = 0X10
REG_VOL_START = 0X20
REG_RTO_START = 0X30

REG_SET_ADDR = 0XC0


class Pi_hat_adc():
    def __init__(self,bus_num=1,addr=ADC_DEFAULT_IIC_ADDR):
        self.bus=Bus(bus_num)
        self.addr=addr
        
    def get_all_vol_milli_data(self):
        array = []
        for i in range(ADC_CHAN_NUM):  
            data=self.bus.read_i2c_block_data(self.addr,REG_VOL_START+i,2)
            val=data[1]<<8|data[0]
            array.append(val)
        return array

def basic_distance(trig_pin, echo_pin, celsius=20):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    speed_of_sound = 331.3 * math.sqrt(1+(celsius / 273.15))
    GPIO.setup(trig_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)
    GPIO.output(trig_pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(trig_pin, True)
    time.sleep(0.00001)
    GPIO.output(trig_pin, False)
    echo_status_counter = 1
    time_out = False
    while GPIO.input(echo_pin) == 0:
        if echo_status_counter < 1000:
            sonar_signal_off = time.time()
            echo_status_counter += 1
        else:
            sonar_signal_off = time.time()
	    time_out = True
            break
            #raise SystemError('No echo')
    if time_out == False:
    	while GPIO.input(echo_pin) == 1:
    	    sonar_signal_on = time.time()
    else:
        sonar_signal_on = time.time()
        
    time_passed = sonar_signal_on - sonar_signal_off
    return time_passed * ((speed_of_sound * 100) / 2)

ADC = Pi_hat_adc()
def main():
    vol_data=ADC.get_all_vol_milli_data()
    #print('{\"0\":\"' + str(vol_data[0]) + '\",\"1\":\"'+ str(basic_distance(11, 13, 20)) +'\"}')
    print(str(basic_distance(11, 13, 20)) + "," + str(vol_data[0]))

if __name__ == '__main__':
    main()