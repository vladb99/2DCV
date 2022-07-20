from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math

def apply_structure_element(img, filter, offset, iter_num, is_dilation):
    # Buch S. 98 (S.113 PDF)
    height, width = np.shape(img)

    # NxN Filter
    N, _ = np.shape(filter)

    # 2K + 1 = N
    K = math.floor(N / 2)

    copy = np.zeros((math.ceil(height / offset), math.ceil(width / offset)))

    for _ in range(iter_num):
        stride_x = K
        for x in range(K, height-K, offset):
            stride_y = K
            for y in range(K, width-K, offset):
                sums_list = []
                for i in range(-K, K+1):
                    for j in range(-K, K+1):
                        pixel = img[x+i, y+j]
                        coefficient = filter[i+K, j+K]

                        replacement = 0
                        if (is_dilation and coefficient is not None):
                            replacement = pixel + coefficient
                            sums_list.append(replacement)
                        elif(not is_dilation and coefficient is not None):
                            replacement = pixel - coefficient
                            sums_list.append(replacement)

                            
                q = 0
                if (is_dilation):
                    q = max(sums_list)
                else:
                    q = min(sums_list)
                
                if (q < 0):
                    q = 0
                if (q > 255):
                    q = 255

                copy[stride_x, stride_y] = q
                stride_y += 1
            stride_x += 1
    return copy

def erode(img, filter, iter_num):
    return apply_structure_element(img, filter, 1, iter_num, False)

def dilate(img, filter, iter_num):
    return apply_structure_element(img, filter, 1, iter_num, True)

def opening(img, filter):
    img = erode(img, filter, 1)
    return dilate(img, filter, 1)

def closing(img, filter):
    img = dilate(img, filter, 1)
    return erode(img, filter, 1)

def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

if __name__ == "__main__":
    # read img
    img = io.imread("6.Aufgabe/cactus.jpg")

    # convert to numpy array
    img = np.array(img)

    # convert to grayscale
    #img = rgb2gray(img)

    f1 = np.array([
        [1, 1, 1],
        [1, 2, 1],
        [1, 1, 1]
    ])

    f2 = np.array([
        [1,1,1],
        [1,2,1],
        [1,1,1],
    ])

    element = np.array([[None,None,None,None,None,None,5],
                        [None,None,None,None,5,5,None],
                        [None,None,None,5,5,5,None],
                        [5,5,5,5,5,None,None],
                        [None,5,5,5,5,None,None],
                        [None,5,5,5,None,None,None],
                        [5,None,None,5,None,None,None]])

    #for _ in range(5):
    new_img = closing(img, element)
    #new_img = dilate(new_img, f2, 1)

    # opening: erosion und dann dilation
    # closing: dilation und dann erosion

    #test = np.array([[6,7,3,4], [5,6,6,8], [6,4,5,2], [6,4,2,3]])
    #dilated_test = erode(test, filter, 1)
    #print(dilated_test)

    plt.figure(1)
    plt.subplot(211)
    plt.imshow(img, cmap=cm.Greys_r)
    plt.figure(1)
    plt.subplot(212)
    plt.imshow(new_img, cmap=cm.Greys_r)
    plt.show()