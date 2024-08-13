
class DysonFrameData:
    def __init__(self):
        self.id = 0
        self.protoID = 0
        self.reserved = False
        self.nodeAID = 0
        self.nodeBID = 0
        self.euler = False
        self.spMax = 0
        self.color = []

    def parse(self,stream):
        head = stream.readInt()
        assert head == 1
        self.id = stream.readInt()
        self.protoID = stream.readInt()
        self.reserved = stream.readBool()
        self.nodeAID = stream.readInt()
        self.nodeBID = stream.readInt()
        self.euler = stream.readBool()
        self.spMax = stream.readInt()
        self.color.append(stream.readByte())
        self.color.append(stream.readByte())
        self.color.append(stream.readByte())
        self.color.append(stream.readByte())
        return self

    def to_dict(self):
        return {
            'id': self.id,
            'protoID': self.protoID,
            'reserved': self.reserved,
            'nodeAID': self.nodeAID,
            'nodeBID': self.nodeBID,
            'euler': self.euler,
            'spMax': self.spMax,
            'color': [byte[0] for byte in self.color]
        }
