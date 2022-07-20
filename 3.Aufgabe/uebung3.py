from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math

def filter1(img, filter, offset):
    # Buch S. 98 (S.113 PDF)
    height, width = np.shape(img)

    # NxN Filter
    N, _ = np.shape(filter)

    # 2K + 1 = N
    K = math.floor(N / 2)

    copy = np.zeros((math.ceil(height / offset), math.ceil(width / offset)))

    stride_x = 0
    stride_y = 0

    for x in range(K, height-K, offset):
        stride_y = 0
        for y in range(K, width-K, offset):
            sum = 0
            for i in range(-K, K+1):
                for j in range(-K, K+1):
                    pixel = img[x+i, y+j]
                    coefficient = filter[i+K, j+K]
                    sum = sum + coefficient * pixel
            q = round(sum)
            if (q < 0):
                q = 0
            if (q > 255):
                q = 255
            copy[stride_x, stride_y] = q
            stride_y += 1
        stride_x += 1
    return copy


def filter2(img, filter, offset, edge):
    # Buch S. 98 (S.113 PDF)
    height, width = np.shape(img)

    # NxN Filter
    N, _ = np.shape(filter)

    # 2K + 1 = N
    K = math.floor(N / 2)

    copy = np.zeros((math.ceil(height / offset), math.ceil(width / offset)))

    stride_x = 0
    stride_y = 0

    for x in range(0, height, offset):
        stride_y = 0
        for y in range(0, width, offset):
            sum = 0
            for i in range(-K, K+1):
                for j in range(-K, K+1):
                    coefficient = filter[i+K, j+K]

                    pixel = -1
                    if (x+i >= 0 and x+i < height and y+j >= 0 and y+j < width):
                        pixel = img[x+i, y+j]
                    elif (edge == 'min'):
                        pixel = 0
                    elif (edge == 'max'):
                        pixel = 255
                    elif (edge == 'continue'):
                        # Up side -
                        if (x+i < 0 and y+j >= 0 and y+j < width):
                            pixel = img[height + i, y+j]
                        # Left up diagonal -
                        elif (x+i < 0 and y+j < 0):
                            pixel = img[height + i, width + j]
                        # Right up diagonal -
                        elif (x+i < 0 and y+j >= width):
                            pixel = img[height + i, j - 1]
                        # Left side -
                        elif(x+i >= 0 and x+i < height and y+j < 0):
                            pixel = img[x+i, width + j]
                        # Right side -
                        elif(x+i >= 0 and x+i < height and y+j >= width):
                            pixel = img[x+i, j - 1]
                        # Bottom side -
                        elif (x+i >= height and y+j >= 0 and y+j < width):
                            pixel = img[i - 1, y+j]
                        # Left down diagonal -
                        elif (x+i >= height and y+j < 0):
                            pixel = img[i - 1, width + j]
                        # Right down diagonal -
                        elif (x+i >= height and y+j >= width):
                            pixel = img[i - 1, j - 1]

                    assert(pixel != -1)
                    sum = sum + coefficient * pixel
            q = round(sum)
            if (q < 0):
                q = 0
            if (q > 255):
                q = 255
            copy[stride_x, stride_y] = q
            stride_y += 1
        stride_x += 1
    return copy

def medianFilter(in_image, filter_size, offset):
    # Buch S. 111 (S. 126 PDF)
    height, width = np.shape(in_image)

    # NxN Filter
    N = filter_size

    # 2K + 1 = N
    K = math.floor(N / 2)

    out_image = np.zeros((math.ceil(height / offset), math.ceil(width / offset)))

    stride_x = 0
    stride_y = 0

    # vector to hold pixels from 3x3 neighborhood
    P = np.zeros(N * N)

    for x in range(K, height-K, offset):
        stride_y = 0
        for y in range(K, width-K, offset):
            # fill the pixel vector P for filter position (u,v)
            k = 0
            for i in range(-K, K+1):
                for j in range(-K, K+1):
                    #print(x+i)
                    #print(y+j)
                    P[k] = in_image[x+i][y+j]
                    k += 1

            # Sort the pixel vector and take center element
            heapSort(P)
            median = 0
            if ((N * N ) % 2 != 0):
                median = P[round(N * N / 2)]
            else:
                median = (P[N * N / 2] + P[N * N / 2 - 1]) / 2
            out_image[stride_x][stride_y] = median
            stride_y += 1
        stride_x += 1
    return out_image

# Python program for implementation of heap Sort
# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


# The main function to sort an array of given size

def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)



def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

def compute_histo(img):
    array = np.zeros(256)
    for row in img:
        for value in row:
            array[round(value)] += 1
    return array

if __name__ == "__main__":

    # read img
    img = io.imread("3.Aufgabe/lena.jpg")

    # convert to numpy array
    img = np.array(img)

    # convert to grayscale
    img = rgb2gray(img)

    # AUFGABE 1
    fm = np.array([
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ])

    # apply filter
    imgOut = filter1(img, fm , 1)
    #imgOut = filter2(img, fm , 1, 'continue')

    # show result
    plt.figure(1)
    plt.subplot(211)
    plt.imshow(img, cmap = cm.Greys_r)
    plt.figure(1)
    plt.subplot(212)
    plt.imshow(imgOut, cmap = cm.Greys_r)
    plt.show()

    # AUFGABE 2
    # read img
    img = io.imread("3.Aufgabe/pepper.jpg")
    #img = io.imread("3.Aufgabe/tree.png")

    # convert to numpy array (already gray scale)
    img = np.array(img)

    # apply filter
    imgOut = medianFilter(img, 3, 1)
    #imgOut = medianFilter(imgOut, 3, 1)
    #imgOut = medianFilter(imgOut, 3, 1)
    #imgOut = medianFilter(imgOut, 3, 1)
    #imgOut = medianFilter(imgOut, 3, 1)
    #imgOut = medianFilter(imgOut, 3, 1)
    #imgOut = medianFilter(imgOut, 3, 1)

    # compute Histo just to see the difference
    histo_img = compute_histo(img)
    histo_imgOut = compute_histo(imgOut)
    # plot img
    f, axarr = plt.subplots(2, 2)
    f.suptitle("Aufgabe 3.2", fontsize=16)
    axarr[0, 0].imshow(img, cmap=plt.get_cmap(name='gray'))
    axarr[0, 0].set_title('Lena')
    axarr[0, 1].imshow(imgOut, cmap=plt.get_cmap(name='gray'))
    axarr[0, 1].set_title('Lena mit Filter')

    # Histograms
    axarr[1, 0].bar(range(0, 256), height=histo_img, color='k')
    axarr[1, 0].set_title('histo_img')
    axarr[1, 1].bar(range(0, 256), height=histo_imgOut, color='k')
    axarr[1, 1].set_title('histo_imgOut')
    plt.show()
