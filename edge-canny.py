'''
利用canny算子进行边缘检测
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import torch

# 4000帧统计出来的可能出现新目标的区域
# [256, 336, 293, 371]
# [300, 1640, 335, 1675]
# [346, 1629, 420, 1691]
# [206, 125, 259, 208]
# [81, 82, 154, 175]
# [289, 1530, 396, 1601]
area_new_obj=[[256, 336, 293, 371],[300, 1640, 335, 1675],[346, 1629, 420, 1691],[206, 125, 259, 208],[81, 82, 154, 175],[289, 1530, 396, 1601]]

def edge_calculate(img):
    # 灰度化处理图像
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 高斯滤波降噪
    gaussian = cv2.GaussianBlur(grayImage, (3, 3), 0)
    # Canny算子
    Canny = cv2.Canny(gaussian, 80, 170)
    num = 0
    time_begin = time.time()
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if Canny[i][j] == 255:
                num = num + 1
    time_end = time.time()
    # print(num)
    # print(time_end-time_begin)
    # print("#------------------------------------------#")
    return num

for i in range(0,len(area_new_obj)):
    frame_edge = {}
    print([area_new_obj[i][0],area_new_obj[i][2],area_new_obj[i][1],area_new_obj[i][3]])
    for index in range(1, 600):
        frame = str(index)
        img = cv2.imread(r"/home/zhiqiang/PycharmProjects/efficientdet-pytorch-2.0/img/subway_frame/" + frame + ".jpg")
        img = img[area_new_obj[i][0]:area_new_obj[i][2],area_new_obj[i][1]:area_new_obj[i][3]]
        num = edge_calculate(img)
        frame_edge[index] = num
    print("##---compute_end___#_box:",i)
    sign=str(i)
    torch.save(frame_edge, "/home/zhiqiang/project/frame_edge_dict_subway"+sign+".pkl")





