'''


'''
import cv2
import time
import torch
# img_1=cv2.imread(r'F:\\PycharmProjects\\efficientdet-pytorch-2.0\\img\\subway_frame\\351.jpg')
# img_2=cv2.imread(r'F:\\PycharmProjects\\efficientdet-pytorch-2.0\\img\\subway_frame\\352.jpg')
# begin=time.time()
# img1=cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
# img2=cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
# #img=cv2.subtract(img1, img2, dst=None, mask=None, dtype=None)
# diff=0
# for i in range(0,img1.shape[0]):
#     for j in range(0,img1.shape[1]):
#         if  abs(int(img1[i][j])-int(img2[i][j]))>35:
#             diff=diff+1
# end=time.time()
# print(diff,end-begin)
# frame_diff={}
area_new_obj=[[256, 336, 293, 371],[300, 1640, 335, 1675],[346, 1629, 420, 1691],[206, 125, 259, 208],[81, 82, 154, 175],[289, 1530, 396, 1601]]
def different_calculate(img1,img2):
    diff = 0
    for i in range(0, img1.shape[0]):
        for j in range(0, img1.shape[1]):
            if abs(int(img1[i][j]) - int(img2[i][j])) > 35:
                diff = diff + 1
    return diff

# for index in range(1,600):
#     frame1=str(index)
#     frame2=str(index+1)
#     img1=cv2.imread(r"/home/zhiqiang/PycharmProjects/efficientdet-pytorch-2.0/img/subway_frame/"+frame1+".jpg")
#     img2=cv2.imread(r"/home/zhiqiang/PycharmProjects/efficientdet-pytorch-2.0/img/subway_frame/"+frame2+".jpg")
#     img1= cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#     img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#     diff=different_calculate(img1,img2)
#     frame_diff[index+1]=diff
#     print(frame1,frame2,diff)
#     print("#---------------------------------------------#")
# torch.save(frame_diff,"/home/zhiqiang/project/frame_diff_dict_subway.pkl")

for i in range(0,len(area_new_obj)):
    frame_diff = {}
    print([area_new_obj[i][0],area_new_obj[i][2],area_new_obj[i][1],area_new_obj[i][3]])
    for index in range(1, 600):
        frame1 = str(index)
        frame2 = str(index + 1)
        img1 = cv2.imread(r"/home/zhiqiang/PycharmProjects/efficientdet-pytorch-2.0/img/subway_frame/" + frame1 + ".jpg")
        img2 = cv2.imread(r"/home/zhiqiang/PycharmProjects/efficientdet-pytorch-2.0/img/subway_frame/" + frame2 + ".jpg")
        img1 = img1[area_new_obj[i][0]:area_new_obj[i][2], area_new_obj[i][1]:area_new_obj[i][3]]
        img2 = img2[area_new_obj[i][0]:area_new_obj[i][2], area_new_obj[i][1]:area_new_obj[i][3]]
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        diff = different_calculate(img1, img2)
        frame_diff[index + 1] = diff
        #print(frame1, frame2, diff)
    print("#----------compute_end------------#",i)
    sign=str(i)
    torch.save(frame_diff, "/home/zhiqiang/project/frame_diff_dict_subway"+sign+".pkl")


# 找到没有目标的基准帧，与基准帧作对比。

for i in range(0,len(area_new_obj)):
    frame_diff = {}
    print([area_new_obj[i][0],area_new_obj[i][2],area_new_obj[i][1],area_new_obj[i][3]])
    if i ==2:
        for index in range(1, 600):
            frame1 = str(index)
            frame2 = str(index + 1)
            img1 = cv2.imread(r"/home/zhiqiang/PycharmProjects/efficientdet-pytorch-2.0/img/subway_frame/332.jpg")
            img2 = cv2.imread(r"/home/zhiqiang/PycharmProjects/efficientdet-pytorch-2.0/img/subway_frame/" + frame2 + ".jpg")
            img1 = img1[area_new_obj[i][0]:area_new_obj[i][2], area_new_obj[i][1]:area_new_obj[i][3]]
            img2 = img2[area_new_obj[i][0]:area_new_obj[i][2], area_new_obj[i][1]:area_new_obj[i][3]]
            img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            diff = different_calculate(img1, img2)
            frame_diff[index + 1] = diff
            # print(frame1, frame2, diff)
    else:
        for index in range(1, 600):
            frame1 = str(index)
            frame2 = str(index + 1)
            img1 = cv2.imread(r"/home/zhiqiang/PycharmProjects/efficientdet-pytorch-2.0/img/subway_frame/1.jpg")
            img2 = cv2.imread(r"/home/zhiqiang/PycharmProjects/efficientdet-pytorch-2.0/img/subway_frame/" + frame2 + ".jpg")
            img1 = img1[area_new_obj[i][0]:area_new_obj[i][2], area_new_obj[i][1]:area_new_obj[i][3]]
            img2 = img2[area_new_obj[i][0]:area_new_obj[i][2], area_new_obj[i][1]:area_new_obj[i][3]]
            img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            diff = different_calculate(img1, img2)
            frame_diff[index + 1] = diff
            # print(frame1, frame2, diff)



    print("#----------compute_end------------#",i)
    sign=str(i)
    torch.save(frame_diff, "/home/zhiqiang/project/frame_diff_dict_subway_based"+sign+".pkl")
