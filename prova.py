# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io


f = open('C:\\Users\\joasm\\OneDrive\\Área de Trabalho\\m1.txt')
triplets = f.read().split()
for i in range(0, len(triplets)): triplets[i]=triplets[i].split(',') 
a = np.array(triplets, dtype = np.uint8)
b = np.reshape(a, (3, 3))

plt.imshow(b)
plt.savefig('C:\\Users\\joasm\\OneDrive\\Área de Trabalho\\imagem.png')




#Criando o histrograma
import numpy as np
import matplotlib.pyplot as plt
import cv2



im = cv2.imread('C:\\Users\\joasm\\OneDrive\\Área de Trabalho\\imagem.png')
vals = im.mean(axis= 2).flatten()
counts,bins = np.histogram(vals, range(100))
plt.bar(bins[:1] - 0.5, counts, width= 1, edgecolor= 'none')
plt.xlim([-0.5, 100.5])
plt.show()


