import numpy as np
import cv2


def image_show(image, nrows=1, ncols=1, cmap='gray', **kwargs):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(10, 10))
    ax.imshow(image, cmap=cmap)
    ax.axis('off')
    return fig, ax


def segment_image(img):
    h = img.shape[0]
    blue, green, red = img[h//2:, :, 0], img[h//2:, :, 1], img[h//2:, :, 2]
    mask = np.zeros(red.shape)
    for x in range(mask.shape[0]):
        for y in range(mask.shape[1]):
            if red[x, y] < 35 and blue[x, y] > 30 and green[x, y] > 30:
                mask[x, y] = 1
    return mask


def is_right(img):
    mask = segment_image(img)
    right = np.sum(mask[:, mask.shape[1]//2:])
    left = np.sum(mask[:, :mask.shape[1]//2])
    if right > left:
        return True
    return False
