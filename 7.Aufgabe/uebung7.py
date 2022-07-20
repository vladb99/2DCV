from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
import cv2
import imageio as iio

def make_img_binary(img, threshold):
    # converting to its binary form
    _, bw_img = cv2.threshold(img, threshold, 1, cv2.THRESH_BINARY)        
    return bw_img

def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def all_neighbors_are_background(img, x, y, width):
    n1 = 0 if y-1 < 0 else img[x][y-1]
    n2 = 0 if y-1 < 0 or x-1 < 0 else img[x-1][y-1]
    n3 = 0 if x-1 < 0 else img[x-1][y]
    n4 = 0 if x-1 < 0 or y+1 < 0 or y+1 >= width else img[x-1][y+1]

    if n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0:
        return True

def exactly_one_neighbor_label(img, x, y, width):
    n1 = 0 if y-1 < 0 else img[x][y-1]
    n2 = 0 if y-1 < 0 or x-1 < 0 else img[x-1][y-1]
    n3 = 0 if x-1 < 0 else img[x-1][y]
    n4 = 0 if x-1 < 0 or y+1 < 0 or y+1 >= width  else img[x-1][y+1]

    n_list = [n1, n2, n3, n4]
    n_list = [e for e in n_list if e > 1]

    if len(n_list) == 1:
        return (True, n_list[0])
    else: 
        return (False, -1)

def several_neighbors_have_label(img, x, y, width):
    n1 = 0 if y-1 < 0 else img[x][y-1]
    n2 = 0 if y-1 < 0 or x-1 < 0 else img[x-1][y-1]
    n3 = 0 if x-1 < 0 else img[x-1][y]
    n4 = 0 if x-1 < 0 or y+1 < 0 or y+1 >= width else img[x-1][y+1]

    n_list = [n1, n2, n3, n4]
    n_list = [e for e in n_list if e > 1]

    if len(n_list) > 1:
        return (True, n_list.pop(0), n_list)
    else: 
        return (False, -1, [])

def assign_initial_labels(img):
    m = 2
    collisions_set = set()
    height, width = np.shape(img)

    copy = np.copy(img)
    preliminary_region_labels = set()

    for x in range(height):
        for y in range(width):
            if copy[x, y] == 0:
                has_one, n1 = exactly_one_neighbor_label(copy, x, y, width)
                has_several, k, rest_labels = several_neighbors_have_label(copy, x, y, width)
                if all_neighbors_are_background(copy, x, y, width):
                    copy[x, y] = m
                    preliminary_region_labels.add(m)
                    m += 1
                elif has_one:
                    copy[x, y] = n1
                elif has_several:
                    copy[x, y] = k
                    for label in rest_labels:
                        if label != k:
                            collisions_set.add((label, k))
    return (copy, collisions_set, preliminary_region_labels)

def resolve_label_collisions(collisions_set, preliminary_region_labels):
    partitioning_list = list()
    for region_label in preliminary_region_labels:
        new_set = set()
        new_set.add(region_label)
        partitioning_list.append(new_set)

    for collision in collisions_set:
        a, b = collision
        a_index = 0
        b_index = 0
        for i, partition in enumerate(partitioning_list):
            if a in partition:
                a_index = i
            if b in partition:
                b_index = i
        if a_index != b_index:
            for e in partitioning_list[b_index]:
                partitioning_list[a_index].add(e)
            partitioning_list[b_index] = set()
    return partitioning_list

def relabel_the_image(img, partitioning_list):
    height, width = np.shape(img)
    for x in range(height):
        for y in range(width):
            for s in partitioning_list:
                if img[x, y] in s:
                    img[x, y] = min(s)
    return img

def sequential_labeling(img):
    copy, collisions_set, preliminary_region_labels = assign_initial_labels(img)
    partitioning_list = resolve_label_collisions(collisions_set, preliminary_region_labels)
    return relabel_the_image(copy, partitioning_list)

if __name__ == "__main__":
    # read img
    img = iio.v3.imread("7.Aufgabe/regionen1.png")

    # convert to numpy array
    img = np.array(img)

    # convert to grayscale
    #img = rgb2gray(img)

    img = make_img_binary(img, 0)
    result = sequential_labeling(img)

    plt.figure(1)
    plt.subplot(211)
    plt.imshow(img, cmap=cm.Greys_r)
    plt.figure(1)
    plt.subplot(212)
    plt.imshow(result, cmap=cm.Greys_r)
    plt.show()