from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
#from scipy.ndimage.filters import generic_filter


def sobel_operator():
    Hx = np.array([[1], [2], [1]]) * np.array([[-1, 0, 1]])
    Hy = np.array([[1, 2, 1]]) * np.array([[-1], [0], [1]])
    return Hx, Hy


def first_derivation_horizontal(img):
    height, width = np.shape(img)
    copy = np.zeros((height, width))

    for i, row in enumerate(img):
        for j, value in enumerate(row):
            if j == 0:
                copy[i, j] = (int(img[i, j + 1]) - int(img[i, j]))
            elif j == width - 1:
                copy[i, j] = (int(img[i, j]) - int(img[i, j - 1]))
            else:
                copy[i, j] = 0.5 * (int(img[i, j + 1]) - int(img[i, j - 1]))

    return copy


def first_derivation_vertically(img):
    out_img = np.transpose(img)
    height, width = np.shape(out_img)

    copy = np.zeros((height, width))

    for i, row in enumerate(out_img):
        for j, value in enumerate(row):
            if j == 0:
                copy[i, j] = (int(out_img[i, j + 1]) - int(out_img[i, j]))
            elif j == width - 1:
                copy[i, j] = (int(out_img[i, j]) - int(out_img[i, j - 1]))
            else:
                copy[i, j] = 0.5 * (int(out_img[i, j + 1]) - int(out_img[i, j - 1]))

    copy = np.transpose(copy)
    return copy


def edge_strength(img):
    height, width = np.shape(img)

    copy = np.zeros(height, width)
    horizontal_derivation = first_derivation_horizontal(img)
    vertically_derivation = first_derivation_vertically(img)
    for i, row in enumerate(img):
        for j, value in enumerate(row):
            copy[i, j] = np.sqrt(np.power(horizontal_derivation[i, j], 2) + np.power(vertically_derivation[i, j], 2))

    return copy


def sobel_filter(img, offset, edge):
    s_vert, s_hor = sobel_operator()
    height, width = np.shape(img)

    # NxN Filter
    N, _ = np.shape(s_vert)

    # 2K + 1 = N
    K = math.floor(N / 2)

    copy = np.zeros((math.ceil(height / offset), math.ceil(width / offset)))

    stride_x = 0
    stride_y = 0

    for x in range(0, height, offset):
        stride_y = 0
        for y in range(0, width, offset):
            sum_hor = 0
            sum_vert = 0
            for i in range(-K, K + 1):
                for j in range(-K, K + 1):
                    coefficient_hor = s_hor[i + K, j + K]
                    coefficient_vert = s_vert[i + K, j + K]

                    pixel = -1
                    if 0 <= x + i < height and 0 <= y + j < width:
                        pixel = img[x + i, y + j]
                    elif edge == 'min':
                        pixel = 0
                    elif edge == 'max':
                        pixel = 255
                    elif edge == 'continue':
                        # Up side -
                        if x + i < 0 and 0 <= y + j < width:
                            pixel = img[height + i, y + j]
                        # Left up diagonal -
                        elif x + i < 0 and y + j < 0:
                            pixel = img[height + i, width + j]
                        # Right up diagonal -
                        elif x + i < 0 and y + j >= width:
                            pixel = img[height + i, j - 1]
                        # Left side -
                        elif 0 <= x + i < height and y + j < 0:
                            pixel = img[x + i, width + j]
                        # Right side -
                        elif 0 <= x + i < height and y + j >= width:
                            pixel = img[x + i, j - 1]
                        # Bottom side -
                        elif x + i >= height and 0 <= y + j < width:
                            pixel = img[i - 1, y + j]
                        # Left down diagonal -
                        elif x + i >= height and y + j < 0:
                            pixel = img[i - 1, width + j]
                        # Right down diagonal -
                        elif x + i >= height and y + j >= width:
                            pixel = img[i - 1, j - 1]

                    assert (pixel != -1)
                    sum_hor = sum_hor + coefficient_hor * pixel
                    sum_vert = sum_vert + coefficient_vert * pixel
            q = sum_vert
            q = round(q)
            if q < 0:
                q = 0
            if q > 255:
                q = 255
            copy[stride_x, stride_y] = q
            stride_y += 1
        stride_x += 1
    return copy


def sobel_filter_2(P):
    return (np.abs((P[0] + 2 * P[1] + P[2]) - (P[6] + 2 * P[7] + P[8])) +
            np.abs((P[2] + 2 * P[6] + P[7]) - (P[0] + 2 * P[3] + P[6])))


def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray


if __name__ == "__main__":
    # read img
    img = io.imread("4.Aufgabe/test.png")

    # convert to numpy array
    img = np.array(img)

    # convert to grayscale
    img = rgb2gray(img)

    #out_img = first_derivation_vertically(img)
    out_img = sobel_filter(img, 1, 'continue')
    #out_img = generic_filter(img, sobel_filter_2, (3, 3))

    plt.figure(1)
    plt.subplot(211)
    plt.imshow(img, cmap=cm.Greys_r)
    plt.figure(1)
    plt.subplot(212)
    plt.imshow(out_img, cmap=cm.Greys_r)
    plt.show()
