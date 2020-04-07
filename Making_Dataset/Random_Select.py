# -*- coding: utf-8 -*-
"""
Created on Fri May 24 23:55:40 2019

@author: CHENG Ming
"""

import os
import random
import shutil 
from tqdm import tqdm


input_path = r'E:\A - 暴力事件检测\Datasets\现有数据集合集\non'
target_path = r'E:\A - 暴力事件检测\Datasets\现有数据集合集\n1'
num = 272




file_list = []
for file in os.listdir(input_path):
    file_path = os.path.join(input_path,file)
    file_list.append(file_path)
    
"""    

file_list = []
for folder in os.listdir(input_path):
    folder_path = os.path.join(input_path, folder)
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path,file)
        file_list.append(file_path)
"""


        
random.shuffle(file_list)

for i in tqdm(range(num)):
    video_name = file_list[i].split('\\')[-1] 
    path = os.path.join(target_path, video_name)
    shutil.move(file_list[i],path)