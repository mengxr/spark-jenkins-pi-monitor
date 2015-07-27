#A Spark Jenkins monitor on Raspberry Pi

This repo implements a simple [Spark Jenkins](https://amplab.cs.berkeley.edu/jenkins/) monitor using a traffic light on Raspberry Pi.

* If Spark master build failed, we turn on the red light.
* If Spark master build succeeded, we turn off the red light (if it is on) and flash the green light.
* If Spark pull request build failed, we flash the yellow light.
* If Spark pull request build succeeded, we flash the green light.

## Setup

You need

* a [Raspberry Pi](https://www.raspberrypi.org)
* a [traffic light for Pi](http://www.amazon.com/dp/B00RIIGD30)

Install the traffic light on [GND and 11/9/10 GPIO pins](http://wiki.lowvoltagelabs.com/pitrafficlight). Then do the following as root:

~~~
# apt-get install python-rpi.gpio
# curl -L https://github.com/mengxr/spark-jenkins-pi-monitor/raw/master/spark_jenkins_pi_monitor.py -o /usr/local/bin/spark_jenkins_pi_monitor.py
# chmod +x /usr/local/bin/spark_jenkins_pi_monitor.py
# crontab -e
*/2 * * * * /usr/local/bin/spark_jenkins_pi_monitor.py
~~~