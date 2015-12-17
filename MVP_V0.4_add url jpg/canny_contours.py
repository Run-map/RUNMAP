# -*- coding: utf-8 -*-
# 2015年12月15日 OpenCV converting Canny edges to contours
# runmap  by shawn0lee0
# Ref:http://stackoverflow.com/questions/18074680/extract-single-line-contours-from-canny-edges


import cv2
import sys,codecs
import json #保证与javascript数据格式统一
import cv2.cv as cv
import numpy as np
import urllib2

position = 100

def local_jpg_caany_contours():
    img = cv2.imread('D:\\python\\RUNMAP\\MVP_V0.4_add url jpg\\COVER.jpg', 0)
    img = cv2.GaussianBlur(img,(3,3),0)
    if img is None:
        raise Exception("Error while loading the image")

    canny_img = cv2.Canny(img, position, position * 3)

    contours, hierarchy = cv2.findContours(canny_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print type(contours)
    contours_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    str_len_contours = str(len(contours)) #取轮廊数量
    print "contours num:%s" %str_len_contours
    contours_list = contours[-1].tolist()
    #contours_location=np.array(contours_list).reshape(-1,).tolist()
    #contours_location=np.array(contours_list).tolist()
    #print contours_list
    print contours_list


    scale = 1 #不缩放
    contours_img = cv2.resize(contours_img, (0, 0), fx=scale, fy=scale)

    for cnt in contours:
        color = np.random.randint(0, 255, (3)).tolist()
        cv2.drawContours(contours_img,[cnt*scale], 0, color, 1)

    cv2.imwrite('C:\\Users\\Administrator\\Desktop\\cany_contours\\COVER_canny_img.jpg', canny_img)
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
    for ele in contours_list:
     s.write("%s\n" % ele)
    s.write("**"*50  + "\n")
    s.close()

    l = open("contours_list.txt",'a')
    l.write("Img Gausss  pix nums:" +"%s" %img_pix + "\n") 
    l.write("Gray pix nums:" +"%s" %gray_pix + "\n")
    l.write("canny_img_pix  nums:" +"%s" %canny_img_pix + "\n")
    l.write("contours num:" +"%s" %str_len_contours + "\n") 
    l.write("contours_list"  + "\n")
    for ele in contours_location:
     l.write("%s\n" % ele)
    l.write("**"*50  + "\n")
    l.close()

    print type(canny_img)
    cv2.waitKey(100)

def url_jpg_contours():
    url = 'http://i12.tietuku.com/05ef0b29030fa46c.jpg'
    filedata = urllib2.urlopen(url).read()
    imagefiledata = cv.CreateMatHeader(1, len(filedata), cv.CV_8UC1)
    print imagefiledata #<cvmat(type=42424000 8UC1 rows=1 cols=48230 step=48230 )>
    cv.SetData(imagefiledata, filedata, len(filedata))
    im = cv.DecodeImage(imagefiledata, cv.CV_LOAD_IMAGE_COLOR)
    col_edge = cv.CreateImage((im.width, im.height), 8, 3)

    # convert to grayscale
    gray_im = cv.CreateImage((im.width, im.height), 8, 1)
    edge_im = cv.CreateImage((im.width, im.height), 8, 1)
    cv.CvtColor(im, gray_im, cv.CV_BGR2GRAY)
    cv.Canny(gray_im, edge_im, position, position * 3, 3)
    cv.SetZero(col_edge)
    # copy edge points
    cv.Copy(im, col_edge, edge_im)
    #ret, edge_jpg = cv2.imencode('.jpg', edge_im, [int(cv.CV_IMWRITE_JPEG_QUALITY), 80])
    edge_im_array = np.asarray(edge_im[:])
    
    print type(edge_im_array)
    #edge_jpg_gray = cv2.cvtColor(edge_im_array,cv2.COLOR_BGR2GRAY)
    ret, edge_im_array = cv2.threshold(edge_im_array,127,255,cv2.THRESH_BINARY)
    print type(edge_im_array)
    contours, hierarchy = cv2.findContours(edge_im_array, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours_img = cv2.cvtColor(edge_im_array, cv2.COLOR_GRAY2BGR)
    url_str_len_contours = str(len(contours)) #取轮廊数量
    str_len_contours = str(len(contours)) #取轮廊数量
   
    #数据处理
   
    all_contours = contours[-1]  #所有轨迹坐标，数据格式为numpy.ndarry
    all_contours_list = all_contours.tolist()
    print contours
    print contours[-1]          #输出所有轨迹坐标，数据格式为numpy.ndarry
    print contours[0][0].tolist()[0] #输出第一条轨迹起始点坐标[[375 241]]并转化成list格式[[375，241]] |**.tolist()[0] 可以省掉一个中括号输出[375，241]
    print contours[0][0].tolist()[0][0] #输出第一条轨迹起始点坐标的X坐标值。
    print contours[0][0].tolist()[0][1] #输出第一条轨迹起始点坐标的Y坐标值。 
    for cons0 in contours:
     for cons1 in contours[cons0].tolist():
       for cons2 in contours[cons0].tolist()[0]:
         for cons3 in contours[cons0].tolist()[0][]:
    
    
    scale = 1 #不缩放
    contours_img = cv2.resize(contours_img, (0, 0), fx=scale, fy=scale)
    print "Url_jpg_contours_num:%s" %url_str_len_contours
    for cnt in contours:
        color = np.random.randint(0, 255, (3)).tolist()
        cv2.drawContours(contours_img,[cnt*scale], 0, color, 1)
    cv2.imshow("URL_canny_img", edge_im_array)
    cv2.imshow("URL_contours_img", contours_img)
    
    
    #轮廊清单转文本输出
    edge_im_array_pix = str(np.size(edge_im_array))
    contours_img_pix = str(np.size(contours_img))

    ss = open("Contours" + ".log",'w')
    ss.write("edge_im_array_pix nums:" +"%s" %edge_im_array_pix + "\n") 
    ss.write("contours_img_pix nums:" +"%s" %contours_img_pix + "\n") 
    ss.write("_url_contours num:" +"%s" %str_len_contours + "\n") 
    for ele in all_contours_list:
     ss.write("%s\n" % ele)
    ss.write("**"*50  + "\n")
    ss.close()
   
    cv2.waitKey(0)
    #return contours_list
def main():
    #local_jpg_caany_contours()
    url_jpg_contours()
    
        
if __name__ == "__main__":
    main()