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




----------
2015年12月15日

因为直接使用contours方法提取的边框非常粗糙，而且会带来很多噪声。
因此想到了下述方法：

1. 载入图片
2. 高斯降噪
3. 二值化
3. 灰度处理
4. Canny边缘提取
5. 将提取的到边缘提取轮廊。

注意几点，

1. cv2.imread("XXX.jpg") #<type 'numpy.ndarray'>
2. cv2.findContours的contours是<type 'list'>
3. `cv2.findContours(image, mode, method[, contours[, hierarchy[, offset ]]])`

    第一个参数是寻找轮廓的图像；

    第二个参数表示轮廓的检索模式，有四种（本文介绍的都是新的cv2接口）：
        cv2.RETR_EXTERNAL表示只检测外轮廓
        cv2.RETR_LIST检测的轮廓不建立等级关系
        cv2.RETR_CCOMP建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
        cv2.RETR_TREE建立一个等级树结构的轮廓。

    第三个参数method为轮廓的近似办法
        cv2.CHAIN_APPROX_NONE存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1
        cv2.CHAIN_APPROX_SIMPLE压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
        cv2.CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS使用teh-Chinl chain 近似算法
    返回值
    cv2.findContours()函数返回两个值，一个是轮廓本身，还有一个是每条轮廓对应的属性。
	
	此处选择`cv2.RETR_EXTERNAL`直接从canny边缘线提取，简单粗暴

3. cv2.Canny(img, position, position * 3)，position用于设置图片边缘阈值，默认值25.后期建议做成调节杆，方便用户前端直接控制效果并输出。
4. 通过url载入图片文件,`urllib2.urlopen(url).read()`解析后为str类型，需要重建为cv能够识别的矩阵类型。在对重建矩阵解码为图片格式：iplimage。Canny的输出结果也是iplimage格式。但是cvfindcontour载入源图需要类型为numpy.ndarry，因此数据需要转换，方法如下：

	下表列出了在这三种对象之间转换的方法：
	在数组、iplimage以及cvmat之间转换

| 类型转换 | 方法 |
|--------|--------|
|    array→cvmat   |    cv.fromarray(array)     |
| cvmat→array |	np.asarray(cvmat) |
| cvmat→iplimage | cv.GetImage(cvmat) |
| iplimage→cvmat	|iplimage[:]，或cv.GetMat(iplimage) |

如果需要在array和iplimage之间转换，可以通过cvmat作为桥梁，本代码中使用`edge_im_array = np.asarray(edge_im[:])`

finish 2015年12月16日




******

参考：

[http://stackoverflow.com/questions/18074680/extract-single-line-contours-from-canny-edges](http://stackoverflow.com/questions/18074680/extract-single-line-contours-from-canny-edges)

[OpenCV converting Canny edges to contours](http://www.helpsforcoder.com/code/15751940-opencv-converting-canny-edges-to-contours.html)

[Reading and Writing Images and Video](http://i12.tietuku.com/3eccda985794c42b.jpg)

[python图片数组格式转化](http://blog.csdn.net/xueweuchen/article/details/38756075 "python图片数组格式转化")

效果图链接：

[http://i4.tietuku.com/6c2f77ca748e17f1.jpg](http://i4.tietuku.com/6c2f77ca748e17f1.jpg)
![](http://i12.tietuku.com/9d6280b185ba688b.jpg)

