

class BitStream:

    def __init__(self, file, access, init_message = None, read_FirstLine = None):
        self.file = open(file, access)
        self.first_line = None
        if access=="wb" and init_message is not None:
            self.file.write(init_message.encode('utf-8'))
        if access=="rb" and read_FirstLine:
            self.first_line = self.file.readline()
        self.byte = 0
        self.count = -1
        if access == "wb":
            self.count = 7
        self.access = access
        self.buffer = bytearray(b'')

    def readBit(self):
        if self.access!="rb":
            print("Não foi possivel ler bit porque o acesso ao ficheiro foi de escrita")
            return None

        
        if self.count < 0:
            self.byte = self.file.read(1)
            #print(bin(int.from_bytes(self.byte, "little")))
            if not self.byte:
                print("Ficheiro já foi completamente lido.")
                self.file.close()
                return None
            self.count = 7
        
        
        bit = (int.from_bytes(self.byte, "little") >> self.count) & 1
        self.count -= 1

        return bit

    def writeBit(self, bit):
        if self.access!="wb":
            print("Não foi possivel escrever o bit porque o acesso ao ficheiro foi de escrita")
            return None

        if self.count < 0:
            #print("Dump no ficheiro..")
            #print(bin(self.byte))
            #print(bin(int.from_bytes(self.byte.to_bytes(8, 'little'), "little")))
            #self.file.write(self.byte.to_bytes(1, 'little'))
            self.buffer.append(self.byte)
            self.byte = 0
            self.count = 7

        self.byte = self.byte | (bit << self.count)
        #self.byte = self.byte.to_bytes(1, "big")
        self.count -= 1

    def endWrite(self):
        if self.access!="wb":
            print("O modo de acesso não foi o de escrita.")

        self.file.write(self.buffer)
        if self.count != 7:
            #print(self.byte)
            self.file.write(self.byte.to_bytes(1, 'little'))
        
        self.file.close()
        print("Escrita de bits finalizada")

    def readBits(self, n):
        if self.access!="rb":
            print("Não foi possivel ler bit porque o acesso ao ficheiro foi de escrita")
            return

        num = 0
        for i in range(n-1,-1,-1):

            bit = self.readBit()
            if bit==None:
                print("Não foi possivel ler o numero de bits pedidos")
                break
            

            val =bit << i & 2**i
            num += val

        return num

    def writeBits(self, n,nbits):
        
        if self.access!="wb":
            print("Não foi possivel escrever o bit porque o acesso ao ficheiro foi de escrita")
            return None
        
        """for i in arr:
            self.writeBit(i)"""
        
        for i in range(nbits-1, -1,-1):
            self.writeBit(n >> i & 1)
