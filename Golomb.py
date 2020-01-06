import math

class Golomb:

    def __init__(self, m, bitStream=None):
        self.m = m
        self.b = math.ceil(math.log2(m))
        self.l = self.b-1

        self.bitStream = bitStream

    def encode2(self, n):
        if n<0:             #negative numbers
            n=(-2*n)
        elif n>0:
            n = 2*n-1
        #result = ""
        r = n % self.m

        for i in range(n//self.m):
            self.bitStream.writeBit(1)
        self.bitStream.writeBit(0)

        self.bitStream.writeBits(r,self.b)      #uses bitstream directly



    def decode(self, encoded_num=None):
        #print(encoded_num)
        
        q = 0
        while self.bitStream.readBit() != 0:
            q += 1
        

        r=self.bitStream.readBits(self.b)   #bitstream returns number
        n = r+q*self.m
        if n%2==0:
            n = int(n/-2)
        else:
            n = (n+1)/2
        return int(n)
        

