# -*- coding: utf-8 -*-
"""
Created on Sat May 18 19:47:16 2019

@author: CHENG Ming
"""

from pytube import YouTube
from time import time
from tqdm import tqdm

def request_video(url,output_path,file_name, counts):
    """
    Request the targed video 
    Args:
        url: link of video
        output_path: directory for downloaded video
        file_name: file name used for downloaded video
        counts: number of trying for videos which cannot be downloaded
    Return:
        None
    """
    
    # stopping condition for recursion
    if counts >= 0:
        try:
            yt =YouTube(url) # Get video streams
            yt = yt.streams.first() # Pick the stream with highest resolution
            yt.download(output_path=output_path, filename=file_name) # download it
        except:
            # Since sometimes the request will be denied by Youtube, 
            # we try again several times
            request_video(url,output_path,file_name,counts-1)
            
    return None
    

def download(video_list,output_path,thread,duplicated_list):
    """
    Downloading each video in given video list
    Args:
        video_list: Given video lsit for downloading, type{pd.Series}
        output_path: directory for downloading video
        thread: the index of current thread
        duplicated_list: if videoID in this list, do not repeat to download and skip it 
    """
    
    time1 = time()
    # download videos one by one
    for video_name in tqdm(video_list):
        if video_name not in duplicated_list:
            url = "https://www.youtube.com/watch?v=" + video_name
            # Request targeted video for trying at most 5 times
            request_video(url,output_path=output_path,file_name=video_name,counts=5) 
        else:
            continue
    time2 = time()
    
    # Calculate time cost
    minutes = int((time2-time1)/60)
    
    # Print states when thread terminates.
    print("Threading {} done. Time: {} mins".format(thread,minutes))

