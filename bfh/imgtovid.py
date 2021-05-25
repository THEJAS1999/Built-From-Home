import cv2 
import os
from os.path import isfile, join

def convert(pathIn, pathOut ,fps, time):
    frame_array=[]
    files=[f for f in os.listdir(pathIn)if isfile(join(pathIn,f))]
    for i in range(len(files)):
        filename=pathIn+files[i]
        img=cv2.imread(filename)
        height,width,layers = img.shape
        size=(width,height)

        for k in range(time):
            frame_array.append(img)
out=cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'mp4v',fps,size))
for i in range(len(frame_array)):
    out.write(frame_array[i])
outrelease()

directory='C:/Users/VISHNU P C/Desktop/Music/Snaps'
pathIn=directory+'/'
pathOut=pathIn+'video.avi'
fps=1
time=2
convert(pathIn,pathOut,fps,time)