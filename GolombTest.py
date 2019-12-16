from Golomb import Golomb
import sys

g = Golomb(5)
try:
    encoded = g.encode(int(sys.argv[1]))
except:
    encoded = g.encode(7)

print(encoded)
#encoded_num, l = g.encode(15)

print(g.decode(encoded))