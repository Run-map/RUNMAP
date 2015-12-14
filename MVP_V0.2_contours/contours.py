# -*- coding: utf-8 -*-
# 2015年12月14日 增加文本查看轮廊list-->txt
# runmap  by shawn0lee0

import cv2
import sys,codecs
import json #保证与javascript数据格式统一
import cv2.cv as cv
import numpy
position = 100

img = cv2.imread('C:\\Users\\robo\\Desktop\\pyjpg\\kaizhi.jpg')
print type(img) #<type 'numpy.ndarray'>
img = cv2.GaussianBlur(img,(3,3),0)
print type(img)
print (numpy.size(img)) #图像像素点-->685452
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print (numpy.size(gray))#灰度图像像素点-->228484
edge = cv.CreateImage((300, 300), 8, 1)
print (numpy.size(edge))
cv.Canny(gray, edge, position, position * 3, 3)
ans = []
for y in range(0, edge.shape[0]):
    for x in range(0, edge.shape[1]):
        if edge[y, x] != 0:
            ans = ans + [[x, y]]
ans = numpy.array(ans)

print(ans.shape)
print(ans[0:10, :])



'''
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv.Canny(gray, edge, position, position * 3, 3) #边缘检测
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,0,255),3)

str_len_contours = str(len(contours)) #取轮廊数量

print "contours num:%s" %str_len_contours


print (type(contours))
print (type(contours[0]))


print contours[0]


contours_list = contours[-1].tolist()
print contours_list
print contours_list[0][0]

for i in contours_list:
 str_len_contours_list = str(len(contours_list[i]))
 print str_len_contours_list + "\n"

#轮廊清单转文本输出
s = open("WXJ_contours.txt",'a')
s.write("contours num:" +"%s" %str_len_contours + "\n") 
s.write("contours num:" +"%s" %str_len_contours + "\n") 
for ele in contours:
 s.write("%s\n" % ele)
s.write("**"*50  + "\n")
s.close()

l = open("contours_list.txt",'a')
l.write("contours_list"  + "\n")
for ele in contours_list:
 l.write("%s\n" % ele)
l.write("**"*50  + "\n")
l.close()

cv2.imshow("img", img)
'''
cv2.waitKey(0)
