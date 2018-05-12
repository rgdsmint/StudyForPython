

# -*- coding: utf-8 -*-

import cv2
import os
file_name = "Character_drawing.txt"        #字符画可以保持到这个文件里面
fideo_name = "a.mp4"                    #这里写视频的名字
show_height = 30                          #可以自己设置合适的大小
show_width = 80

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

char_len = len(ascii_char)
output_list = []

if os.path.exists(file_name):
    print("正在加载字符画……")
    with open('a.mp4','rb') as file:
        text = ""
        for line in file.readlines():
            if line == '\n':
                output_list.append(text)
                text = ""
            else:
                text += str(line)
else:
    vc = cv2.VideoCapture(fideo_name)

    if vc.isOpened():
        rval , frame = vc.read()
    else:
        rval = False

    frame_count = 0
    while rval:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray,(show_width,show_height))
        text = ""
        for pixel_line in gray:
            for pixel in pixel_line:
                text += ascii_char[int(pixel / 256 * char_len )]
            text += "\n"
        output_list .append(text)
        frame_count = frame_count + 1
        if frame_count % 100 == 0:
            print("已处理" + str(frame_count) + "帧")
        rval, frame = vc.read()
    print("处理完毕，正在保持字符画……")
    with open(file_name,'w') as file:
        for frame in output_list:
            file.write(frame + "\n");

for frame in output_list :
    os.system("cls")
    print(frame)
    print()
    print()