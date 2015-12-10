from baidumap import xBaiduMap
bm=xBaiduMap()
print bm.getLocation("红旗大街淮河路",'哈尔滨')
print bm.getLocation("人民路沙浦路")
print bm.getLocation("浙江大学紫金港",'杭州')
print bm.getAddress(30.275836, 120.13107)        

