import cv2
import numpy as np
from Frame import Frame
from Video import Video
from Bitstream import BitStream
from Golomb import Golomb
import sys
import time
import math

bitstream = BitStream("write_ducks.y4m",'rb', read_FirstLine=True)
print(bitstream.first_line)
params = str(bitstream.first_line)[2:-3].split(" ")

width = int(params[0])

height = int(params[1])

formato = params[2]

m = int(params[3])

golomb = Golomb(m,bitstream)

write_file = open("Decoded_File.y4m", 'wb')
write_file.write(("YUV4MPEG2 W"+str(width)+" H"+str(height)+" F50:1 Ip A1:1").encode("utf-8"))

r_size = math.ceil(math.log2(m))

if formato == '444':
    uv_shape = (height,width)
elif formato == '422':
    uv_shape = (height, (width//2))
elif formato == '420':
    uv_shape = (height//2, width//2)

stop = 0
numf = 0

while True:
    t = time.time()
    y = np.zeros((height, width), dtype=int)
    u = np.zeros(uv_shape, dtype=int)
    v = np.zeros(uv_shape, dtype=int)

    for lin in range(y.shape[0]):
        for col in range(y.shape[1]):
            '''
            r = ''
            while bitstream.readBit() != 0:
                r += '1'
            
            r +='0'
            for i in bitstream.readBits(r_size):
                r += str(i)

            print([1 if i == '1' else 0 for i in list(r)])
            dec = golomb.decode(r)
            print(dec)
            '''
            dec = golomb.decode()
            print(dec)

            y[lin, col] = np.uint8(dec)
    
    for lin in range(u.shape[0]):
        for col in range(u.shape[1]):
            # rq = bitstream.readBit()
            # q = str(rq)
            # while rq==1:
            #     rq = bitstream.readBit()
            #     q = q + str(rq)
            # r_arr = bitstream.readBits(r_size)
            # r = ''
            # for i in r_arr:
            #     r = r + str(i)
            # dec = golomb.decode(q+r)
            dec = golomb.decode()
            print(dec)

            u[lin, col] = np.uint8(dec)

    for lin in range(v.shape[0]):
        for col in range(v.shape[1]):
            # rq = bitstream.readBit()
            # q = str(rq)
            # while rq==1:
            #     rq = bitstream.readBit()
            #     q = q + str(rq)
            # r_arr = bitstream.readBits(r_size)
            # r = ''
            # for i in r_arr:
            #     r = r + str(i)
            # dec = golomb.decode(q+r)
            dec = golomb.decode()
            print(dec)

            v[lin, col] = np.uint8(dec)
    
    y.tofile(write_file)
    u.tofile(write_file)
    v.tofile(write_file)
    numf=numf+1
    print(numf)
    print(time.time()-t)
    if numf>=500:
        break
    write_file.write("Frame\n".encode("utf-8"))
    

write_file.close()