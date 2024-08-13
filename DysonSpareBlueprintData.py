import io
import struct

from ByteStream import ByteStream
from DysonOrbitBlueprintData import DysonOrbitBlueprintData
from DysonSphereLayerData import DysonSphereLayerData


def readMask(mask):
    if mask >= 0:
        return bin(mask)[2:].zfill(32)
    else:
        max_value = 1 << 32
        return bin(max_value + mask)[2:].zfill(32)

class DysonSpareBlueprintData:

    def __init__(self):
        self.timestamp = 0
        self.gameVersion = ""
        self.type = 0

        self.latLimit = 0
        self.editorRenderMaskS = 0
        self.gameRenderMaskS = 0
        self.swarmOrbits = []
        self.sailOrbitColorHSVA = []

        self.editorRenderMaskL = 0
        self.gameRenderMaskL = 0
        self.layerOrbits = []
        self.layers = []
        self.singleLayer = None

    def parse(self,head,data):
        (unused_head,self.timestamp,self.gameVersion,self.type,self.latLimit) = head.split(',')
        assert unused_head == 'DYBP:0'
        stream = ByteStream(io.BytesIO(data))
        stream.read(4)
        if self.type == "3" or self.type == "4":
            self.editorRenderMaskS = stream.readInt()
            self.gameRenderMaskS = stream.readInt()
            for i in range(0,20):
                self.swarmOrbits.append(DysonOrbitBlueprintData().parse(stream.read(29)))
            colorLength = stream.readInt()
            for i in range(0,colorLength):
                self.sailOrbitColorHSVA.append(
                    (stream.readFloat(),
                     stream.readFloat(),
                     stream.readFloat(),
                     stream.readFloat())
                )
        if self.type == "2" or self.type == "4":
            self.editorRenderMaskL = stream.readInt()
            self.gameRenderMaskL = stream.readInt()
            length = stream.readInt()
            for i in range(0,length):
                if stream.readBool():
                    self.layerOrbits.append(DysonOrbitBlueprintData().parse(stream.read(29)))
                else:
                    self.layerOrbits.append(None)
            length = stream.readInt()
            for i in range(0,length):
                if stream.readBool():
                    self.layers.append(DysonSphereLayerData().parse(stream))
                else:
                    self.layers.append(None)
        if self.type == "1":
            self.singleLayer = DysonSphereLayerData().parse(stream)
        return self

    def to_dict(self):
        ds = {
                'editorRenderMaskS': readMask(self.editorRenderMaskS),
                'gameRenderMaskS': readMask(self.gameRenderMaskS),
                'swarmOrbits': [orbit.to_dict() for orbit in self.swarmOrbits],
                'sailOrbitColorHSVA': [[color[0],color[1],color[2],color[3]] for color in self.sailOrbitColorHSVA],
            }
        dl = {
            'editorRenderMaskL': readMask(self.editorRenderMaskL),
            'gameRenderMaskL': readMask(self.gameRenderMaskL),
            'layerOrbits': [orbit.to_dict() if orbit is not None else {} for orbit in self.layerOrbits],
            'layers': [layer.to_dict() if layer is not None else {} for layer in self.layers],
        }
        if self.type == "1":
            return {
                'timestamp': self.timestamp,
                'gameVersion': self.gameVersion,
                'type': self.type,
                'latLimit': self.latLimit,
                'singleLayer': self.singleLayer.to_dict(),
            }
        if self.type == "2":
            return {
                'timestamp': self.timestamp,
                'gameVersion': self.gameVersion,
                'type': self.type,
                'latLimit': self.latLimit,
                'dysonLayers' : dl
            }
        if self.type == "3":
            return {
                'timestamp': self.timestamp,
                'gameVersion': self.gameVersion,
                'type': self.type,
                'latLimit': self.latLimit,
                'dysonSwarm': ds
            }
        return {
            'timestamp': self.timestamp,
            'gameVersion': self.gameVersion,
            'type': self.type,
            'latLimit': self.latLimit,
            'dysonSwarm' : ds,
            'dysonLayers': dl
            }