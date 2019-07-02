# Python一些小Demo(学习用）
- AsciiPicture
    - 描述: 将图片变成字符画
    - 方式: 使用PIL库处理传入的图片 输出在屏幕上 然后写入文件

- BookDemo
	- 描述: Python核心编程一些代码
	- AboutNetwork
		- 描述: 关于网络编程的相关代码

- ChickenAndRabbit
	- 描述: 用代码求解鸡兔同笼
	- 方式: 小学学的

- ComputePI
	- 描述: 计算圆周率PI(π)
	- 方式: 泰勒级数求圆周率的近似值

- GetBingPictures
    - 描述: 获取必应搜索引擎上的今日美图
    - 方式: 分析网页得到接口 然后得出图片链接, 用urllib保存下来

- Ip 
    - 描述: 查询IP地址所对应的地址
    - 方式: 通过http://www.ip138.com/ips138.asp?ip={'ip'} 这样的接口 生成展示ip地址的网页
     并通过requests、BeautifulSoup制作简易的爬虫 将ip地址信息爬取并展示出来

- PeppaPig (PS.粉红猪小妹, 就是小猪佩奇哈哈哈哈)
    - 方式: 绘出近期大火的小猪佩奇
    - 描述: 通过turtle库 画出小猪佩奇

- PythonGame
	- 描述: 小游戏
		- Confession
			- 描述: 生成一个表白窗口(咋也关不掉) 需要同意表白才可以关掉
			- 方式: Pygame模块
		- CatchBall
			- 描述: 接球小游戏
			- 方式: Pygame模块
		- GuessFist
			- 描述: 猜拳小游戏
			- 方式: 命令行输入
			
- QueryFastMail
    - 描述: 命令行查询快递
    - 方式: 通过requests、json库解析相应接口输出到命令行
    
- SinaNewsOfChina
    - 描述: 爬取新浪国内新闻网的新闻以及用户评论并写入文件
    - 方式: 通过requests、BeautifulSoup爬取新浪新闻网主页采集新闻链接 再爬取单个新闻获取
    内容、用户评论等 最后写入文件

- TextProBar                                                           
	- 描述: 文本进度条
	- 方式: 通过print控制输出实现文本进度条

- TheBestUniversity
	- 描述: 展示中国大学排名                                           
	- 方式: 通过requests、BeautifulSoup、re制作简易爬虫 爬取最好大学网的>    信息 并用PrettyTable将其漂亮地输出在屏幕上

- Ticket
    - 用途: 查询国内火车票信息
    - 做法: 通过requests、BeautifulSoup、re制作简易爬虫 爬取12306网站的信息 并用PrettyTable
    将其漂亮地输出在屏幕上
    
- Top500
	- 描述: 获取世界五百强信息 并可视化展示
	- 方式: 未做完 留空

