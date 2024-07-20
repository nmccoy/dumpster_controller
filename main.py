try:
    import usocket as socket
except:
    import socket

from machine import Pin
import machine

# import network

import esp

esp.osdebug(None)

import gc
import time

gc.collect()

# ssid = "Not My Real Wifi"
# password = "lol"
# station = network.WLAN(network.STA_IF)
# station.active(True)
# station.connect(ssid, password)

# Oops, want to test this when wifi isn't working
# while station.isconnected() == False:
#  pass
# print('Connection successful!!')
# print(station.ifconfig())

led = Pin(2, Pin.OUT)
dumpster = Pin(19, Pin.OUT)
fire1 = Pin(5, Pin.OUT)
fire2 = Pin(18, Pin.OUT)

dumpster.value(1)
fire_state = False

# Was this a watchdog reset?
if machine.reset_cause() == machine.WDT_RESET:
    print("Doggy doggy what now?")
else:
    print("Something else this time")

# Give me time to interrupt before enabling WDT.
def give_me_some_time():
    for _ in range(20):
        led(True)
        time.sleep(0.25)
        led(False)
        time.sleep(0.25)


give_me_some_time()

# enable watchdog with a timeout of 2s
watchdog = machine.WDT(timeout=2000)
watchdog.feed()


def toggle_fire():
    global fire_state
    new_state = not fire_state
    led(fire_state)
    fire1(fire_state)
    fire2(new_state)
    fire_state = new_state


while True:
    toggle_fire()
    time.sleep(0.8)
    watchdog.feed()
