from skimage import io
from matplotlib import pyplot as plt
import numpy as np


def aufgabe1(img_path):
    img = io.imread(img_path)

    red_image = img[:, :, 0]
    green_image = img[:, :, 1]
    blue_image = img[:, :, 2]

    f, axarr = plt.subplots(2, 2)
    f.suptitle("Aufgabe 1, 4)", fontsize=16)
    axarr[0, 0].imshow(img)
    axarr[0, 0].set_title('original')
    axarr[0, 1].imshow(red_image, cmap="gray")
    axarr[0, 1].set_title('red')
    axarr[1, 0].imshow(green_image, cmap="gray")
    axarr[1, 0].set_title('green')
    axarr[1, 1].imshow(blue_image, cmap="gray")
    axarr[1, 1].set_title('blue')
    plt.show()

    f, axarr = plt.subplots(2, 2)
    f.suptitle("Aufgabe 1, 5)", fontsize=16)
    axarr[0, 0].imshow(img)
    axarr[0, 0].set_title('original')
    axarr[0, 1].imshow(horizontal_mirror(img))
    axarr[0, 1].set_title('horizontal')
    axarr[1, 0].imshow(vertical_mirror(img))
    axarr[1, 0].set_title('vertical')
    plt.show()


def aufgabe2():
    img1 = io.imread('bild01.jpg')
    img2 = io.imread('bild02.jpg')
    img3 = io.imread('bild03.jpg')
    img4 = io.imread('bild04.jpg')
    img5 = io.imread('bild05.jpg')

    gray1 = convert_to_grayscale(img1)
    gray2 = convert_to_grayscale(img2)
    gray3 = convert_to_grayscale(img3)
    gray4 = convert_to_grayscale(img4)
    gray5 = convert_to_grayscale(img5)

    histo1 = compute_histo(gray1)
    histo2 = compute_histo(gray2)
    histo3 = compute_histo(gray3)
    histo4 = compute_histo(gray4)
    histo5 = compute_histo(gray5)

    fig, axarr = plt.subplots(5, 2)
    fig.suptitle('Aufgabe 2, 4)')
    axarr[0, 0].imshow(gray1, cmap=plt.get_cmap(name='gray'))
    axarr[0, 0].set_title('bild01')
    axarr[0, 1].bar(range(0, 256), height=histo1, color='k')
    axarr[0, 1].set_title('bild01-hist')
    axarr[1, 0].imshow(gray2, cmap=plt.get_cmap(name='gray'))
    axarr[1, 0].set_title('bild02')
    axarr[1, 1].bar(range(0, 256), height=histo2, color='k')
    axarr[1, 1].set_title('bild02-hist')
    axarr[2, 0].imshow(gray3, cmap=plt.get_cmap(name='gray'))
    axarr[2, 0].set_title('bild03')
    axarr[2, 1].bar(range(0, 256), height=histo3, color='k')
    axarr[2, 1].set_title('bild03-hist')
    axarr[3, 0].imshow(gray4, cmap=plt.get_cmap(name='gray'))
    axarr[3, 0].set_title('bild04')
    axarr[3, 1].bar(range(0, 256), height=histo4, color='k')
    axarr[3, 1].set_title('bild04-hist')
    axarr[4, 0].imshow(gray5, cmap=plt.get_cmap(name='gray'))
    axarr[4, 0].set_title('bild05')
    axarr[4, 1].bar(range(0, 256), height=histo5, color='k')
    axarr[4, 1].set_title('bild05-hist')
    plt.show()


def aufgabe3(img_path):
    img = io.imread(img_path)
    gray = convert_to_grayscale(img)
    table = look_up_table(256, 0.8)
    brightened_image = brighten(gray, table)

    histo1 = compute_histo(gray)
    histo2 = compute_histo(brightened_image)

    fig, axarr = plt.subplots(2, 2)
    fig.suptitle('Aufgabe 2, 5)')
    axarr[0, 0].imshow(gray, cmap=plt.get_cmap(name='gray'))
    axarr[0, 0].set_title('bild01')
    axarr[0, 1].bar(range(0, 256), height=histo1, color='k')
    axarr[0, 1].set_title('bild01-hist')
    axarr[1, 0].imshow(brightened_image, cmap=plt.get_cmap(name='gray'))
    axarr[1, 0].set_title('bild02-brightened')
    axarr[1, 1].bar(range(0, 256), height=histo2, color='k')
    axarr[1, 1].set_title('bild02-brightened-hist')
    plt.show()


# Siehe Buch Digitale Bildverarbeitung (Seite 79 Buch, Seite 94 PDF)
def look_up_table(k, gamma):
    aMax = k - 1

    table = np.zeros(k)
    for i, _ in enumerate(table):
        aa = i / aMax
        bb = pow(aa, gamma)
        b = round(bb * aMax)
        table[i] = b
    return table


def brighten(img, table):
    brightened_img = np.copy(img)
    for i, row in enumerate(brightened_img):
        for j, value in enumerate(row):
            brightened_img[i, j] = table[round(value)]
            if brightened_img[i, j] > 255:
                brightened_img[i, j] = 255
    return brightened_img


def convert_to_grayscale(img):
    gray = lambda rgb: np.dot(rgb[..., :3], [0.299, 0.587, 0.114])
    return gray(img)


def compute_histo(img):
    array = np.zeros(256)
    for row in img:
        for value in row:
            array[round(value)] += 1
    return array


def vertical_mirror(img_numpy):
    return np.array([list(reversed(row)) for row in img_numpy])


def horizontal_mirror(img_numpy):
    return np.array(list(reversed(img_numpy)))


if __name__ == "__main__":
    # aufgabe1('monkey.jpg')
    # aufgabe2()
    # aufgabe3_old("bild01.jpg")
    aufgabe3('bild01.jpg')
    exit(0)
