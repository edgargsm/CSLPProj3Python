import cv2
import numpy as np


class Frame:

    def __init__(self, frame):
        # Frame é tuplo de três elementos: (y, u, v) 
        # Como o output da função get frame da classe video
        self.y = frame[0]
        self.u = frame[1]
        self.v = frame[2]
        self.height = self.y.shape[0]
        self.width = self.y.shape[1]

    def preditiveEncodingJPEG_LS(self):
        final_y = np.zeros(self.y.shape, dtype=int)
        final_u = np.zeros(self.u.shape, dtype=int)
        final_v = np.zeros(self.v.shape, dtype=int)
        # Calcular o preditor de y
        for lin in range(self.y.shape[0]):
            for col in range(self.y.shape[1]):
                if col-1<0 and lin-1<0:
                    a = 127
                    b = 127
                    c = 127
                elif col-1<0:
                    a = int(self.y[lin,col-1])
                    b = 127
                    c = 127
                elif lin-1<0:
                    a = 127
                    b = int(self.y[lin-1,col])
                    c = 127  
                else:
                    a = int(self.y[lin,col-1])
                    b = int(self.y[lin-1,col])
                    c = int(self.y[lin-1,col-1])
                if c >= max([a,b]):
                    pred = min([a,b])
                elif c <= min([a,b]):
                    pred = max([a,b])
                else:
                    pred = a+b-c
                #golomb.encode(self.y[lin,col] - pred)
                #print(g_code)
                #for b in range(len(g_code)):
                    #print(int(g_code[b]))
                    #bitstream.writeBit(int(g_code[b]))
                final_y[lin,col] = self.y[lin,col] - pred

        # Calcular o preditor de u
        for lin in range(self.u.shape[0]):
            for col in range(self.u.shape[1]):
                if col-1<0 and lin-1<0:
                    a = 127
                    b = 127
                    c = 127
                elif col-1<0:
                    a = int(self.u[lin,col-1])
                    b = 127
                    c = 127
                elif lin-1<0:
                    a = 127
                    b = int(self.u[lin-1,col])
                    c = 127
                else:
                    a = int(self.u[lin,col-1])
                    b = int(self.u[lin-1,col])
                    c = int(self.u[lin-1,col-1])

                if c >= max([a,b]):
                    pred = min([a,b])
                elif c <= min([a,b]):
                    pred = max([a,b])
                else:
                    pred = a+b-c
                #golomb.encode(self.u[lin,col] - pred)
                #print(g_code)
                #for b in range(len(g_code)):
                    #print(int(g_code[b]))
                    #bitstream.writeBit(int(g_code[b]))
                final_u[lin,col] = self.u[lin,col] - pred

        # Calcular o preditor de v
        for lin in range(self.v.shape[0]):
            for col in range(self.v.shape[1]):
                if col-1<0 and lin-1<0:
                    a = 127
                    b = 127
                    c = 127
                elif col-1<0:
                    a = int(self.v[lin,col-1])
                    b = 127
                    c = 127
                elif lin-1<0:
                    a = 127
                    b = int(self.v[lin-1,col])
                    c = 127
                else:
                    a = int(self.v[lin,col-1])
                    b = int(self.v[lin-1,col])
                    c = int(self.v[lin-1,col-1])

                if c >= max([a,b]):
                    pred = min([a,b])
                elif c <= min([a,b]):
                    pred = max([a,b])
                else:
                    pred = a+b-c
                #golomb.encode(self.v[lin,col] - pred)
                #print(g_code)
                #for b in range(len(g_code)):
                    #print(int(g_code[b]))
                    #bitstream.writeBit(int(g_code[b]))
                final_v[lin,col] = int(self.v[lin,col]) - int(pred)

        return (final_y, final_u, final_v)


