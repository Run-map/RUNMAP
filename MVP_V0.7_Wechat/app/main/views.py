# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import request, render_template, session, redirect, url_for, current_app, make_response
import json
import logging
from ..logger import handler
from . import main
import hashlib  
import xml.etree.ElementTree as ET
import cv2
import sys,codecs
import json
import cv2.cv as cv
import numpy as np
import urllib2
import time
import os


logger = logging.getLogger(__file__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


@main.route('/runmap/<user>', methods=['GET', 'POST'])
def index(user):
    #return render_template('index.html', api_key=current_app.config['API_KEY'])
    return render_template('index.html', points_js=url_for('static', filename='js/{0}.js'.format(user))) 
 
@main.route('/', methods = ['GET', 'POST'] )  
def wechat():  
    if request.method == 'GET':
        token = 'runmap'
        query = request.args
        signature = query.get('signature', '')
        timestamp = query.get('timestamp', '')
        nonce = query.get('nonce', '')
        echostr = query.get('echostr', '')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s)
        if ( hashlib.sha1(s).hexdigest() == signature ):
            return make_response(echostr)
    else:
        rec = request.stream.read()
        xml_rec = ET.fromstring(rec)
        msgtype = xml_rec.find('MsgType').text
        fromu = xml_rec.find('FromUserName').text
        tou = xml_rec.find('ToUserName').text
        if msgtype == 'image':
            picurl = xml_rec.find('PicUrl').text
            points_js = "app/static/js/{0}.js".format(fromu)
            os.remove(points_js)
            with open(points_js, "w") as f:
                prefix = 'var data = {"data":['
                data_points = ""
                points = url_jpg_contours(picurl)
                data_points = ",".join(["[{0},{1},1]".format(point[0], point[1]) for point in points])
                suffix = '],"total":{0},"rt_loc_cnt":47764510,"errorno":0,"NearestTime":"{1}","userTime":"{1}"}}'.format(len(points), time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                f.write(prefix+data_points+suffix)
            xml_rep_text = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>"
            response = make_response(xml_rep_text % (fromu,tou,str(int(time.time())),"http://13.75.40.237/runmap/{0}".format(fromu)))
            response.content_type='application/xml'
            return response
        return make_response('')

#@main.route('/yingyan', methods=['GET', 'POST'])
#def yingyan():
#    return render_template('yingyan.html')

def url_jpg_contours(url):
    position = 100
    filedata = urllib2.urlopen(url).read()
    imagefiledata = cv.CreateMatHeader(1, len(filedata), cv.CV_8UC1)
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
    edge_im_array = np.asarray(edge_im[:])
    
    ret, edge_im_array = cv2.threshold(edge_im_array,127,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(edge_im_array, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    scale = 10000.0
    points = []
    for contour in contours:
        for i in contour:
            for j in i:
                lng_offset = j[0] / scale
                lat_offset = j[1] / scale
                points.append([lng_offset, lat_offset])
    return points
