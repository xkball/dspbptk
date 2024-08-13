import struct


class ByteStream:

    _INT_READER = struct.Struct('<i')
    _FLOAT_READER = struct.Struct('<f')
    _BOOL_READER = struct.Struct('<?')

    def __init__(self,stream):
        self.stream=stream

    def readInt(self):
        return self._INT_READER.unpack(self.stream.read(4))[0]

    def readFloat(self):
        return self._FLOAT_READER.unpack(self.stream.read(4))[0]

    def readBool(self):
        return self._BOOL_READER.unpack(self.stream.read(1))[0]

    def readByte(self):
        return self.stream.read(1)

    def read(self,length):
        return self.stream.read(length)