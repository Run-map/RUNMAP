
## 开发
+ Fork: [Github](https://github.com/shawn0lee0/RUNMAP)
+ 发起人所在城市:浙江杭州
+ 发起人的优势：七年电子产品开发经验，十年体育竞技类游戏骨灰玩家
+ 已知的技术难点：
 + LBS技术
 + 前端
     + [WebApp](https://developers.google.com/web/updates/2014/11/Support-for-installable-web-apps-with-webapp-manifest-in-chrome-38-for-Android)
 + 服务器架构
 + 图形生成
  + web前端浏览器内嵌js脚本生成，可调用api接口
  + 后台管理数据可用py实现数据可视化管理；
 + 用户认证
  + 利用现成模块
 + 积分反馈（MVP先不做）
+ 现有的代码基础：入门
+ 问题场景,以及解决思路：见上述分析。
+ 未来发展策划
    + 市场：开源软件+智能硬件接入
    + 潜在用户画像：
        + 小明码了一整天的电脑，想参加运动，但是迟迟迈不开第一步；
        + 小强每天在小区跑步，跑来跑去都是同样的路线；
        + Nike团队在西湖边画上一个10KM的√ ， 三叶草团队暗自忧伤。。。
        + Github成员通过运动轨迹联线。。
        + 小明因经常在小区跑步，系统自动将他周边2km地盘设定为他所有，任意闯入报警提示，并发出战书是否PK?胜利者获得对方地盘10%领地。。。来吧。。攻城掠地
    + 系统压力预测：
     + 开智群内测吧~
     + 
+ 如何加入：
 + [fork](https://github.com/shawn0lee0/RUNMAP)
 + [Gmail](mailto:run-map@googlegroups.com?subject=反馈)
 + [开发群通讯录](http://qun.hk/b/6427c35cd44c)

+ [目前成员：](https://github.com/shawn0lee0/RUNMAP/issues/3)
 + WEB架构+优化：[@Lcking](https://github.com/Lcking)
 + 服务器后台:[@bingosummer](https://github.com/bingosummer),[@shawn0lee0](https://github.com/shawn0lee0/RUNMAP)，[@Lcking](https://github.com/Lcking)
 + 观察、测试：
   + 原型设计分析：[@Acural](https://github.com/Acural)，[@Lcking](https://github.com/Lcking)
   + 用户行为分析：[@wwshen](https://github.com/wwshen)，[植入观察@aJiea](https://github.com/aJiea)
   + 观察员：开发过程中所有相关工作文档整理、api接口梳理、测试笔记，知识管理（能够相关联起来）
   + 测试：全员参与|友情测试@qingquan0083
 + 程序猿鼓励师：[@wwshen](https://github.com/wwshen)，@aJiea，@shawn0lee0
 + 有余力：思考web与ios/android GPS模块调用 
   
 + 欢迎其他团队一起Fork



## 版本规划：
+ 第1周：MVP
 + DAY1：功能精简、搭平台、熟悉API
  + [交互效果V1.0](https://modao.cc/app/wZtUeShfg7Q8DGUeembZ)
  + ![](http://i5.tietuku.com/2de2658477fdfc2bs.png)![](http://i5.tietuku.com/cf4ddc327dab57cds.png)
 + DAY2：[√]MVP_0.1 实现CLI地址、坐标解析，该结构可适用于后期api调用
 + DAY3：--2015年12月9日
   + [ ]交互页面V1.1初稿、说明文档（墨刀、layoutit.com）
   + [ ]web架构MVP
     + []本地运行版本实现：框架：flask
     + []云平台选择:云os/sinasae/七牛 原则：优先考虑国内服务器。
     + []公网版本MVP
       + []通过域名访问
       + []获取ip.gps 通过webapi解析
   + [ ]服务端后台MVP
     + [][数据表属性字段定义完善](http://developer.baidu.com/map/index.php?title=yingyan/api/entity)
     + []上传本地gps信息并解析
     + []可查询历史轨迹
 + DAY4：
   + []页面定稿&文档
   + []Web + html +(js)接口融合
   + []优化、测试
 + DAY5/6：核心功能模块开发、优化
   + []后台轨迹实时监控存储
   + []后台历史轨迹查询
   + []时间戳
   + []多轨迹统计分析（轨迹活跃度|时间）
 
 + DAY7：独立模块内测、迭代
+ 第2周：优化迭代
 + DAY1：
   + 增加覆盖物[（制定跑图图案）](http://developer.baidu.com/map/jsdemo.htm#a1_2)
   + 轨迹完成度匹配分析--进度条
 + DAY2：
   + 优化覆盖物[（制定跑图图案）](http://developer.baidu.com/map/jsdemo.htm#a1_2)
   + [加载pm2.5天气信息](http://developer.baidu.com/map/index.php?title=car/api/weather)
   + [结合历史轨迹数据进度完成情况，酌情生成地理围栏](http://developer.baidu.com/map/index.php?title=yingyan/api/fence)
 + DAY3：优化、测试、迭代
 + DAY4：   
   + []用户认证
 + DAY5：
   + []用户认证
   + []自定义图形导航
 + DAY6：预发布
 + DAY7：迭代
+ 第3周：测试、输出
 + DAY1：单元测试（相关函数穷举测试）
 + DAY2：单元测试（相关函数穷举测试）
 + DAY3：整体测试→更新→分支版本输出|操作文档编辑整理|演示素材收集整理
 + DAY4：分支版本小范围群测|操作文档编辑整理|演示素材收集整理
 + DAY5：群测反馈，修改，更新|操作文档定稿|路演视频初版
 + DAY6：预发布||路演视频定稿
 + DAY7：检查，总结

+ 代码交流：
 + [有道协作群 群号：15172380](http://163.fm/bCEj1yB)
 + Wechat群组：个人号：robo_one申请验证后拉群。
 + [Google run-map Group](mailto:run-map@googlegroups.com?subject=反馈)
+ 代码合并
+ 运行
+ 测试
+ 任务：
 + 认领
 + 分配
 + 指派
 + 追踪
 + 交付
 + 关闭 



技术

+ [百度鹰眼](http://yingyan.baidu.com/)
+ [高德LBS开放平台](http://lbs.amap.com/api/javascript-api/reference/plugin/#m_AMap.Geolocation)
+ [腾讯LBS开放平台](http://lbs.qq.com/)
+ [看板管理](http://www.infoq.com/cn/articles/agile-kanban-boards)
 + [《看板方法》](http://book.douban.com/subject/25788807/) 
+ 版本控制：
 + [Git分支管理策略](http://www.ruanyifeng.com/blog/2012/07/git.html)
 + [Gitflow](https://github.com/nvie/gitflow/)
 + [Managing branches in your repository](https://help.github.com/articles/managing-branches-in-your-repository/)

## 意见反馈

[调查问卷](https://jinshuju.net/f/T85Nps)

## 版权

[本作品采用知识共享许可协议](http://creativecommons.org/licenses/by-nc-sa/3.0)

![](https://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png)

知识共享署名-非商业性使用-相同方式共享 3.0 未本地化版本许可协议


进行许可。