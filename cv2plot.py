import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('black.jpg')
print(img)

plt.show(img)
plt.plot([300,300,600,600],[600,600,1200,300],'--r')
plt.show()
