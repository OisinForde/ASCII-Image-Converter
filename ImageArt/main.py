import cv2 as cv
import math
import numpy as np
import os

characterList=list('~!"#$%&().+_}/:;<=>^-{|*1234567890') #List of all ASCII character the converter can use

def accessImgs():
    imgFile=[]
    for filename in os.listdir('C:\\Users\\oisin\\pyproj\\ASCII_art\\ImageArt\\img'):
        f = os.path.join('C:\\Users\\oisin\\pyproj\\ASCII_art\\ImageArt\\img', filename)
        # checking if it is a file
        if os.path.isfile(f):
            imgFile.append(f)
    return imgFile[0] #Return first file


def main():
        outputImg=[]
        FilteredoutputImg=[]
        final=[]
        img=cv.imread(accessImgs())
        img=np.array(cv.cvtColor(img,cv.COLOR_RGB2GRAY))
        img_width=img.shape[1]
        rowIndex=0
        multipler=2
        for column in range(img_width):
            FilteredoutputImg.append([])

        for column in img:
            for pixel in column:
                #print(pixel)
                for i in range(multipler):
                    outputImg.append(characterList[math.ceil(pixel/7.5)-1])

        for i in range(0,img_width*img_width*multipler,img_width*multipler):
            if i%img_width*multipler==0:
                FilteredoutputImg[rowIndex]=outputImg[i:i+img_width*multipler]
                rowIndex+=1

        for i in FilteredoutputImg:
            b=''.join(str(i).split(','))
            b = ''.join(str(b).split(']'))
            b = ''.join(str(b).split('['))
            b = ''.join(str(b).split("'"))
            b = ''.join(str(b).split(" "))
            b=b.replace('\u200b', '9')

            final.append(b)

        return final

print(*main(),sep='\n')
