# strip  is the list
# n      number of LEDs
# colour Tuple with RGB value
def addPixels(strip, n, colour):
	strip += [colour]*n
	return