## RWF2000 - A Large Scale Video Database for Violence Detection



### Introduction

With the increasing of surveillance cameras in modern cities, huge amount of videos can be collected. While there are insufficient human resource for  monitoring all the screens at  one time. 

We are considering how to use techniques of video understanding to detect violent behavior so that it can give a quick alarm in time.



### Dataset

- Collected raw surveillance videos from YouTube, sliced them into clips within 5s at 30 fps, and labeled each clip as Violent or Non-Violent Behavior。

- Dropped duplicated contents which appear in both training set and validation set.

- Finally we got 2000 clips and 300,000 frames as a new data set for real-world violent behavior detection under surveillance camera.

  <img src="https://github.com/mchengny/RWF2000-Video-Database-for-Violence-Detection/raw/master/Images/demo1.gif" width="400px" height="250px">



### Problems

Since all the videos are captured by surveillance cameras in public places, many of them may not have a good imaging quality due to dark environment, fast movement of object, lighting blur, etc. Here are some examples:

- Only part of the person appears in the picture

  <img src="https://github.com/mchengny/RWF2000-Video-Database-for-Violence-Detection/raw/master/Images/blocked.gif" width="400px" height="250px">

- Crowds and chaos

  <img src="https://github.com/mchengny/RWF2000-Video-Database-for-Violence-Detection/raw/master/Images/crowded.gif" width="400px" height="250px">

- Small object at far distance

  <img src="https://github.com/mchengny/RWF2000-Video-Database-for-Violence-Detection/raw/master/Images/far_distance.gif" width="400px" height="250px">

- Low resolution

  <img src="https://github.com/mchengny/RWF2000-Video-Database-for-Violence-Detection/raw/master/Images/low_resolution.gif" width="400px" height="250px">

- Transient action

  <img src="https://github.com/mchengny/RWF2000-Video-Database-for-Violence-Detection/raw/master/Images/transient.gif" width="400px" height="250px">



### Download

To download the released dataset, please:

1. download the *Agreement Sheet.pdf* and sign it. 
2. Send the PDF version of scanned *Agreement Sheet* with signature to ming.cheng@dukekunshan.edu.cn
3. We will return an e-mail with download link to you as soon as possible.

 

Kindly remind: using the proposed dataset, please cite:

Ming Cheng, Kunjing Cai, and Ming Li. "RWF-2000: An Open Large Scale Video Database for Violence Detection." arXiv preprint arXiv:1911.05913 (2019).



### Note

Since the dataset contains 2,000 video clips extracted from about 1,000 unique videos, we have manually checked the train set, validation set and test set to avoid the data leakage between three parts. We suggest you to keep the original partition, and do not re-shuffle the entire dataset.

















