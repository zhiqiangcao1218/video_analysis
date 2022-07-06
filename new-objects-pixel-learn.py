import torch
frame_dete_4000=torch.load("/home/zhiqiang/project/frame_box_subway_dete_ten_minute_4000.pkl")
frame_dete_8000=torch.load("/home/zhiqiang/project/frame_box_subway_dete_ten_minute_4001_8000.pkl")
frame_dete_24600=torch.load("/home/zhiqiang/project/frame_box_subway_dete_ten_minute_8001_24600.pkl")
new_obj_4000=[]
for i in range(1,(len(frame_dete_4000)-1)):
    if len(frame_dete_4000[i+1])>len(frame_dete_4000[i]):
        print(i+1)
        new_obj_4000.append(i+1)
print(len(new_obj_4000))
torch.save(new_obj_4000,"/home/zhiqiang/project/new_object_subway_4000.pkl")
