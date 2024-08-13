
class DysonShellData:
    def __init__(self):
        self.id = 0
        self.protoID = 0
        self.randSeed = 0
        self.color = []
        self.nodes = []

    def parse(self,stream):
        head = stream.readInt()
        assert head == 2
        self.id = stream.readInt()
        self.protoID = stream.readInt()
        self.randSeed = stream.readInt()
        self.color.append(stream.readByte())
        self.color.append(stream.readByte())
        self.color.append(stream.readByte())
        self.color.append(stream.readByte())
        nodeCount = stream.readInt()
        for i in range(nodeCount):
            self.nodes.append(stream.readInt())
        return self

    def to_dict(self):
        return {
            'id': self.id,
            'protoID': self.protoID,
            'randSeed': self.randSeed,
            'color': [byte[0] for byte in self.color],
            'nodes': self.nodes
        }