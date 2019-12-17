Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
import numpy as np
import matplotlib.pyplot as plt
import cv2
im = cv2.imread('C:\Users\joasm\OneDrive\Área de Trabalho\imagem.png')
vals = im.mean(axis= 2).flatten()
counts,bins = np.histogram(vals, range(100))
plt.bar(bins[:1] - 0.5, counts, width= 1, edgecolor= 'none')
plt.xlim([-0.5, 100.5])
plt.show()
