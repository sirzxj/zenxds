# install
	pip install Scrapy

# 创建项目
	scrapy startproject 项目名

## 目录组织
	项目名/
	    scrapy.cfg	项目配置文件
	    项目名/
	        __init__.py
	        items.py		# items 文件, item是你抓取的数据存放的容器
	        pipelines.py	# 管道文件, 定义如何对抓取到的内容进行再处理
	        settings.py		# 项目配置文件
	        spiders/		# 你蜘蛛的存放位置
	            __init__.py
	            蜘蛛文件		# 抓取逻辑
	            ...

# 开始抓取
	scrapy crawl 蜘蛛名
	scrapy crawl 蜘蛛名 -o items.json -t json
	scrapy crawl myspider -a category=electronics	#  传递参数category到蜘蛛的__init__方法里

# shelll
	scrapy shell 目标url

# response对象
	'body', 
	'body_as_unicode()',
	'copy()', 
	'encoding', 
	'flags',		# [] 
	'headers', 	
	'meta', 
	'replace()',	 
	'request', 		# obj
	'status', 		
	'url'		

# Project-only commands:
	
# Global commands:
	scrapy startproject <name>	
	scrapy genspider [-t template] <name> <domain>	# 在当前项目创建一个新蜘蛛, template-basic/crawl/csvfeed/xmlfeed

# Link Extractors

