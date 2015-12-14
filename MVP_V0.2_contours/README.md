# 图片边框提取

效果图链接：[http://i4.tietuku.com/2d5ced664cf008c1.jpg](http://i4.tietuku.com/2d5ced664cf008c1.jpg)
![](http://i4.tietuku.com/2d5ced664cf008c1.jpg)

函数使用简化算法，只提取图形轮廊的终点坐标，节省存储空间


    print (type(contours)) #查询所有轮廊数据类型

    print (type(contours[0])) #查询图形中第一个轮廊数据类型

    print (len(contours)) #查询图形中所有轮廊的数量


本案例返回值：

    <type 'list'>

    <type 'numpy.ndarray'>

    1


接下来:将提取到图形轮廊坐标重定义为javascript api 中的location等

海盗教练建议：与javascript的数据接口统一使用json格式

[https://docs.python.org/2/library/json.html](https://docs.python.org/2/library/json.html)

因为contours[0]的数据类型为，`<type 'numpy.ndarray'>`

利用ndarray.tolist()可以将numpy的数组转为python的list
效果如下：
`[[[10, 18]], [[10, 249]], [[251, 249]], [[251, 18]]]`