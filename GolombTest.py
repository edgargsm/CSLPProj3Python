from Golomb import Golomb

g = Golomb(5)

encoded = g.encode(-5)
print(encoded)
#encoded_num, l = g.encode(15)

print(g.decode(encoded))