from machine import Pin
import time

button = Pin(13, Pin.IN)

while True:
    time.sleep(1)
    print(button.value())
