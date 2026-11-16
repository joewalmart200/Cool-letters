#!/usr/bin/env python3
import sys
import argparse


Raw = {
    "A": ".XXX./X...X/XXXXX/X...X/X...X",
    "B": "XXXX./X...X/XXXX./X...X/XXXX.",
    "C": ".XXXX/X..../X..../X..../.XXXX",
    "D": "XXXX./X...X/X...X/X...X/XXXX.",
    "E": "XXXXX/X..../XXXX./X..../XXXXX",
    "F": "XXXXX/X..../XXXX./X..../X....",
    "G": ".XXXX/X..../X..XX/X...X/.XXXX",
    "H": "X...X/X...X/XXXXX/X...X/X...X",
    "I": "XXXXX/..X../..X../..X../XXXXX",
    "J": "..XXX/....X/....X/X...X/.XXX.",
    "K": "X...X/X..X./XXX../X..X./X...X",
    "L": "X..../X..../X..../X..../XXXXX",
    "M": "X...X/XX.XX/X.X.X/X...X/X...X",
    "N": "X...X/XX..X/X.X.X/X..XX/X...X",
    "O": ".XXX./X...X/X...X/X...X/.XXX.",
    "P": "XXXX./X...X/XXXX./X..../X....",
    "Q": ".XXX./X...X/X.X.X/X..X./.XX.X",
    "R": "XXXX./X...X/XXXX./X..X./X...X",
    "S": ".XXXX/X..../.XXX./....X/XXXX.",
    "T": "XXXXX/..X../..X../..X../..X..",
    "U": "X...X/X...X/X...X/X...X/.XXX.",
    "V": "X...X/X...X/X...X/.X.X./..X..",
    "W": "X...X/X...X/X.X.X/XX.XX/X...X",
    "X": "X...X/.X.X./..X../.X.X./X...X",
    "Y": "X...X/.X.X./..X../..X../..X..",
    "Z": "XXXXX/...X./..X../.X.../XXXXX",
    "0": ".XXX./X..XX/X.X.X/XX..X/.XXX.",
    "1": "..X../.XX../..X../..X../.XXX.",
    "2": ".XXX./X...X/..XX./.X.../XXXXX",
    "3": "XXXX./....X/.XXX./....X/XXXX.",
    "4": "X..X./X..X./XXXXX/...X./...X.",
    "5": "XXXXX/X..../XXXX./....X/XXXX.",
    "6": ".XXX./X..../XXXX./X...X/.XXX.",
    "7": "XXXXX/....X/...X./..X../..X..",
    "8": ".XXX./X...X/.XXX./X...X/.XXX.",
    "9": ".XXX./X...X/.XXXX/....X/.XXX.",
    "!": "X/X/X/./X",
    "?": ".XXX./X...X/..XX./...../..X..",
    ".": "././././X",
    "-": "...../...../XXXXX/...../.....",
    " ": ".../.../.../.../...",
}

ROWS = 5


def _unpack(blob):
    return blob.split("/")


GLYPHS = {k: _unpack(v) for k, v in RAW.items()}


def shout(msg, pen="█", size=1, gap=1):
    lines = []
    for r in range(ROWS):
        bits = []
        for c in msg.upper():
           
            g = GLYPHS.get(c, GLYPHS["?"])
            bits.append(g[r])
        
        line = (" " * gap).join(bits)
        line = line.replace("X", pen).replace(".", " ")
        
        line = "".join(ch * (size * 2) for ch in line).rstrip()
        
        lines += [line] * size
    return "\n".join(lines)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="big text for your terminal")
    ap.add_argument("words", nargs="*", help="what to say")
    ap.add_argument("-p", "--pen", default="█", help="char to draw with")
    ap.add_argument("-s", "--size", type=int, default=1)
    ap.add_argument("-g", "--gap", type=int, default=1, help="space between letters")

    msg = " ".join(a.words) if a.words else input("say what? ")
    if not msg.strip():
        sys.exit("nothing to say, huh")

    print(shout(msg, a.pen[:1] or "█", max(1, a.size), max(0, a.gap)))
