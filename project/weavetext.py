from ledutils import addPixels
import opc

strip = []
black = (0,0,0)
purple = (130,0,255)


# (13) 151 344 13131 24 (14)
addPixels(strip, 13, black)

addPixels(strip, 1, purple)
addPixels(strip, 5, black)
addPixels(strip, 1, purple)

addPixels(strip, 3, black)
addPixels(strip, 4, purple)
addPixels(strip, 4, black)

addPixels(strip, 1, purple)
addPixels(strip, 3, black)
addPixels(strip, 1, purple)
addPixels(strip, 3, black)
addPixels(strip, 1, purple)

addPixels(strip, 2, black)
addPixels(strip, 4, purple)
addPixels(strip, 14, black)

# (13) 15121 7111 213 111 4 (14)
addPixels(strip, 13, black)

addPixels(strip, 1, purple)
addPixels(strip, 5, black)
addPixels(strip, 1, purple)
addPixels(strip, 2, black)
addPixels(strip, 1, purple)

addPixels(strip, 7, black)
addPixels(strip, 1, purple)
addPixels(strip, 1, black)
addPixels(strip, 1, purple)

addPixels(strip, 2, black)
addPixels(strip, 1, purple)
addPixels(strip, 3, black)

addPixels(strip, 1, purple)
addPixels(strip, 1, black)
addPixels(strip, 1, purple)

addPixels(strip, 18, black)

# (13) 151 235 111 213 113 (16)
addPixels(strip, 13, black)

addPixels(strip, 1, purple)
addPixels(strip, 5, black)
addPixels(strip, 1, purple)

addPixels(strip, 2, black)
addPixels(strip, 3, purple)
addPixels(strip, 5, black)

addPixels(strip, 1, purple)
addPixels(strip, 1, black)
addPixels(strip, 1, purple)

addPixels(strip, 2, black)
addPixels(strip, 1, purple)
addPixels(strip, 3, black)

addPixels(strip, 1, purple)
addPixels(strip, 1, black)
addPixels(strip, 3, purple)

addPixels(strip, 16, black)

# (14) 11111 316 11111 2111 21 (18)
addPixels(strip, 14, black)

addPixels(strip, 1, purple)
addPixels(strip, 1, black)
addPixels(strip, 1, purple)
addPixels(strip, 1, black)
addPixels(strip, 1, purple)

addPixels(strip, 3, black)
addPixels(strip, 1, purple)
addPixels(strip, 6, black)

addPixels(strip, 1, purple)
addPixels(strip, 1, black)
addPixels(strip, 1, purple)
addPixels(strip, 1, black)
addPixels(strip, 1, purple)

addPixels(strip, 2, black)
addPixels(strip, 1, purple)
addPixels(strip, 1, black)
addPixels(strip, 1, purple)

addPixels(strip, 2, black)
addPixels(strip, 1, purple)

addPixels(strip, 18, black)

# (14) 11111 316 131  2111 21 (18)
addPixels(strip, 14, black)

addPixels(strip, 1, purple)
addPixels(strip, 1, black)
addPixels(strip, 1, purple)
addPixels(strip, 1, black)
addPixels(strip, 1, purple)

addPixels(strip, 3, black)
addPixels(strip, 1, purple)
addPixels(strip, 6, black)

addPixels(strip, 1, purple)
addPixels(strip, 3, black)
addPixels(strip, 1, purple)

addPixels(strip, 2, black)
addPixels(strip, 1, purple)
addPixels(strip, 1, black)
addPixels(strip, 1, purple)

addPixels(strip, 2, black)
addPixels(strip, 1, purple)

addPixels(strip, 18, black)

# (15) 111 542 131 314 4 (14)
addPixels(strip, 15, black)

addPixels(strip, 1, purple)
addPixels(strip, 1, black)
addPixels(strip, 1, purple)

addPixels(strip, 5, black)
addPixels(strip, 4, purple)
addPixels(strip, 2, black)

addPixels(strip, 1, purple)
addPixels(strip, 3, black)
addPixels(strip, 1, purple)

addPixels(strip, 3, black)
addPixels(strip, 1, purple)
addPixels(strip, 4, black)

addPixels(strip, 4, purple)
addPixels(strip, 14, black)


ADDRESS = 'localhost:7890'
client = opc.Client(ADDRESS)
client.put_pixels(strip)
client.put_pixels(strip)