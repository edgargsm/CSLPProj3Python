import cv2
import numpy as np

'''
narr = np.array([1,2,3,4,5,6])
print(narr)

narr = narr.reshape((2,3))
print(narr)

narr1 = np.array([1,2,3])
print(narr1.reshape((6,)))
'''
f = open('ducks_take_off_444_720p50.y4m','rb')
#cap = cv2.VideoCapture('ducks_take_off_444_720p50.y4m')
status = f.readline()
print(status)
status = str(status)[2:-3].split()
f.readline() #Ler Frame
width = int(status[1][1:])
height = int(status[2][1:])
form = [int((status[-1][1:])[0]),int((status[-1][1:])[1]),int((status[-1][1:])[2])]
s = sum(form)/4
y_size = int(width*height)
uv_size = int(width*height*(form[1]+form[2])/8)

while(True):
    #ret, frame = cap.read()
    y = f.read(y_size)
    y = np.frombuffer(y, dtype="uint8")
    if len(y)==0:
        break
    u = f.read(uv_size)
    u = np.frombuffer(u, dtype="uint8")
    if len(u)==0:
        break
    #u = np.reshape(u, (width*height,))
    v = f.read(uv_size)
    v = np.frombuffer(v, dtype="uint8")
    if len(v)==0:
        break
    #v = np.reshape(v, (width*height,))

    #r = np.zeros((width*height,),dtype=np.uint8)
    #g = np.zeros((width*height,),dtype=np.uint8)
    #b = np.zeros((width*height,),dtype=np.uint8)

    #delta = 128
    #r = y+(1.403*(u-delta))
    #g = y-0.714*(u-delta)-0.344*(v-delta)
    #b = y+1.773*(v-delta)

    y = np.reshape(y, (height,width))
    u = np.reshape(u, (height,width))
    v = np.reshape(v, (height,width))

    #r = np.reshape(r, (height,width))
    #g = np.reshape(g, (height,width))
    #b = np.reshape(b, (height,width))

    frameexp = cv2.cvtColor(cv2.merge((y,u,v)),cv2.COLOR_YUV2BGR)
    frameyuv = cv2.merge((y,u,v))
    #framergb = cv2.merge((r,g,b))
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #print(frameexp.shape)
    #print(frameexp[0,0])
    cv2.imshow('frame',frameexp)
    f.readline()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    


#cap.release()
cv2.destroyAllWindows()
