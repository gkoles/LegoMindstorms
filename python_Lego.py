#!/usr/bin/env python3
from time import sleep
from ev3dev.auto import *

# Wind Left Motor
def wind_left(lmotor):

    reverse = -1
    # interval = 900000
    interval = 3000
    speed = 140

    counter  = 5

    while counter and not button.any():

        # Clockwise cycle
        lmotor.run_timed(speed_sp = speed * direction, time_sp = interval)

        #Test program execution
        motor.wait_while('running')
        Sound.beep()

        # Counter clockwise cycle
        lmotor.run_timed(speed_sp = speed * reverse, time_sp = interval)


        #Test program execution
        motor.wait_while('running')
        Sound.speak()

        counter -= 1

    return


# Run the program
if __name__ == '__main__':

    # Connect two large motors on output ports A and C
    lmotor, rmotor = [LargeMotor(address) for address in (OUTPUT_A, OUTPUT_C)]

    # Check that the motors are actually connected
    assert lmotor.connected
    assert rmotor.connected

    # Connect the medium motor on output B
    # mmotor = MediumMotor(OUTPUT_B)
    # assert mmotor.connected

    # Connect touch sensor and remote control
    # ts = TouchSensor();   assert ts.connected
    # rc = RemoteControl(); assert rc.connected

    # Initialize button handler
    button = Button()

    # Turn leds off
    Leds.all_off()

    # run the winder
    left_winder = wind_left(lmotor, Leds)
    left_winder.main()
