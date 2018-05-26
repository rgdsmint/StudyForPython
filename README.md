# python- python一些基础型小Demo
- 1.AsciiPicture
    - 用途: 将图片变成字符画
    - 做法: 使用PIL库处理传入的图片 输出在屏幕上 然后写入文件

- 2.GuessNumber
    - 用途: 简易的猜数字游戏 
    - 做法: 采用random生成随机数 让用户去猜
- 3.Ip 
    - 用途: 画出小猪佩奇
    - 做法: 通过http://www.ip138.com/ips138.asp?ip={'ip'} 这样的接口 生成展示ip地址的网页
     并通过requests、BeautifulSoup制作简易的爬虫 将ip地址信息爬取并展示出来
- 4.PeppaPig (PS.粉红猪小妹, 就是小猪佩奇哈哈哈哈)
    - 用途: 绘出近期大火的小猪佩奇
    - 做法: 通过turtle库 画出小猪佩奇
- 5.sinaNewsOFChina
    - 用途:爬取新浪国内新闻网的新闻以及用户评论并写入文件
    - 做法:通过requests、BeautifulSoup爬取新浪新闻网主页采集新闻链接 再爬取单个新闻获取
    内容、用户评论等 最后写入文件
- 6.Ticket
    - 用途: 查询国内火车票信息
    - 做法: 通过requests、BeautifulSoup、re制作简易爬虫 爬取12306网站的信息 并用PrettyTable
    将其漂亮地输出在屏幕上
- 7.zui_hao_da_xue_pai_ming
    - 用途: 展示中国大学排名
    - 做法: 通过requests、BeautifulSoup、re制作简易爬虫 爬取最好大学网的信息 并用PrettyTable
    将其漂亮地输出在屏幕上