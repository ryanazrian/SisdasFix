import cv2
import numpy as np

def subgraygray (gray1, gray2):
    #catatan ukuran gray 1 dan 2 harus sama dan inten sitas gray2 berupa 0 atau 255 (treshold)
    row, col = gray2.shape
    output = np.zeros((row,col,1), np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            if int(gray1[i,j])-int(gray2[i,j]) < 0 :
                output.itemset((i,j,0),0)
            else:
                output.itemset((i,j,0),int(gray1[i,j])-int(gray2[i,j]))
    return output

def treshold(img1):
    row, col, ch = img1.shape
    treshold = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            val = img1[i, j]
            if (val < 65):
                val = 0
            if (val > 65):
                val = 255

            treshold.itemset((i, j, 0), val)
    return treshold

def substract(image, image2):
    row, col = image.shape
    canvas = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            subs = int(image[i, j]) - int(image2[i, j])
            if (subs < 0):
                canvas.itemset((i, j, 0), 0)
            else:
                canvas.itemset((i, j, 0), subs)
    return canvas


def subrgbgray(rgb, treshold):
    row, col, raw = rgb.shape
    output = np.zeros((row, col, 3), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            if treshold[i, j] != 255:
                output.itemset((i, j, 0), 0)
                output.itemset((i, j, 1), 0)
                output.itemset((i, j, 2), 0)
            else:
                output[i, j] = rgb[i, j]
    return output


def erod(img, kernel):
    row, col, _ = img.shape
    canvas = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            hasil = 0

            if (i - kernel // 2 < 0) or (i + kernel // 2 > row - 1) or (j - kernel // 2) < 0 or (
                    j + kernel // 2 > col - 1):
                continue
            for ii in range(i - kernel // 2, i + kernel // 2 + 1):
                for jj in range(j - kernel // 2, j + kernel // 2 + 1):
                    if img[ii][jj] > 0:
                        hasil += 1
            if (hasil == kernel * kernel):
                canvas.itemset((i, j, 0), 255)
    return canvas


def dila(img, kernel):
    row, col, _ = img.shape
    canvas = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            hasil = 0

            if (i - kernel // 2 < 0) or (i + kernel // 2 > row - 1) or (j - kernel // 2) < 0 or (
                    j + kernel // 2 > col - 1):
                continue
            for ii in range(i - kernel // 2, i + kernel // 2 + 1):
                for jj in range(j - kernel // 2, j + kernel // 2 + 1):
                    if img[ii][jj] > 0:
                        hasil += 1
            if (hasil > 0):
                canvas.itemset((i, j, 0), 255)
    return canvas

