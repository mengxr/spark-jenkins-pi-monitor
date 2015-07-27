#!/usr/bin/env python

import time
from jenkinsapi.jenkins import Jenkins

try:
    import RPi.GPIO as gpio
    has_gpio = True
except:
    has_gpio = False
    
def setup_traffic_light():
    """setup the traffic light on pi"""
    gpio.setmode(gpio.BCM)
    for pin in [9, 10, 11]:
        gpio.setup(pin, gpio.OUT)

def check_spark_builds():
    """check Spark master and PR builds"""
    server = Jenkins("https://amplab.cs.berkeley.edu/jenkins/")
    master = server.get_job("Spark-Master-SBT")
    if master.get_last_completed_build().is_good():
        turn_off("r")
        turn_on("g", 3)
    else:
        turn_on("r")
    pr = server.get_job("SparkPullRequestBuilder")
    if pr.get_last_completed_build().is_good():
        turn_on("g", 2)
    else:
        turn_on("y", 3)
        
def get_pin(color):
    """traffic light color to GPIO pin mapping"""
    if color == "r":
        pin = 9
    elif color == "y":
        pin = 10
    elif color == "g":
        pin = 11
    else:
        raise RuntimeError("Do not support color %s." % color)    
        
def turn_on(color, duration=None):
    """turn on a traffic light for given duration"""
    if has_gpio:
        pin = get_pin(color)
        gpio.output(pin, True)
        if duration:
            time.sleep(duration)
            gpio.output(pin, False)
    else:
        msg = "Turn on %s light" % color
        if duration:
            msg += " for %d seconds" % duration
        print msg

        
def turn_off(color):
    """turn off a traffic light"""
    if has_gpio:
        pin = get_pin(color)
        gpio.output(pin, False)
    else:
        print "Turn off %s light" % color
        
if __name__ == "__main__":
    if has_gpio:
        setup_traffic_light()
    check_spark_builds()
