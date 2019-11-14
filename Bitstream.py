

class BitStream:

    def __init__(self, file, access):
        self.file = open(file, access)
        self.byte = bytes(0)
        self.count = 0
        self.access = access

    def readBit(self):
        if self.access!="rb":
            print("Não foi possivel ler bit porque o acesso ao ficheiro foi de escrita")
            return None

        
        if self.count < 0:
            self.byte = self.file.read(1)
            #print(bin(int.from_bytes(self.byte, "little")))
            if self.byte == None:
                print("Ficheiro já foi completamente lido.")
                self.file.close()
                return None
            self.count = 7
        
        
        bit = (int.from_bytes(self.byte, "big") >> self.count) & 1
        self.count -= 1

        return bit

    def writeBit(self, bit):
        if self.access!="wb":
            print("Não foi possivel escrever o bit porque o acesso ao ficheiro foi de escrita")
            return None

        if self.count < 0:
            self.file.write(self.byte)
            self.byte = 0
            self.count = 7

        self.byte = self.byte | (bit << self.count)
        self.count -= 1

        pass

    def endWrite(self):
        if self.access!="wb":
            print("O modo de acesso não foi o de escrita.")

        if self.byte != 0:
            self.file.write(self.byte)
        
        self.file.close()
        print("Escrita de bits finalizada")

    def readBits(self, n):
        if self.access!="rb":
            print("Não foi possivel ler bit porque o acesso ao ficheiro foi de escrita")
            return

        arr = []

        for i in range(n):
            bit = self.readBit()
            if bit==None:
                print("Não foi possivel ler o numero de bits pedidos")
                break
            arr.append(bit)

        return arr

    def writeBits(self, arr):
        
        if self.access!="wb":
            print("Não foi possivel escrever o bit porque o acesso ao ficheiro foi de escrita")
            return None

        for i in arr:
            self.writeBit(i)
