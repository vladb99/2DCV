from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def linear_ht(img, angle_steps, radius_steps):
    height, width = np.shape(img)

    xCtr = width / 2
    yCtr = height / 2

    dAng = np.pi/angle_steps

    rMax = np.sqrt(xCtr**2 + yCtr**2)
    dRad = (2*rMax)/radius_steps

    hough_array = np.zeros((angle_steps, radius_steps))
    
    for v in range(0, height):
        for u in range(0, width):
            # Must be equal 0, because the points of the lines in the image is black
            if (img[v, u] == 0):
                x = u - xCtr
                y = v - yCtr

                for a in range(angle_steps):
                    theta = dAng * a
                    r = int(round((x*np.cos(theta) + y*np.sin(theta)) / dRad) + radius_steps/2)
                    if (r >= 0 and r < radius_steps):
                        hough_array[r, a] += 1
    return hough_array

def apply_threshold(hough_array):   
    hough_array[hough_array <= 127] = 0

def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

if __name__ == "__main__":
    # read img
    img = io.imread("5.Aufgabe/noisy-lines.tif")

    # convert to numpy array
    img = np.array(img)

    # convert to grayscale
    #img = rgb2gray(img)

    out_img = linear_ht(img, 256, 256)
    tmp = out_img.copy()
    apply_threshold(out_img)

    plt.figure(1)
    plt.subplot(311)
    plt.imshow(img, cmap=cm.Greys_r)
    plt.figure(1)
    plt.subplot(312)
    plt.imshow(tmp, cmap=cm.Greys_r)
    plt.figure(1)
    plt.subplot(313)
    plt.imshow(out_img, cmap=cm.Greys_r)
    plt.show()