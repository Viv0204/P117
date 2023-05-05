import os
import cv2
path = "Images"
Images = []

for fileName in os.listdir(path):
    name, ext = os.path.splitext(fileName)
    if ext in [".gif", ".png", ".jpg", ".jpeg", ".jfif"]:
        file_name = path + "/" + fileName
    print(file_name)
    Images.append(file_name)
count = len(Images)
print(count)
frame = cv2.imread(Images[0])
height, width, Channels = frame.shape
size = (width, height)
print(size)

out = cv2.VideoWriter('friends.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for i in range(0, count-1):
    frame = cv2.imread(Images[i])
    out.write(frame)
print("Done")