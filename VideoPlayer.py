import cv2
import numpy as np
import sys


f = open('ducks_take_off_422_720p50.y4m','rb')
status = f.readline()
print(status)
status = str(status)[2:-3].split()
f.readline() #Ler Frame
width = int(status[1][1:])
height = int(status[2][1:])
try:
    formato = status[-1][1:]
    form = [int((status[-1][1:])[0]),int((status[-1][1:])[1]),int((status[-1][1:])[2])]
except:
    formato = '420'
    form = [4,2,0]
s = sum(form)/4
y_size = int(width*height)
uv_size = int(width*height*(form[1]+form[2])/8)

while(True):
    
    y = f.read(y_size)
    y = np.frombuffer(y, dtype="uint8")
    if len(y)==0:
        break
    u = f.read(uv_size)
    u = np.frombuffer(u, dtype="uint8")
    if len(u)==0:
        break
    v = f.read(uv_size)
    v = np.frombuffer(v, dtype="uint8")
    if len(v)==0:
        break

    y = np.reshape(y, (height,width))
    if formato == '444':
        u = np.reshape(u, (height,width))
        v = np.reshape(v, (height,width))
    if formato == '422':
        u = np.repeat(u,2)
        u = np.reshape(u, (height, width))
        v = np.repeat(v,2)
        v = np.reshape(v, (height, width))
    if formato == '420':
        u = np.repeat(u,2)
        u = np.reshape(u, (height//2, width))
        v = np.repeat(v,2)
        v = np.reshape(v, (height//2, width))
        u = np.concatenate((u,u),1)
        v = np.concatenate((v,v),1)
        u = np.reshape(u, (height, width))
        v = np.reshape(v, (height, width))


    frameexp = cv2.cvtColor(cv2.merge((y,u,v)),cv2.COLOR_YUV2BGR)
    frameyuv = cv2.merge((y,u,v))


    cv2.imshow('ducks_take_off_422_720p50',frameexp)
    f.readline()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cv2.destroyAllWindows()
