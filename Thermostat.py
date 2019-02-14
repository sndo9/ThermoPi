import threading
import time
import Adafruit_DHT
import math

import RPi.GPIO as GPIO

calibration = 0

target_temperature = 74

fan_delay = 20

fan = 17
heat = 22
cool = 27

ctrl_channels = (fan, heat, cool)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ctrl_channels, GPIO.OUT)
GPIO.output(ctrl_channels, GPIO.HIGH)

# MODES
# 1 IS HEAT
# 0 IS OFF
# -1 IF COOL
class Function():
    function = 0

class Temperature_monitor(threading.Thread):
    def turn_on_heat(a):
        GPIO.output(heat, GPIO.LOW)
        time.sleep(fan_delay)
        GPIO.output(fan, GPIO.LOW)

    def turn_off_heat(a):
        GPIO.output(heat, GPIO.HIGH)
        time.sleep(fan_delay)
        GPIO.output(fan, GPIO.HIGH)
    
    def __init__(self, current_mode):
        threading.Thread.__init__(self)
        
    def run(self):
        for i in range(0, 10):
            humidity, temperature = Adafruit_DHT.read_retry(22, 4)
            temperature = temperature * 9/5.0 + 32 + calibration

            if mode.function == 1:
                print "In heat mode"
                if math.floor(temperature) < target_temperature and GPIO.input(heat) == GPIO.HIGH:
                    self.turn_on_heat()
                    print "Turning on furnace"

                if math.floor(temperature) >= target_temperature and GPIO.input(heat) == GPIO.LOW:
                    self.turn_off_heat()
                    print "Turning off furnace"

            if mode.function == -1:
                print "In cool mode"
                if math.floor(temperature) > target_temperature and GPIO.input(cool) == GPIO.HIGH:
                    turn_on_cool()
                    print "Turning on air conditioner"

                if math.floor(temperature) <= target_temperature and GPIO.input(cool) == GPIO.LOW:
                    turn_off_cool()
                    print "Turning off air conditioner"

            print str(temperature) + " " + str(target_temperature) + " " + str(math.floor(temperature) >= target_temperature)

    def turn_on_cool():
        GPIO.output(cool, GPIO.LOW)
        time.sleep(fan_delay)
        GPIO.output(cool, GPIO.LOW)

    def turn_off_cool():
        GPIO.output(cool, GPIO.HIGH)
        time.sleep(fan_delay)
        GPIO.output(cool, GPIO.HIGH)

mode = Function()
mode.function = 1
thermostat = Temperature_monitor(mode)
thermostat.start()
thermostat.join()
