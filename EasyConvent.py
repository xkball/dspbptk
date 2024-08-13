import gzip
import base64
import json
import struct
from win32 import win32clipboard
import time

from DysonSpareBlueprintData import DysonSpareBlueprintData


def main():
    raw10000 = "H4sIAAAAAAAAC2NgYGD4DwVAJgMjiHCQcWNAAQ32jAyjYBQQBgpAvMKiz9bYeLMdKN2A8BM0Prr8KH948QFoAqzIVAQAAA=="
    raw10001 = "H4sIAAAAAAAAC2NgYGD4DwVAJgMjiHCRcWNAAQ32jAyjYBQQBgpAvMKiz9bYeLMdKN2A8BM0Prr8KH948QGZrg7eVAQAAA=="
    raw2 =     "H4sIAAAAAAAAC2NgYGD4DwVAJgMjiHCQcWNAAQ32YHEmELGgx1Vv7+7Nb9d2LgdJ6O21NmZkGAWjAAwUgHiFRZ+tsfFmO1DyAOFR/sjiAwBoQnWMVAQAAA=="
    raw3 =     "H4sIAAAAAAAAC2NgYGD4DwVAJgMjiHCQcWNAAQ32YHEmELGgx1Vv7+7Nb9d2LgdJ6O21NgZLMoMIF4jOfT/59oDoxr/1EJ2jYIQABSBeYdFna2y82Q6UPEB4lD+y+AA21x4LVAQAAA=="
    # compressed_data = base64.b64decode(raw3)
    # data = gzip.decompress(compressed_data)
    offset = 20
    raw = ""
    rawold = ""
    while True:
        time.sleep(0.5)
        try:
            win32clipboard.OpenClipboard()
            raw = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
            win32clipboard.CloseClipboard()
        except:
            pass
        if(raw != rawold):
            rawold = raw
            b64data_hash_split = raw.split("\"")
            if(len(b64data_hash_split) != 3):
                continue
            (long_desc, b64data, hash_value) = b64data_hash_split
            compressed_data = base64.b64decode(b64data)
            data = gzip.decompress(compressed_data)
            ds_bp_data = DysonSpareBlueprintData().parse(long_desc,data)
            #json_str = json.dumps(ds_bp_data.to_dict(),indent=4)
            with open("test_output.json", "w") as f:
                json.dump(ds_bp_data.to_dict(),f, indent=4)
            # for byte in data[offset:offset+20]:
            #     print(f"{byte:0x}",end = "")
            #     
            # print("")
            # for byte in data[20:40]:
            #     print(f"{byte:08b}",end = " ")
            # print("")
            # for byte in data[29*20:]:
            #     print(byte,end = "")
            #     
            # print("")
            # for byte in data[32:40]:
            #     print(byte,end = " ")
            # print("")
            # dou = struct.unpack('<d',data[32:40])
            # print(dou)
    # for byte in data[offset:offset+20]:
    #     b = struct.unpack('<B', struct.pack('>B', byte))[0]
    #     print(f"{b:08b}",end = " ")
    # print("")
    # for byte in data[offset:offset+20]:
    #     b = struct.unpack('<B', struct.pack('>B', byte))[0]
    #     print(f"{b:8}",end = " ")
    # print("")


main()