from Bitstream import BitStream

#bt = BitStream("text.txt", "rb")

bt1 = BitStream("text1.txt", "wb")

bt1.writeBit(1)
bt1.writeBit(1)
bt1.writeBit(1)
bt1.writeBit(1)
bt1.writeBit(1)
bt1.writeBit(1)
bt1.writeBit(1)
bt1.writeBit(1)

bt1.endWrite()

bt = BitStream("text1.txt", "rb")
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print(bt.readBit())
print("first byte")
print(bt.readBit())

