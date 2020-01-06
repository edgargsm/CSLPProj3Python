import cv2
import numpy as np
from Frame import Frame
from Video import Video
from Bitstream import BitStream
from Golomb import Golomb
import sys
import time

video = Video(sys.argv[1])
m=5
params = "" + str(video.width) +" "+ str(video.height) +" "+ str(video.formato) +" "+ str(m) +"\n"

bitstream = BitStream(sys.argv[2],'wb', params)
golomb = Golomb(m, bitstream)

fnum=0
while True:
    t = time.time()
    frame_read = video.getFrame()

    if frame_read is None:
        break

    frame = Frame(frame_read)

    encodedFrame = frame.preditiveEncodingJPEG_LS()
    fnum+=1
    print(fnum)

    for f in range(len(encodedFrame)):
        for line in range(encodedFrame[f].shape[0]):
            for col in range(encodedFrame[f].shape[1]):
                pix = int(encodedFrame[f][line,col])    #prediction
                golomb.encode2(pix)                     #uses bitstream to save

#    if fnum == 10:
#        break
    print(time.time()-t)

bitstream.endWrite()

