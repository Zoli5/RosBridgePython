#!/usr/bin/env python

from ws4py.client.threadedclient import WebSocketClient
from json import dumps
import jsonpickle


class RosBridgePython(WebSocketClient):
    connected = False

    def opened(self):
        self.connected = True

    def closed(self, code, reason=None):
        print(code, reason)

    def received_message(self, m):
        print("received", m)

    def publish(self, receiver, type, msg):
        if receiver is None or type is None or msg is None:
            raise AttributeError
        if not self.connected:
            raise Exception("No connection!")
        print('Connected!')
        m = self.Message(receiver, type, msg)
        needtosend = jsonpickle.dumps(m)
        # msga = {'receiver': '/turtle1/command_velocity', 'type': 'turtlesim/Velocity', 'msg': {'linear': 20.0, 'angular': 20.0}}
        # msgb = {"receiver": "/turtle1/command_velocity", "type": "turtlesim/Velocity", "msg": {"linear": 20.0, "angular": 20.0}}
        print(needtosend)
        self.send(needtosend)
        print('Message sent!')

    #def PublishString:

    #def Subscribe:

    #def CloseConnection:

    class Message:
        def __init__(self, receiver, type, msg):
            self.receiver = receiver
            self.type = type
            self.msg = msg

    class TurtleSim:
        def __init__(self, linear, angular):
            self.linear = linear
            self.angular = angular

    #class Neobotix:

    #class FreeString:
