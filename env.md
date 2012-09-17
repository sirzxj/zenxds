#更新软件源--使用163的源

#git
    apt-get install git

#设置用户名邮箱
    cd .ssh 
    ssh-keygen

#mysql
    apt-get install mysql-server
    mysql 5.5 编码改为utf-8：
    * 修改my.cnf
    * [client]
    * default-character-set = utf8
    * [mysqld]
    * character-set-server = utf8
    启动sudo /etc/init.d/mysql start

#pip
安装python模块
    apt-get install python-pip
    pip install gdata 
    再安装douban的python包

#python-dev
    apt-get install python-dev

#django
官方下载
    cd Django-1.3.3/
    python setup.py install

关闭django占用的端口
    ps aux | grep -i manage
    and then kill the pid
    kill -9 pid
    the pid is what you found


#celey redis 
    pip install -U celery-with-redis


#nginx
    apt-get install nginx

* /etc/nginx/conf.d/目录放置自己的配置文件
* sudo /etc/init.d/nginx restart 重启nginx

#flup
使用python写的web服务器软件，它可以接受nginx发来的请求，执行相应的python代码，将结果返回给nginx。
    sudo apt-get install python-flup

#文件系统
    apt-get install smbfs
    sudo mount -t smbfs //192.168.1.10/share ~/share

#sublime text 2
字体设置为文泉驿等宽微米黑

* yui-compressor
* bootstarp

#nodejs





#常用软件

#proxy switchysharp
* chrome插件，翻墙
* 网页截图


# FTP
FileZila

# ChmSee
chm文件查看，乱码时修改编码即可

# xmind
思维导图

# ReText
markdown编辑器
