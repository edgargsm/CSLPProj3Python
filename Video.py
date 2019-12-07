import cv2
import numpy as np
import sys

class Video:

    def __init__(self,file):
        self.f = open(file,'rb')
        self.status = self.f.readline()
        #print(status)
        self.status = str(self.status)[2:-3].split()
        self.f.readline() #Ler Frame
        self.width = int(self.status[1][1:])
        self.height = int(self.status[2][1:])
        try:
            self.formato = self.status[-1][1:]
            self.form = [int((self.status[-1][1:])[0]),int((self.status[-1][1:])[1]),int((self.status[-1][1:])[2])]
        except:
            self.formato = '420'
            self.form = [4,2,0]
        self.s = sum(self.form)/4
        self.y_size = int(self.width*self.height)
        self.uv_size = int(self.width*self.height*(self.form[1]+self.form[2])/8)

    def getFrame(self):
        y = self.f.read(self.y_size)
        y = np.frombuffer(y, dtype="uint8")
        if len(y)==0:
            return None
        u = self.f.read(self.uv_size)
        u = np.frombuffer(u, dtype="uint8")
        if len(u)==0:
            return None
        v = self.f.read(self.uv_size)
        v = np.frombuffer(v, dtype="uint8")
        if len(v)==0:
            return None

        y = np.reshape(y, (self.height,self.width))

        if self.formato == '444':
            u = np.reshape(u, (self.height,self.width))
            v = np.reshape(v, (self.height,self.width))
        elif self.formato == '422':
            u = np.reshape(u, (self.height, (self.width//2)))
            v = np.reshape(v, (self.height, (self.width//2)))
        elif self.formato == '420':
            u = np.reshape(u, (self.height//2, self.width//2))
            v = np.reshape(v, (self.height//2, self.width//2))
        
        self.f.readline() # Read 'Frame\n'

        return (y, u, v)
