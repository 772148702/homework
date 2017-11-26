# -*- coding: utf-8 -*-
import pipe
import random
import bird
def choose(choice):   #随机选择难度
    if choice==1:
        set_easy()
    if choice==2:
        set_middle()
    if choice==3:
        set_difficult()
def set_easy():
    pipe.pipeDistance=150  #设置管道的间距
    pipe.pipeCount = 4   #管道的种类
    bird.upSpeed = 200  #小鸟上升的速度，值越大越难
def set_middle():
    pipe.pipeDistance = 100 #设置管道的间距
    pipe.pipeCount = 4    #管道的种类
    pipeInterval = 90     #管道的间隔
    bird.upSpeed = 200    #小鸟上升的速度，值越大越难
def set_difficult():
    pipe.pipeDistance = 100
    pipe.pipeCount = 4
    pipeInterval = 90
    bird.upSpeed = 250   #小鸟速度加大了，难度增加了