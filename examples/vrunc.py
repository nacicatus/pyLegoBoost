# #!/usr/bin/env python3
# coding=utf-8
# Vernie run

from time import sleep
import time
from pylgbst import *
from pylgbst import get_connection_bleak
#from pylgbst.hub import MoveHub
from pylgbst.peripherals import EncodedMotor, COLOR_GREEN, COLOR_NONE
from vernie import *

#robot = Vernie()

def main():
    print("Run")
    conn=get_connection_bleak(hub_name='Move Hub')
    robot=Vernie()
    running=True
    
    robot.led.set_color(COLOR_GREEN)
    robot.button.subscribe(on_btn)
    robot.vision_sensor.subscribe(callback)
    robot.say("Place your hand in front of sensor")

    sleep(2.0)
    print("I'm tired")
        
    robot.vision_sensor.unsubscribe(callback)
    robot.button.unsubscribe(on_btn)
    conn.disconnect()
    
    
def callback(color, distance):
    robot.led.set_color(color)
    speed = (10 - distance + 1) / 10.0
    secs = (10 - distance + 1) / 10.0
    print("Distance is %.1f inches, I'm running back with %s%% speed!" % (distance, int(speed * 100)))
    if speed <= 1:
        robot.motor_AB.timed(secs / 1, -speed)
        robot.say("Ouch")


def on_btn(pressed):
    global running
    if pressed:
        running = False
                                                                                                                      
     
if __name__ == '__main__':
    main()
