from Golomb import Golomb

g = Golomb(5)

print(g.encode(15))
encoded_num, l = g.encode(15)

print(g.decode(encoded_num, l))