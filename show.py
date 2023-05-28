import nibabel as nib
from nibabel.viewers import OrthoSlicer3D
import skimage.io as io
import numpy as np
from matplotlib import pylab as plt
import matplotlib

#导入nii文件
img=nib.load('23w3d.nii')

print(img.dataobj.shape)

width, height, queue = img.dataobj.shape

#3D图
OrthoSlicer3D(img.dataobj).show()

#每次切割的步长
x = int((queue/10) ** 0.5) + 1
num = 1

#按步长进行切割显示
for i in range(0, queue, 10):
    img_arr = img.dataobj[:, :, i]
    plt.subplot(x, x, num)
    plt.imshow(img_arr, cmap='gray')
    num += 1
 
plt.show()
