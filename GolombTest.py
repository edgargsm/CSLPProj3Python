from Golomb import Golomb
from Bitstream import BitStream
import sys

bt = BitStream("text1.txt", "wb",init_message = "Ola\n")
g = Golomb(5, bt)

encoded2 = g.encode2(int(sys.argv[1]))
bt.endWrite()


bt2 = BitStream("text1.txt", "rb",read_FirstLine = True)
g2 = Golomb(5,bt2)
decoded2 = g2.decode() 
print(bt2.first_line)
print(decoded2)
