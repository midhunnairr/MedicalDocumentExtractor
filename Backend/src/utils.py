import cv2
import numpy as np


def image_processing(page):
    grayscale_image = cv2.cvtColor(np.array(page), cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(grayscale_image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    processed_image = cv2.adaptiveThreshold(resized_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY, 61, 11)

    return processed_image
