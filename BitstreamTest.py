from Bitstream import BitStream

#bt = BitStream("text.txt", "rb")

bt1 = BitStream("text1.txt", "wb",init_message = "Ola\n")

bt1.writeBit(int(1))
bt1.writeBit(1)
bt1.writeBit(1)
bt1.writeBit(1)
bt1.writeBit(1)
bt1.writeBit(0)
bt1.writeBit(1)
bt1.writeBit(1)

bt1.writeBits([1,0,0,0,0,0,0,1])

bt1.writeBit(1)
bt1.writeBit(1)
bt1.writeBit(1)
bt1.writeBit(1)

bt1.endWrite()

bt = BitStream("text1.txt", "rb", read_FirstLine=True)
print("first byte")
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print("second byte")
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print("third byte")
print(bt.readBits(8))

print(bt.first_line)

