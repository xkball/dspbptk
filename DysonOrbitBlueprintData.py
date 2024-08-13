import struct


class DysonOrbitBlueprintData:

    _STRUCT = struct.Struct("<iifffff?")

    def __init__(self):
        self.id = 0
        self.radius = 0
        self.rx = 0
        self.ry = 0
        self.rz = 0
        self.rw = 0
        self.enable = False

    def to_dict(self):
        return {
            'id': self.id,
            'radius': self.radius,
            'rotation' : [ self.rx, self.ry, self.rz, self.rw ],
            'enable': self.enable
        }

    def parse(self, _bytes):
        data = self._STRUCT.unpack_from(_bytes)
        self.id = data[1]
        self.radius = data[2]
        self.rx = data[3]
        self.ry = data[4]
        self.rz = data[5]
        self.rw = data[6]
        self.enable = data[7]
        return self

