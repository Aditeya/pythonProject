import sys
import opc
import time

ADDRESS = 'localhost:7890'
client = opc.Client(ADDRESS)

if client.can_connect():
    print('connected to %s' % ADDRESS)
else:
	print('WARNING: could not connect to %s' % ADDRESS)
	sys.exit()
