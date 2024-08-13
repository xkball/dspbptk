import struct

from DysonFrameData import DysonFrameData
from DysonNodeData import DysonNodeData
from DysonShellData import DysonShellData


class DysonSphereLayerData:

    def __init__(self):
        self.nodeCapacity = 0
        self.nodeCursor = 0
        self.nodeRecycleCursor = 0
        self.nodePool = [None]
        self.nodeRecycle = []

        self.frameCapacity = 0
        self.frameCursor = 0
        self.frameRecycleCursor = 0
        self.framePool = [None]
        self.frameRecycle = []

        self.shellCapacity = 0
        self.shellCursor = 0
        self.shellRecycleCursor = 0
        self.shellPool = [None]
        self.shellRecycle = []

        self.paintGridMode = 0
        self.cellColors = []

    def parse(self,stream):
        _head = stream.readInt()
        assert _head == 1
        self.nodeCapacity = stream.readInt()
        self.nodeCursor = stream.readInt()
        self.nodeRecycleCursor = stream.readInt()
        for i in range(1,self.nodeCursor):
            if stream.readInt() == i:
                self.nodePool.append(DysonNodeData().parse(stream))
            else:
                self.nodePool.append(None)
        for i in range(0,self.nodeRecycleCursor):
            self.nodeRecycle.append(stream.readInt())

        self.frameCapacity = stream.readInt()
        self.frameCursor = stream.readInt()
        self.frameRecycleCursor = stream.readInt()
        for i in range(1,self.frameCursor):
            if stream.readInt() == i:
                self.framePool.append(DysonFrameData().parse(stream))
            else:
                self.framePool.append(None)
        for i in range(0,self.frameRecycleCursor):
            self.frameRecycle.append(stream.readInt())

        self.shellCapacity = stream.readInt()
        self.shellCursor = stream.readInt()
        self.shellRecycleCursor = stream.readInt()
        for i in range(1,self.shellCursor):
            if stream.readInt() == i:
                self.shellPool.append(DysonShellData().parse(stream))
            else:
                self.shellPool.append(None)
        for i in range(0,self.shellRecycleCursor):
            self.shellRecycle.append(stream.readInt())
        self.paintGridMode = stream.readInt()
        if stream.readBool():
            length = stream.readInt()
            for i in range(0,length):
                color = [stream.readInt(),stream.readInt(),stream.readInt(),stream.readInt()]
                self.cellColors.append(color)
        return self

    def to_dict(self):
        return {
            'nodeCapacity': self.nodeCapacity,
            'nodeCursor': self.nodeCursor,
            'nodeRecycleCursor': self.nodeRecycleCursor,
            'nodePool': [node.to_dict() if node is not None else {} for node in self.nodePool],
            'nodeRecycle': self.nodeRecycle,
            'frameCapacity': self.frameCapacity,
            'frameCursor': self.frameCursor,
            'frameRecycleCursor': self.frameRecycleCursor,
            'framePool': [frame.to_dict() if frame is not None else {} for frame in self.framePool],
            'frameRecycle': self.frameRecycle,
            'shellCapacity': self.shellCapacity,
            'shellCursor': self.shellCursor,
            'shellRecycleCursor': self.shellRecycleCursor,
            'shellPool': [shell.to_dict() if shell is not None else {} for shell in self.shellPool],
            'shellRecycle': self.shellRecycle,
            'paintGridMode': self.paintGridMode,
            'cellColors': self.cellColors
        }