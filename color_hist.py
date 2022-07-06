# 掩膜直方图
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#读取图像
img = cv2.imread(r'/home/zhiqiang/PycharmProjects/efficientdet-pytorch-2.0/img/subway_frame/139.jpg')

#转换为RGB图像
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(8, 6))
#25
#img_rgb[314:410,1617:1695]=255
# 26
#img_rgb[319:414,1617:1693]=255
# 27 subway_light
#img_rgb[319:415,1618:1694]=255
# 139
img_rgb[374:460,1619:1683]=255
#设置字体
# matplotlib.rcParams['font.sans-serif']=['SimHei']

plt.imshow(img_rgb)
plt.title("(a)yuan_tu")

#设置掩膜
# mask = np.zeros(img.shape[:2], np.uint8)
# mask[100:300, 100:300] = 255
# masked_img = cv2.bitwise_and(img, img, mask=mask)



#图像直方图计算
hist_full_1 = cv2.calcHist([img], [0], None, [256], [0,256]) #通道[0]-灰度图
hist_full_2 = cv2.calcHist([img], [1], None, [256], [0,256]) #通道[0]-灰度图
hist_full_3 = cv2.calcHist([img], [2], None, [256], [0,256]) #通道[0]-灰度图

# #图像直方图计算(含掩膜)
# hist_mask = cv2.calcHist([img], [0], mask, [256], [0,256])



# #绘制直方图
plt.figure(figsize=(8, 6))
plt.plot(hist_full_1)
plt.plot(hist_full_2)
plt.plot(hist_full_3)

plt.title("(d)hist")
plt.xlabel("x")
plt.ylabel("y")
plt.show()