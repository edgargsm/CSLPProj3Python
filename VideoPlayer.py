import cv2
import numpy as np

#cap = cv2.VideoCapture('ducks_take_off_444_720p50.y4m')

f = open('ducks_take_off_444_720p50.y4m','rb')


status = f.readline()
status = str(status)[2:-3].split()
f.readline() #Ler Frame
width = int(status[1][1:])
height = int(status[2][1:])
form = [int((status[-1][1:])[0]),int((status[-1][1:])[1]),int((status[-1][1:])[2])]
s = sum(form)/4
print(width)
print(height)
print(s)
y_size = int(width*height)
uv_size = int(width*height*(form[1]+form[2])/8)
i=0
while True:
    
    y = f.read(y_size)
    y = np.frombuffer(y, dtype="uint8")
    u = f.read(uv_size)
    u = np.frombuffer(u, dtype="uint8")
    u = np.reshape(u, (width*height,))
    v = f.read(uv_size)
    v = np.frombuffer(v, dtype="uint8")
    v = np.reshape(v, (width*height,))
    #print(v)
    #print(u)
    r = np.zeros((width*height,),dtype=np.uint8)
    g = np.zeros((width*height,),dtype=np.uint8)
    b = np.zeros((width*height,),dtype=np.uint8)
    
    #for i in range(y_size):
        #r[i] =y[i]+int(1.140*v[i])
        #print(r)
        #g[i] = y[i]-0.395*u[i]-0.581*v[i]
        #b[i] = y[i]+2.032*u[i]
        #np.append(g,y[i]-0.395*u[i]-0.581*v[i])
        #np.append(b,y[i]+2.032*u[i])
    r = y+(1.140*v)
    g = y-0.395*u-0.581*v
    b = y+2.032*u
    #print(r)
    r = np.reshape(r, (width, height))
    g = np.reshape(g, (width, height))
    b = np.reshape(b, (width, height))
    #print(r)
    
    frame = cv2.merge((r,g,b))
    #print(frame.shape)
    #print(frame)
    
    cv2.imshow('frame',frame)
    print(frame[5][5])

    
#print(f.read(6))


#print(str(status)[2:-3])
#print(f.readline())
#print(f.readline())
#print(f.read(1280*720*3))
#print(f.readline())

#print(f.read(10))
