# -*- coding: utf-8 -*-
# 2015年12月15日 OpenCV converting Canny edges to contours
# runmap  by shawn0lee0
# Ref:http://stackoverflow.com/questions/18074680/extract-single-line-contours-from-canny-edges


import cv2
import sys,codecs
import json #保证与javascript数据格式统一
import cv2.cv as cv
import numpy as np

position = 25

#def main():
img = cv2.imread('D:\\python\\RUNMAP\\MVP_V0.3_CannyEdge_to_contours\\COVER.jpg', 0)
img = cv2.GaussianBlur(img,(3,3),0)
if img is None:
    raise Exception("Error while loading the image")

canny_img = cv2.Canny(img, position, position * 3)

contours, hierarchy = cv2.findContours(canny_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
str_len_contours = str(len(contours)) #取轮廊数量
print "contours num:%s" %str_len_contours
contours_list = contours[-1].tolist()
print contours_list
print contours_list[0][0]


scale = 1 #不缩放
contours_img = cv2.resize(contours_img, (0, 0), fx=scale, fy=scale)

for cnt in contours:
    color = np.random.randint(0, 255, (3)).tolist()
    cv2.drawContours(contours_img,[cnt*scale], 0, color, 1)

#cv2.imwrite("COVER.jpg", canny_img)
#cv2.imwrite("fx_canny_contours.jpg", contours_img)
cv2.imshow("canny_img", canny_img)
cv2.imshow("contours_img", contours_img)

img_pix = str(np.size(img))
gray_pix = str(np.size(contours_img))
canny_img_pix = str(np.size(canny_img))
#轮廊清单转文本输出
s = open("Contours.txt",'a')
s.write("Img Gausss  pix nums:" +"%s" %img_pix + "\n") 
s.write("Gray pix nums:" +"%s" %gray_pix + "\n")
s.write("canny_img_pix  nums:" +"%s" %canny_img_pix + "\n")
s.write("contours num:" +"%s" %str_len_contours + "\n") 
for ele in contours:
 s.write("%s\n" % ele)
s.write("**"*50  + "\n")
s.close()

l = open("contours_list.txt",'a')
l.write("Img Gausss  pix nums:" +"%s" %img_pix + "\n") 
l.write("Gray pix nums:" +"%s" %gray_pix + "\n")
l.write("canny_img_pix  nums:" +"%s" %canny_img_pix + "\n")
l.write("contours num:" +"%s" %str_len_contours + "\n") 
l.write("contours_list"  + "\n")
for ele in contours_list:
 l.write("%s\n" % ele)
l.write("**"*50  + "\n")
l.close()


cv2.waitKey(0)
    