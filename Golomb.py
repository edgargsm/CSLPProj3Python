import math

class Golomb:

    def __init__(self, m, bitStream=None):
        self.m = m
        self.b = math.ceil(math.log2(m))
        self.l = self.b-1

        self.bitStream = bitStream

    def encode2(self, n):
        if n<0:
            n=(-2*n)
        elif n>0:
            n = 2*n-1
        #result = ""
        r = n % self.m

        for i in range(n//self.m):
            self.bitStream.writeBit(1)
        self.bitStream.writeBit(0)

        self.bitStream.writeBits(r,self.b)

        '''
        if r >= 2**self.b - self.m:
            r = r + 2**self.b - self.m
            self.l = self.b
        '''

        '''
        #result = '1'*q+'0'
        helper = bin(r)[2:]
        while len(helper) < self.b:
            helper = '0' + helper

        self.bitStream.writeBits([1]*(n//self.m) + [0] + [1 if digit=='1' else 0 for digit in helper])
        #print([1]*(n//self.m) + [0] + [1 if digit=='1' else 0 for digit in helper])
        #return '1' *(n//self.m) + '0' + bin(r)[2:]'''

    def decode(self, encoded_num=None):
        #print(encoded_num)
        
        q = 0
        while self.bitStream.readBit() != 0:
            q += 1
        
        # r = ''
        # for i in self.bitStream.readBits(self.b):
        #     r += str(i)
        # r = int(r,2)

        r=self.bitStream.readBits(self.b)   #bitstream returns number
        n = r+q*self.m
        if n%2==0:
            n = int(n/-2)
        else:
            n = (n+1)/2
        return int(n)
        

        '''q = 0
        i = 0
        while i<len(encoded_num) and encoded_num[i]!='0':
            q+=1
            i+=1
        i+=1
        r = encoded_num[i:]
        l = len(r)
        r = int(r, 2)
        #if(l==self.b):
        #    r = r - 2**self.b + self.m
        n = r+q*self.m
        #print("q-> ",q)
        #print("r-> ",r)
        if n%2==0:
            n = int(n/-2)
        else:
            n = (n+1)/2
        return n'''
