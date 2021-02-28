import numpy as np
import cv2

obj_img = cv2.imread("imgs/cachorro1.jpeg")

from matplotlib import pyplot as plt
obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)
plt.imshow(obj_img)
plt.show()