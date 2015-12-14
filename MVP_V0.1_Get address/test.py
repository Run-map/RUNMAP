#-*- coding:utf-8 -*-
from baidumap import xBaiduMap
bm=xBaiduMap()
print bm.getLocation("天安门",'北京')
print bm.getLocation("浙江大学玉泉校区")
print bm.getLocation("浙江大学玉泉校区",'杭州')
print bm.getAddress(39.912684,116.404049)



