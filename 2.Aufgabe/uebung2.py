from skimage import io, exposure
from matplotlib import pyplot as plt
import numpy as np


def aufgabe2(img_path):
    img = io.imread(img_path)
    gray = convert_to_grayscale(img)
    histo = compute_histo(gray)
    cumhisto = cumHisto(histo)
    #linhisto = equalizeImg(gray)
    f, axarr = plt.subplots(2, 2)
    f.suptitle("Aufgabe 2", fontsize=16)
    axarr[0, 0].imshow(img)
    axarr[0, 0].set_title('original')
    axarr[0, 1].bar(range(0, 256), height=histo, color='k')
    axarr[0, 1].set_title('histo')
    axarr[1, 0].bar(range(0, 256), height=cumhisto, color='k')
    axarr[1, 0].set_title('cumhisto')
    #axarr[1, 1].bar(range(0, 256), height=linhisto, color='k')
    #axarr[1, 1].set_title('linhisto')
    plt.show()


def aufgabe4(img_path, ref_img_path):
    # imread both pictures
    img = io.imread(img_path)
    ref_img = io.imread(ref_img_path)

    # convert to grayscale
    gray_img = convert_to_grayscale(img)
    gray_ref_img = convert_to_grayscale(ref_img)

    # compute histogram
    histo_img = compute_histo(gray_img)
    histo_ref_img = compute_histo(gray_ref_img)

    # compute cumulative histogram
    cumhisto_img = cumHisto(histo_img)
    cumhisto_ref_img = cumHisto(histo_ref_img)

    # Create Look-Up-Table
    lut = match_Histo(histo_img, histo_ref_img)

    # Modified Picture, Histogram, Cumulative Histogram
    mod_img = apply_lut(lut, gray_img)
    histo_mod_img = compute_histo(mod_img)
    cumhisto_mod_img = cumHisto(histo_mod_img)
    # Plot Aufgabe 4
    f, axarr = plt.subplots(3, 3)
    f.suptitle("Aufgabe 4", fontsize=16)
    # Normal Pictures
    axarr[0, 0].imshow(gray_ref_img, cmap=plt.get_cmap(name='gray'))
    axarr[0, 0].set_title('Referenzbild')
    axarr[0, 1].imshow(gray_img, cmap=plt.get_cmap(name='gray'))
    axarr[0, 1].set_title('Originalbild')
    axarr[0, 2].imshow(mod_img, cmap=plt.get_cmap(name='gray'))
    axarr[0, 2].set_title('Modifiziertes Bild')

    # Histograms
    axarr[1, 0].bar(range(0, 256), height=histo_ref_img, color='k')
    axarr[1, 0].set_title('histo_ref_img')
    axarr[1, 1].bar(range(0, 256), height=histo_img, color='k')
    axarr[1, 1].set_title('histo_img')
    axarr[1, 2].bar(range(0, 256), height=histo_mod_img, color='k')
    axarr[1, 2].set_title('histo_mod_img')
    # Cumulative Histograms
    axarr[2, 0].bar(range(0, 256), height=cumhisto_ref_img, color='k')
    axarr[2, 0].set_title('cumhisto_ref_img')
    axarr[2, 1].bar(range(0, 256), height=cumhisto_img, color='k')
    axarr[2, 1].set_title('cumhisto_img')
    axarr[2, 2].bar(range(0, 256), height=cumhisto_mod_img, color='k')
    axarr[2, 2].set_title('cumhisto_mod_img')
    plt.show()


def cumHisto(histo): # Buch S. 71, PDF S. 86
    K = len(histo)
    n = 0
    for i in range(0, K):
        n += histo[i]

    P = np.zeros(K)
    c = histo[0]
    P[0] = c / n
    for i in range(1, K):
        c += histo[i]
        P[i] = c / n

    return P


def equalizeImg(bild):
    h, w = bild.shape
    M = w * h
    K = 256
    count = 0
    histo = compute_histo(bild)
    cumulativeHisto = cumHisto(histo)
    for i in range(0, h):
        for j in range(0, w):
            a = bild[i][j]
            b = cumulativeHisto[round(a)] * (K - 1) / M
            bild[i][j] = b
            count += 1
            print(count)
    bild = compute_histo(bild)
    bild = cumHisto(bild)
    return bild

def match_Histo(img_histo, ref_histo): # Buch S. 71, PDF S. 86
    K = len(img_histo)
    PA = cumHisto(img_histo)
    PR = cumHisto(ref_histo)
    F = np.zeros(K)

    for a in range(0, K):
        j = K-1
        while True:
            F[a] = j
            j -= 1
            if (not (j>=0 and PA[a] <= PR[j])):
                break
    return F

def apply_lut(lut, image):
    new_img = image.copy()
    for i, row in enumerate(new_img):
        for j, value in enumerate(row):
            new_img[i][j] = lut[round(value)]

    return new_img


def convert_to_grayscale(img):
    gray = lambda rgb: np.dot(rgb[..., :3], [0.299, 0.587, 0.114])
    return gray(img)


def compute_histo(img):
    array = np.zeros(256)
    for row in img:
        for value in row:
            array[round(value)] += 1
    return array


if __name__ == "__main__":
    # aufgabe2("bild01.jpg", 100)
    aufgabe4('bild01.jpg', 'bild02.jpg')
    # aufgabe3_old("bild01.jpg")
    # aufgabe3('bild01.jpg')
    exit(0)
