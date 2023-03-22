from serial import Serial
import json

class Coms:
    def __init__(self, port):
	    self.serial = Serial(port)

    def write(self, obj):
        self.serial.write(json.dumps(obj))
