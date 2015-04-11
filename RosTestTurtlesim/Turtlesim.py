#!/usr/bin/env python

from RosBridgePython.RosBridgePython import *

if __name__ == "__main__":
    topic = "/turtle1/command_velocity"
    msgtype = "turtlesim/Velocity"
    turtleGo = RosBridgePython.TurtleSim(20, 20)
    try:
        ts = RosBridgePython('ws://192.168.111.133:9090/')
        ts.opened()
        ts.connect()
        ts.publish(topic, msgtype, turtleGo)
    finally:
        ts.close()