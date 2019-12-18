import math

class Golomb:

    def __init__(self, m, bitStream=None):
        self.m = m
        self.b = math.ceil(math.log2(m))
        self.l = self.b-1

        self.bitStream = bitStream


    def encode(self, n):
        if n<0:
            n=(-2*n)
        elif n>0:
            n = 2*n-1
        #result = ""
        q = (n//self.m)
        r = n % self.m

        if r >= 2**self.b - self.m:
            r = r + 2**self.b - self.m
            self.l = self.b

        #result = '1'*q+'0'
        stringr = bin(r)[2:]

        self.bitStream.writeBits([1]*q + [0] + [0] * (self.l-len(stringr)))


        #result += '0'*(self.l-len(stringr))
        for i in stringr:
            self.bitStream.writeBit(int(i))
            #result += i

        '''stringr = '0'*(self.l-len(stringr))+stringr
        result = result + stringr'''
        #return result
    
    def encode2(self, n):
        if n<0:
            n=(-2*n)
        elif n>0:
            n = 2*n-1
        #result = ""
        r = n % self.m
        #result = '1'*q+'0'
        
        self.bitStream.writeBits([1]*(n//self.m) + [0] + [1 if digit=='1' else 0 for digit in bin(r)[2:]])
        #self.bitStream.writeBit(0)

        #for i in range(self.b-1,-1, -1):
            #result += str(r >> i & 1)
            #self.bitStream.writeBit(r >> i & 1)
        
        #self.bitStream.writeBits([1 if digit=='1' else 0 for digit in bin(r)[2:]])
        #return result



    def decode(self, encoded_num):
        q = 0
        i = 0
        while encoded_num[i]!='0':
            q+=1
            i+=1
        i+=1
        r = encoded_num[i:]
        l = len(r)
        r = int(r, 2)
        if(l==self.b):
            r = r - 2**self.b + self.m
        n = r+q*self.m
        #print("q-> ",q)
        #print("r-> ",r)
        if n%2==0:
            n = int(n/-2)
        else:
            n = (n+1)/2
        return n
