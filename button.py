from machine import Pin

button = Pin(1, Pin.IN)

while True:
    print(button.value())
    if button.value() == 1:
        print(1)
