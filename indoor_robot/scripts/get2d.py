#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
import cv2

import numpy as np

#导入消息类型，OccupancyGrid是消息类型
from nav_msgs.msg import OccupancyGrid
import matplotlib.pyplot as plt

class Map(object):
    def __init__(self):
        #rospy订阅map话题，第二个是数据类型，第三个是回调函数
        #将订阅的数据传给回调函数，就是那个mapmsg变量
        #如果有话题来了，就直接调用callback函数
        self.map_sub = rospy.Subscriber("rtabmap/proj_map",OccupancyGrid, self.callback)
        print "get map~"
        #下面输出的是地址，并不是数据
        print self.map_sub

    #回调函数的定义，传了mapmsg
    def callback(self,mapmsg):
        try:
            print "into callback"
            #主要是想拿到data，这里存的是地图的信息
            map = mapmsg.data
            print(mapmsg.info)
            width=mapmsg.info.width
            height=mapmsg.info.height
            #下面是tuple类型
            print type(map)
            #变成可以画图的numpy格式
            map = np.array(map)
            #下面输出的是(368466,)，明显不能画图
            print map.shape
            #需要reshape，将上面的数字在线因数分解，然后算出了两个最大因数
            #于是就大概是这样：
            #map = map.reshape((651,566))
            map = map.reshape((width,height))
            print map
            #可以看到大部分的值是-1，所以需要把值规整一下
            row,col = map.shape
            print row,col
            tem = np.zeros((row,col))
            for i in range(row):
                for j in range(col):
                    if(map[i,j]==-1):
                        tem[i,j]=255
                    else:
                        tem[i,j]=map[i,j]
            print map.shape
            cv2.imshow("map",tem)
            cv2.waitKey(0)
    #      plt.imshtabow(map)
    #      plt.show()
        except Exception,e:
            print e
            rospy.loginfo('convert rgb image error')

    def getImage():
        return self.rgb_image

def main(_):
    rospy.init_node('map',anonymous=True)
    v=Map()
    rospy.spin()

if __name__=='__main__':
  main('_')
