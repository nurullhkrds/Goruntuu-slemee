import cv2
import numpy as np
from matplotlib import pyplot as plt


resim=cv2.imread("ari.jpg",0)
#cv2.imshow("ari",foto)
cv2.waitKey()

hist= np.zeros(256)
[h,w]=np.shape(resim)

for i in range (0,h):
    for j in range (0,w):
        a=resim[i,j]
        hist[a]=hist[a]+1

for i in range (0,256):
    print(i,"=",hist[i])



# aşağıda tek tek BGR kanallarının ayrı ayrı  OpenCv fonksiyonu ile histogram yoğunluğunu gösterdim.

# B kanalının hist yoğunluğu için [0] kanalını girdim
hist_B = cv2.calcHist([resim], [0], None, [256], [0, 256])

plt.plot(hist_B, color='b')
plt.title('Histogram Blue')
plt.show()


# G kanalının hist yoğunluğu için [1] kanalını girdim

hist_G = cv2.calcHist([resim], [1], None, [256], [0, 256])

plt.plot(hist_G, color='g')
plt.title('Histogram Gren ')
plt.show()
