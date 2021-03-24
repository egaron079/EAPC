import zlib
import random
import string

def compress(files):
    with open("attacks.eap", "ab") as m:
        # write the header
        m.write(b"EAPC")
        for a in range(12):
            m.write(b"\x00")
    for file in files:
        with open(file, "rb") as i:
            data = i.read()
            cData = zlib.compress(data)
        with open("attacks.eap", "ab") as m:
            m.write(bytes(file, "ascii"))
            for b in range(16 - len(file)):
                m.write(b"\x00")
            # write compressed data
            m.write(cData)
            for d in range(64 - len(cData)):
                m.write(b"\x00")

def decompress(files):
    for file in files:
        with open(file, "rb") as m:
            data = m.read()[16:]
            chunks = [data[a: a + 80] for a in range(0, len(data), 80)]
            for chunk in chunks:
                filename = chunk[0:16].strip(b"\x00")
                chunkData = chunk[16:]
                with open(str(chunk[0:16].strip(b"\x00")).lstrip("b'").rstrip("'"), "ab") as f:
                    f.write(zlib.decompress(chunkData))