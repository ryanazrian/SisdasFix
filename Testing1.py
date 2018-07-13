import numpy as np
import cv2
import kumpulanKode as libs
import object_size as size
import glob

import pickle
import os


kernel = np.ones((5,5), np.uint8)
def imageProcess(filename):
    os.chdir('/home/ryanazrian/Desktop/PCD/Project/code/CodeFix/WEB')
    img = cv2.imread('temp/'+ filename)
    red = 0
    blue = 0
    green = 0

    hue = 0
    sat = 0
    val = 0

    ha=0
    sa=0
    va=0

    re = 0
    gr = 0
    bl  = 0

    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    gray = cv2.cvtColor(hsv, cv2.COLOR_RGB2GRAY)

    #img = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
    #b, g, r = cv2.split()
    #b = libs.treshold(libs.substract(r, g))

    ret, b = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)


    dilate = cv2.dilate(b, kernel, iterations = 10)
    final = cv2.erode(dilate, kernel, iterations= 10)
    hasil = libs.subrgbgray(img, final)

    row, col, ch  = hasil.shape
    for x in range (0, row):
        for y in range (0, col):
            b, g, r = hasil[x, y]
            if(b & g & r):
                red = red + r
                green = green + g
                blue = blue +b

                if(b):
                    bl = bl+ 1
                if(r):
                    re = re + 1
                if(g):
                    gr = gr +1
    red = red / re
    green = green/ gr
    blue = blue / bl
    jumlah_frek =  re + gr +bl

    HSV = cv2.cvtColor(hasil, cv2.COLOR_RGB2HSV)
    row, col, ch = HSV.shape
    for x in range (0, row):
        for y in range (0, col):
            h, s, v = HSV[x, y]
            if(h & s & v):
                hue = hue + h
                sat = sat + s
                val = val + v
                
                if(h):
                    ha = ha+1
                if(s):
                    sa = sa+1
                if(v):
                    va = va+1

    hue = hue / ha
    sat = sat / sa
    val = val / va

    #ambil ukuran
    panjang = 0
    lebar = 0
    float(panjang)
    float(lebar)
    panjang, lebar = size.cari_size(hasil)

            
    myTomat = '%d, %d, %d, %d, %d, %d, %d, %s' %(red, green, blue, hue, sat, val, jumlah_frek, panjang)

    testMatang = [[red, green, blue, hue, sat, val]]
    testBerat = [[jumlah_frek, panjang]]


    #test kematangan
    filename = 'kematangan1.sav'
    loaded_model = pickle.load(open(filename, 'rb')) 
    matangPredict = loaded_model.predict(testMatang) #nnti ini test : inputan baru 

    #Test Berat
    filename = 'berat1.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    beratPredict = loaded_model.predict(testBerat)

    return matangPredict[0], beratPredict[0]

# print('Kematangan: %s' %(matangPredict[0]))
# print('Berat : %.2f' %(beratPredict[0]))