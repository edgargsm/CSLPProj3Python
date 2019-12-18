from Golomb import Golomb
import sys
mask = (1<<3)-1
print(4 & mask)

g = Golomb(5)
try:
    encoded = g.encode(int(sys.argv[1]))
    encoded2 = g.encode2(int(sys.argv[1]))
except:
    encoded = g.encode(7)

print(encoded)
print(encoded2)
#encoded_num, l = g.encode(15)

print(g.decode(encoded))