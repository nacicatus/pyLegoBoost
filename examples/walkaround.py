# #!/usr/bin/env python3
# coding=utf-8
# Walk around the Vernie  

from time import sleep
import time
from pylgbst import *
from pylgbst import get_connection_bleak
from pylgbst.hub import MoveHub
from pylgbst.peripherals import EncodedMotor
from vernie import *

robot=Vernie()

def main():
  print("Walking")
  conn=get_connection_bleak(hub_name='Move Hub')
  try:
    movehub = MoveHub(conn) #Connect to Move Hub
    # put your functions here:
    walk(movehub)
    sleep(1.0)
    print("Done")
  finally:
    conn.disconnect()

def walk(movehub):
    for level in range (0, 101):
        levels = level / 10.0
        movehub.motor_AB.timed(0.7,level)
        robot.say("Ouch")
        

def demo_motors_timed(movehub):
    print("Motors movement demo: timed")
    for level in range(0, 101, 10):
        levels = level / 100.0
        print(" Speed level: %s" %  levels)
        movehub.motor_A.timed(0.2, levels)
        movehub.motor_B.timed(0.2, -levels)
    print("now moving both motors with one command")    
    movehub.motor_AB.timed(1.5, -0.2, 0.2)
    movehub.motor_AB.timed(0.5, 1)
    movehub.motor_AB.timed(0.5, -1)


def demo_motors_angled(movehub):
    print("Motors movement demo: angled")
    for angle in range(0, 361, 90):
        print("Angle: %s" % angle)
        movehub.motor_B.angled(angle, 1)
        sleep(1)
        movehub.motor_B.angled(angle, -1)
        sleep(1)

    movehub.motor_AB.angled(360, 1, -1)
    sleep(1)
    movehub.motor_AB.angled(360, -1, 1)
    sleep(1)


def demo_port_cd_motor(movehub): # Move motor on port C or D
    print("Move external motor on Port C or D 45 degrees left & right")
    motor = None
    if isinstance(movehub.port_D, EncodedMotor):
        print("Rotation motor is on port D")
        motor = movehub.port_D
    elif isinstance(movehub.port_C, EncodedMotor):
        print("Rotation motor is on port C")
        motor = movehub.port_C
    else:
        print("Motor not found on ports C or D")
    if motor:
        print("Left")
        motor.angled(45, 0.3)
        sleep(2)
        motor.angled(45, -0.3)
        sleep(2)

        print("Right")
        motor.angled(45, -0.1)
        sleep(2)
        motor.angled(45, 0.1)
        sleep(2)


if __name__ == '__main__':
    main()

