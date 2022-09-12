import time
import pyb
from machine import Pin

pyb.enable_irq()

HOUR = 60 * 60
MINUTE = 60

alloted_time = 25 * MINUTE

# formats time
def tft(seconds):
    #hours = int(seconds / HOUR)
    # seconds % HOUR = remaining minutes
    minutes = int((seconds % HOUR) / MINUTE)
    # same thing as: seconds % MINUTE / 1 second
    seconds = seconds % MINUTE

    #print("{0}::{1}::{2}".format(hours, minutes, seconds))
    return("{0}:{1}".format(minutes, seconds))

def timer(alloted_time):
    now = time.time()
    then = time.time()

    elapsed = 0

    elapsed_time = alloted_time + elapsed
    
    while (elapsed_time) >= 0:
        then = time.time()
        elapsed = int(now - then)
        elapsed_time = alloted_time + elapsed

        #print(elapsed)
        print("\rtime: {0}".format(tft(elapsed_time)), end=' ')


def main():
    timer(alloted_time)    
    tft(61)

main()
