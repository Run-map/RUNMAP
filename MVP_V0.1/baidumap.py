#-*- coding:utf-8 -*-
import urllib2,urllib,httplib
import json


class xBaiduMap:
    def __init__(self,key='your_key'):
        self.host='http://api.map.baidu.com'
        self.path='/geocoder?'
        self.param={'address':None,'output':'json','key':key,'location':None,'city':None}
      
    def getLocation(self,address,city=None):
        rlt=self.geocoding('address',address,city)
        if rlt!=None:
            l=rlt['result']
            if isinstance(l,list):
                return None
            return l['location']['lat'],l['location']['lng']
        
    def getAddress(self,lat,lng):
        rlt=self.geocoding('location',"{0},{1}".format(lat,lng))
        if rlt!=None:
            l=rlt['result']
            return l['formatted_address']
            #Here you can get more details about the location with 'addressComponent' key
            #ld=rlt['result']['addressComponent']
            #print(ld['city']+';'+ld['street'])
            #
    def geocoding(self,key,value,city=None):
        if key=='location':
            if 'city' in self.param:
                del self.param['city']
            if 'address' in self.param:
                del self.param['address']
            
        elif key=='address':
            if 'location' in self.param:
                del self.param['location']
            if city==None and 'city' in self.param:
                del self.param['city']
            else:
                self.param['city']=city
        self.param[key]=value
        r=urllib.urlopen(self.host+self.path+urllib.urlencode(self.param))
        rlt=json.loads(r.read())
        if rlt['status']=='OK':
            return rlt
        else:
            print "Decoding Failed"
            return None
