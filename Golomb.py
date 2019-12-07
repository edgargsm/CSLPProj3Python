import math

class Golomb:

    def __init__(self, m):
        self.m = m
        self.b = math.ceil(math.log2(m))
        self.l = self.b-1


    def encode(self, n):
        if n<0:
            n=int(-2*n)
        result = ""
        q = int(n/self.m)
        r = n - q*self.m
        l = self.b-1
        if r >= 2**self.b - self.m:
            r = r + 2**self.b - self.m
            l = self.b
        for i in range(q):
            result = result+'1'
        result = result+'0'
        #unary_q = self.unariCode(q)
        #print(result)
        stringr = bin(r)[2:]
        #print((r))
        stringr = '0'*(l-len(stringr))+stringr
        result = result + stringr
        #unary_length = q+1
        #result = (unary_q << l) | r
        #print("R -> ",r)
        #print("Q -> ",q)
        #print("b -> ",self.b)
        #, unary_length+l
        return result


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
        return n
        pass
