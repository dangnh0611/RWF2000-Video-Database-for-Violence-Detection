# -*- coding: utf-8 -*-
"""
Created on Sat May 18 19:47:16 2019

@author: CHENG Ming
"""

import pandas as pd
from pytube import YouTube
import threading
from my_utils import download
import os
import math

# In[] 
# 设置csv文件路径
file_path = "haha.csv"
# 设置启动最大线程数
thread_num = 4
# 设置下载范围：video_list[start_num,end_num]
start_num = 0
end_num   = 605
# 设置下载路径
save_dir = r'E:\A - data'

# In[]
duplicated_list = os.listdir(save_dir)
duplicated_list = [x.split('.')[0] for x in duplicated_list]
# In[]
# 加载csv文件到DataFrame
df = pd.read_csv(file_path)
# 获得去重后的视频id列表，并打印
video_list = df['VideoID'].drop_duplicates()
video_list = video_list.reset_index(drop=True)
print("Total number of videos: ", len(video_list), '\n')
# In[]
# 将目标任务总量划分为n个子任务区间，分别用多个线程处理
intervals = []
width = math.ceil((end_num-start_num) / thread_num)
for i in range(thread_num):
    if start_num+(i+1)*width<=end_num:
        interval = video_list[start_num+i*width : start_num+(i+1)*width]
        intervals.append(interval)
    else:
        interval = video_list[start_num+i*width : end_num]
        intervals.append(interval)
    
# 定义列表thread_pool，循环加载线程
thread_pool = []
for i in range(thread_num):
    t = threading.Thread(target=download, args=(intervals[i],save_dir,i,duplicated_list))
    thread_pool.append(t)
    
# 依次启动下载任务
for t in thread_pool:
    t.start()
    
# 依次join
for t in thread_pool:
    t.join()
    



 
