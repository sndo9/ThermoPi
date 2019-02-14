import threading
import time
import Adafruit_DHT

calibration = 0

class Temperature_monitor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(22, 4)
            temperature = temperature * 9/5.0 + 32 + calibration

            print temperature
            time.sleep(3)

thermostat = Temperature_monitor()
thermostat.start()
thermostat.join()
