from ledutils import addPixels
import opc

strip = []
black = (0,0,0)
purple = (194,106,221)
blue = (160,218,242)
white = (255,255,255)
yellow = (255,255,81)
orange = (255,172,48)
pink = (255,137,198)

# 1
addPixels(strip, 7,black)
addPixels(strip, 4,purple)
addPixels(strip, 4,black)

addPixels(strip, 3,blue)
addPixels(strip, 2,black)

addPixels(strip, 5,white)
addPixels(strip, 2,black)

addPixels(strip, 2,yellow)
addPixels(strip, 2,black)
addPixels(strip, 1,yellow)
addPixels(strip, 2,black)

addPixels(strip, 4,orange)
addPixels(strip, 4,black)

addPixels(strip, 3,pink)
addPixels(strip, 3,black)

addPixels(strip, 1,purple)
addPixels(strip, 3,black)
addPixels(strip, 1,purple)
addPixels(strip, 7,black)

# 2
addPixels(strip, 7,black)
addPixels(strip, 1,purple)
addPixels(strip, 3,black)
addPixels(strip, 1,purple)
addPixels(strip, 3,black)

addPixels(strip, 1,blue)
addPixels(strip, 1,black)
addPixels(strip, 1,blue)

addPixels(strip, 4,black)
addPixels(strip, 1,white)
addPixels(strip, 4,black)

addPixels(strip, 2,yellow)
addPixels(strip, 2,black)
addPixels(strip, 1,yellow)

addPixels(strip, 2,black)
addPixels(strip, 1,orange)
addPixels(strip, 3,black)
addPixels(strip, 1,orange)
addPixels(strip, 2,black)

addPixels(strip, 1,pink)
addPixels(strip, 3,black)
addPixels(strip, 1,pink)
addPixels(strip, 2,black)

addPixels(strip, 1,purple)
addPixels(strip, 3,black)
addPixels(strip, 1,purple)
addPixels(strip, 7,black)

# 3
addPixels(strip, 7,black)
addPixels(strip, 1,purple)
addPixels(strip, 2,black)
addPixels(strip, 2,purple)
addPixels(strip, 2,black)

addPixels(strip, 1,blue)
addPixels(strip, 3,black)
addPixels(strip, 1,blue)

addPixels(strip, 3,black)
addPixels(strip, 1,white)
addPixels(strip, 4,black)

addPixels(strip, 1,yellow)
addPixels(strip, 1,black)
addPixels(strip, 1,yellow)
addPixels(strip, 1,black)
addPixels(strip, 1,yellow)

addPixels(strip, 2,black)
addPixels(strip, 1,orange)
addPixels(strip, 1,black)
addPixels(strip, 2,orange)
addPixels(strip, 3,black)

addPixels(strip, 1,pink)
addPixels(strip, 3,black)
addPixels(strip, 1,pink)
addPixels(strip, 2,black)

addPixels(strip, 1,purple)
addPixels(strip, 3,black)
addPixels(strip, 1,purple)
addPixels(strip, 7,black)

# 4
addPixels(strip, 7,black)
addPixels(strip, 3,purple)
addPixels(strip, 4,black)

addPixels(strip, 5,blue)

addPixels(strip, 3,black)
addPixels(strip, 1,white)
addPixels(strip, 4,black)

addPixels(strip, 1,yellow)
addPixels(strip, 1,black)
addPixels(strip, 3,yellow)

addPixels(strip, 2,black)
addPixels(strip, 1,orange)
addPixels(strip, 3,black)
addPixels(strip, 1,orange)
addPixels(strip, 2,black)

addPixels(strip, 1,pink)
addPixels(strip, 3,black)
addPixels(strip, 1,pink)
addPixels(strip, 2,black)

addPixels(strip, 1,purple)
addPixels(strip, 1,black)
addPixels(strip, 1,purple)
addPixels(strip, 1,black)
addPixels(strip, 1,purple)
addPixels(strip, 7,black)

# 5
addPixels(strip, 7,black)
addPixels(strip, 1,purple)
addPixels(strip, 1,black)
addPixels(strip, 1,purple)
addPixels(strip, 4,black)

addPixels(strip, 1,blue)
addPixels(strip, 3,black)
addPixels(strip, 1,blue)

addPixels(strip, 3,black)
addPixels(strip, 1,white)
addPixels(strip, 4,black)

addPixels(strip, 1,yellow)
addPixels(strip, 2,black)
addPixels(strip, 2,yellow)

addPixels(strip, 2,black)
addPixels(strip, 1,orange)
addPixels(strip, 3,black)
addPixels(strip, 1,orange)
addPixels(strip, 2,black)

addPixels(strip, 1,pink)
addPixels(strip, 3,black)
addPixels(strip, 1,pink)
addPixels(strip, 2,black)

addPixels(strip, 1,purple)
addPixels(strip, 1,black)
addPixels(strip, 1,purple)
addPixels(strip, 1,black)
addPixels(strip, 1,purple)
addPixels(strip, 7,black)

# 6
addPixels(strip, 7,black)
addPixels(strip, 1,purple)
addPixels(strip, 2,black)
addPixels(strip, 2,purple)
addPixels(strip, 2,black)

addPixels(strip, 1,blue)
addPixels(strip, 3,black)
addPixels(strip, 1,blue)

addPixels(strip, 1,black)
addPixels(strip, 5,white)
addPixels(strip, 2,black)

addPixels(strip, 1,yellow)
addPixels(strip, 3,black)
addPixels(strip, 1,yellow)

addPixels(strip, 2,black)
addPixels(strip, 4,orange)
addPixels(strip, 4,black)

addPixels(strip, 3,pink)
addPixels(strip, 4,black)

addPixels(strip, 3,purple)
addPixels(strip, 8,black)



ADDRESS = 'localhost:7890'
client = opc.Client(ADDRESS)
client.put_pixels(strip)
client.put_pixels(strip)