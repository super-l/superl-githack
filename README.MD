# 程序简介
##### .git信息泄露漏洞利用工具，程序主要运用于WEB安全脆弱性测试~~ 与李姐姐的GitHack有所不同。

# 当前版本
##### Version 1.0
  
# 特点说明
#####  1：可自动完整的下载整个项目GIT工程文件；
#####  2：可获得从git项目创建以来的所有更新历程和源代码；
#####  3：下载的代码完整(在使用李姐姐的GitHack时候，发现提示很多文件找不到)
#####  4：同时支持python2和python3运行；

# 使用方法
##### 判断网站是否存在.git泄露漏洞；
##### 修改102行代码base_url = "http://www.superl.org/.git/" 中的地址；
##### 运行：python superl-githack.py
##### 之后会在工具的当前目录下生成git目录，里面存放该网站的git文件，如图：
![image](https://github.com/super-l/superl-githack/blob/master/test1.png)
![image](https://github.com/super-l/superl-githack/blob/master/test2.png)
##### 随便使用一款带git版本控制的IDE，如phpstrom,intellij IDEA,Clion,Pycharm等，创建一个空的项目，如图：
![image](https://github.com/super-l/superl-githack/blob/master/test3.png)
##### 在当前空工程路径下使用git init命令初始化git功能（会自动创建一个.git目录;
##### 删除空工程的.git目录下的所有文件，把我们下载到的git目录中的文件，全部复制粘贴过去；
##### 重新打开IDE，就会自动加载新的git开发版本记录，如图；
![image](https://github.com/super-l/superl-githack/blob/master/test4.png)



# 使用效果
##### 测试环境系统为Mac Pro 10.12
##### 测试环境python版本为2.7
##### 如果提示模块不存在，请自行pip安装！
##### 如果使用遇到问题，可以留言。