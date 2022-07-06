import itertools
import numpy as np
import cv2
import torch
import matplotlib
import matplotlib.pyplot as plt
#import icecream
'''
通过递归的方法，将可能出现目标的区域中的，那些重合的矩形给合并成一个并集。
'''
matplotlib.use("TKAgg")

def remove_duplicated(boxes_list):
    res = []
    for i in boxes_list:
        if i not in res:
            res.append(i)
    return res

'''
输入是 x,y,w,h 
'''
def intersection(a, b):
    x = max(a[0], b[0])
    y = max(a[1], b[1])
    w = min(a[0] + a[2], b[0] + b[2]) - x
    h = min(a[1] + a[3], b[1] + b[3]) - y
    if w < 0 or h < 0: return ()  # or (0,0,0,0) ?
    return [x, y, w, h]


def union(a, b):
    x = min(a[0], b[0])
    y = min(a[1], b[1])
    w = max(a[0] + a[2], b[0] + b[2]) - x
    h = max(a[1] + a[3], b[1] + b[3]) - y
    return [x, y, w, h]


boxes = torch.load("/home/zhiqiang/project/new_obj_area_subway_4000.pkl")
new_list_boxes = []
for j in boxes:
    new_list_boxes.append([j[0], j[1], j[2] - j[0], j[3] - j[1]])

print(len(new_list_boxes))
new_result = []

def combine_boxes(boxes):
    num=0
    num_=len(boxes)-1
    for i in range(1, len(boxes)):

        if intersection(boxes[0], boxes[i]):
            tmp_0=boxes[0]
            tmp_i=boxes[i]
            box_tmp = union(boxes[0], boxes[i])
            boxes.remove(tmp_0)
            boxes.remove(tmp_i)
            boxes.append(box_tmp)
            break
        else:
            num=num+1
    if num==num_:
        return 0



while True:
    tmp = combine_boxes(new_list_boxes)
    print(len(new_list_boxes))
    if tmp==0:
        new_result.append(new_list_boxes[0])
        tmp=new_list_boxes[0]
        new_list_boxes.remove(tmp)
    if len(new_list_boxes) == 1:
        new_result.append(new_list_boxes[0])
        break

print("new_result",len(new_result))

img = cv2.imread('/home/zhiqiang/PycharmProjects/efficientdet-pytorch-2.0/img/subway_frame/1.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

for i in new_result:
    #print(i[0],i[1],i[0]+i[2],i[1]+i[3])
    img_rgb[i[0]:(i[0]+i[2]),i[1]:(i[1]+i[3])]=255
plt.figure(figsize=(8, 6))
plt.imshow(img_rgb)
plt.show()