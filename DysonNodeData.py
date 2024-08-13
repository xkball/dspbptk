
class DysonNodeData:
    def __init__(self):
        self.id = 0
        self.protoID = 0
        self.use = 0
        self.reserved = False
        self.pos = []
        self.spMax = 0
        self.rid = 0
        self.frameTurn = 0
        self.shellTurn = 0
        self._spReq = 0
        self._cpReq = 0
        self.color = []

    def parse(self,stream):
        head = stream.readInt()
        assert head == 5
        self.id = stream.readInt()
        self.protoID = stream.readInt()
        self.use = stream.readBool()
        self.reserved = stream.readBool()
        self.pos.append(stream.readFloat())
        self.pos.append(stream.readFloat())
        self.pos.append(stream.readFloat())
        self.spMax = stream.readInt()
        self.rid = stream.readInt()
        self.frameTurn = stream.readInt()
        self.shellTurn = stream.readInt()
        self._spReq = stream.readInt()
        self._cpReq = stream.readInt()
        self.color.append(stream.readByte())
        self.color.append(stream.readByte())
        self.color.append(stream.readByte())
        self.color.append(stream.readByte())
        return self

    def to_dict(self):
        return {
            'id': self.id,
            'protoID': self.protoID,
            'use': self.use,
            'reserved': self.reserved,
            'pos': self.pos,
            'spMax': self.spMax,
            'rid': self.rid,
            'frameTurn': self.frameTurn,
            'shellTurn': self.shellTurn,
            '_spReq': self._spReq,
            '_cpReq': self._cpReq,
            'color': [byte[0] for byte in self.color]
        }