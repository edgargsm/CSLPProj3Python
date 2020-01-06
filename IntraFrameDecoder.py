import cv2
import numpy as np
from Frame import Frame
from Video import Video
from Bitstream import BitStream
from Golomb import Golomb
import sys
import time
import math
import os
bitstream = BitStream(sys.argv[1],'rb', read_FirstLine=True)
print(bitstream.first_line)
params = str(bitstream.first_line)[2:-3].split(" ")

width = int(params[0])

height = int(params[1])

formato = params[2]

m = int(params[3])

golomb = Golomb(m,bitstream)
bt2 = BitStream(sys.argv[2],'wb', "YUV4MPEG2 W"+str(width)+" H"+str(height)+" F50:1 Ip A1:1\n")
#write_file = open(sys.argv[2], 'wb')
#write_file.write(("YUV4MPEG2 W"+str(width)+" H"+str(height)+" F50:1 Ip A1:1\n").encode("utf-8"))

r_size = math.ceil(math.log2(m))

if formato == '444':
    uv_shape = (height,width)
elif formato == '422':
    uv_shape = (height, (width//2))
elif formato == '420':
    uv_shape = (height//2, width//2)

stop = 0
numf = 0
bt2.writeStuff("Frame\n")

while os.stat(sys.argv[1]).st_size != 0:
#while numf < 10:

    t = time.time()
    y = np.zeros((height, width), dtype=int)
    u = np.zeros(uv_shape, dtype=int)
    v = np.zeros(uv_shape, dtype=int)
    
    for lin in range(y.shape[0]):
        for col in range(y.shape[1]):

            if col-1<0 and lin-1<0:
                a = 127
                b = 127
                c = 127
            elif col-1<0:
                a = 127
                b = int(y[lin-1,col])
                c = 127
            elif lin-1<0:
                a = int(y[lin,col-1])
                b = 127
                c = 127  
            else:
                a = int(y[lin,col-1])
                b = int(y[lin-1,col])
                c = int(y[lin-1,col-1])
            if c >= max([a,b]):
                pred = min([a,b])
            elif c <= min([a,b]):
                pred = max([a,b])
            else:
                pred = a+b-c
            dec = golomb.decode()       #get prediction from file
            y[lin, col] = dec+pred
            bt2.writeBits(dec+pred,8)

    
    for lin in range(u.shape[0]):
        for col in range(u.shape[1]):

            if col-1<0 and lin-1<0:
                a = 127
                b = 127
                c = 127
            elif col-1<0:
                a = 127
                b = int(u[lin-1,col])
                c = 127
            elif lin-1<0:
                a = int(u[lin,col-1])
                b = 127
                c = 127    
            else:
                a = int(u[lin,col-1])
                b = int(u[lin-1,col])
                c = int(u[lin-1,col-1])
            if c >= max([a,b]):
                pred = min([a,b])
            elif c <= min([a,b]):
                pred = max([a,b])
            else:
                pred = a+b-c
            dec = golomb.decode()
            u[lin, col] = dec+pred
            bt2.writeBits(dec+pred,8)


    for lin in range(v.shape[0]):
        for col in range(v.shape[1]):

            if col-1<0 and lin-1<0:
                a = 127
                b = 127
                c = 127
            elif col-1<0:
                a = 127
                b = int(v[lin-1,col])
                c = 127
            elif lin-1<0:
                a = int(v[lin,col-1])
                b = 127
                c = 127    
            else:
                a = int(v[lin,col-1])
                b = int(v[lin-1,col])
                c = int(v[lin-1,col-1])
            if c >= max([a,b]):
                pred = min([a,b])
            elif c <= min([a,b]):
                pred = max([a,b])
            else:
                pred = a+b-c
            dec = golomb.decode()
            v[lin, col] = dec+pred
            bt2.writeBits(dec+pred,8)


    numf=numf+1
    print(numf)
    print(time.time()-t)

    #write_file.write("Frame\n".encode("utf-8"))
    bt2.writeStuff("Frame\n")

bt2.endWrite()
#write_file.close()
