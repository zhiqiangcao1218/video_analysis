import torch
import cv2
def compute_iou(rec1, rec2):
    """
    computing IoU
    rec1: (x0, y0, x1, y1)
    rec2: (x0, y0, x1, y1)
    :return: scala value of IoU
    """
    # computing area of each rectangle
    S_rec1 = (rec1[2] - rec1[0]) * (rec1[3] - rec1[1])
    S_rec2 = (rec2[2] - rec2[0]) * (rec2[3] - rec2[1])

    # computing the sum_area
    sum_area = S_rec1 + S_rec2

    # find the each edge of intersect rectangle
    left_line = max(rec1[1], rec2[1])
    right_line = min(rec1[3], rec2[3])
    top_line = max(rec1[0], rec2[0])
    bottom_line = min(rec1[2], rec2[2])
    #print(top_line, left_line, right_line, bottom_line)

    # judge if there is an intersect area
    if left_line >= right_line or top_line >= bottom_line:
        return 0
    else:
        intersect = (right_line - left_line) * (bottom_line - top_line)
        return (intersect / (sum_area - intersect)) * 1.0

frame_dete_4000=torch.load("/home/zhiqiang/project/frame_box_subway_dete_ten_minute_4000.pkl")
list_new_obj_frame=[89,364,937,1231,1275,1596,1666,1792,1909,1926,2222,2523,2529,2567,2837,2936,2995,2996]
box_new_obj=[]
for i in list_new_obj_frame:
    for j in range(0,len(frame_dete_4000[i])):
        num=0
        for k in range(0,len(frame_dete_4000[i-1])):
            iou=compute_iou(frame_dete_4000[i][j],frame_dete_4000[i-1][k])
            if iou<=0.3:
                num = num + 1
        #print(num)
        if num==len(frame_dete_4000[i-1]):
            box_new_obj.append(frame_dete_4000[i][j])
            print(i)
print(len(box_new_obj))
torch.save(box_new_obj,"/home/zhiqiang/project/new_obj_area_subway_4000.pkl")






