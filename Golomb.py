import math

class Golomb:

    def __init__(self, m):
        self.m = m
        self.b = math.ceil(math.log2(m))


    def encode(self, n):
        q = int(n/self.m)
        r = n - q*self.m
        l = self.b-1
        if r >= 2**self.b - self.m:
            r = r + 2**self.b - self.m
            l = self.b
        unary_q = self.unariCode(q)
        unary_length = q+1
        result = (unary_q << l) | r
        #print("R -> ",r)
        #print("Q -> ",unary_q)
        #print("b -> ",self.b)
        return result, unary_length+l


    def decode(self, encoded_num, length):
        unary_length = 0
        l = length
        while True:
            l -= 1
            if ((encoded_num >> l) & 1) :
                

        pass

    def unariCode(self, n):
        result = 0
        for i in range(n):
            result = (result | 1) << 1
        return result
            

