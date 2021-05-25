import cv2
import os
from os.path import isfile, join

def convert(pathIn, pathOut ,fps, time):
    print("file converting")
    frame_array=[]
    files=[f for f in os.listdir(pathIn)if isfile(join(pathIn,f))]
    for i in range(len(files)):
        filename=pathIn+files[i]
        img=cv2.imread(filename)
        height,width,layers = img.shape
        size=(width,height)
        for k in range(time):
            frame_array.append(img)
    fourcc=cv2.VideoWriter_fourcc(*'mp4v')
    out=cv2.VideoWriter(pathOut,fourcc,fps,size)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()
   