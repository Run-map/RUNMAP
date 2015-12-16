#! /usr/bin/env python
# coding=utf-8
# author: shawn0lee0
# email: run-map@googlegroups.com
# version: 1.0

print "OpenCV Python version of edge"

import sys
import urllib2
import cv2.cv as cv
import cv2

# some definitions
win_name = "Edge"
trackbar_name = "Threshold"

# the callback on the trackbar
def on_trackbar(position):

    cv.Smooth(gray, edge, cv.CV_BLUR, 3, 3, 0)
    cv.Not(gray, edge)

    # run the edge dector on gray scale
    cv.Canny(gray, edge, position, position * 3, 3)

    print "Type_edge:%s"%type(edge) 
    # reset
    cv.SetZero(col_edge)
  
    # copy edge points
    cv.Copy(im, col_edge, edge)
    


    # show the im
    cv.ShowImage(win_name, edge)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        im = cv.LoadImage( sys.argv[1], cv.CV_LOAD_IMAGE_COLOR)
    else:
        url = 'http://i12.tietuku.com/05ef0b29030fa46c.jpg'
        filedata = urllib2.urlopen(url).read()
        imagefiledata = cv.CreateMatHeader(1, len(filedata), cv.CV_8UC1) #创建并初始化矩阵头文件

        print "Type_imagefiledata:%s"%type(imagefiledata) 
        cv.SetData(imagefiledata, filedata, len(filedata)) #将图片数据加入矩阵头文件中
        im = cv.DecodeImage(imagefiledata, cv.CV_LOAD_IMAGE_COLOR)
        print "Type_SetData_filedata:%s"%type(filedata) 
    # create the output im
    col_edge = cv.CreateImage((im.width, im.height), 8, 3)

    # convert to grayscale
    gray = cv.CreateImage((im.width, im.height), 8, 1)
    edge = cv.CreateImage((im.width, im.height), 8, 1)
    cv.CvtColor(im, gray, cv.CV_BGR2GRAY) #将im灰度处理并存贮在gray的内存容器中

    # create the window
    cv.NamedWindow(win_name, cv.CV_WINDOW_AUTOSIZE)

    # create the trackbar
    cv.CreateTrackbar(trackbar_name, win_name, 1, 100, on_trackbar)

    # show the im
    on_trackbar(100)

    # wait a key pressed to end
    print "filedata:%s"%type(filedata)
    print "imagefiledata:%s"%type(imagefiledata)
    
    print "im_cv.DecodeImage:%s"%type(im)
    print "col_edge_cv.CreateImage:%s"%type(col_edge)
    print "gray_CreateImage:%s"%type(gray)
    print "After canny edge type:%s"%type(edge)
    '''
    OpenCV Python version of edge
    Type_imagefiledata:<type 'cv2.cv.cvmat'>
    Type_SetData_filedata:<type 'str'>
    Type_edge:<type 'cv2.cv.iplimage'>
    filedata:<type 'str'>
    imagefiledata:<type 'cv2.cv.cvmat'>
    im_cv.DecodeImage:<type 'cv2.cv.iplimage'>
    col_edge_cv.CreateImage:<type 'cv2.cv.iplimage
    gray_CreateImage:<type 'cv2.cv.iplimage'>
    After canny edge type:<type 'cv2.cv.iplimage'>
    '''
    cv.WaitKey(10000) #延迟ms,0表示一直
    #cv2.destroyAllWindows()