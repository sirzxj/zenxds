# windows

## setuptools
	python ez_setup.py to install easy_install

## pip
	install setuptools
	add Python27/Scripts to the path
	get the pip source
	python setup.py install
	
## django
	pip install django
	or
	python setup.py install

## mysql-python
	pip install mysql-python
	or 
	get the exe

## PIL
	get the exe

## django连wamp mysql问题
	神经非要在windows下开发，再装一个mysql
	把mysql的bin加到path里
	关掉wamp

	# 不执行上面直接下面开启mysql服务的不起作用，wamp你干了啥
	mysqld --install
	net start mysql

## ant
	下载ant
	ANT_HOME：c:/ant
	JAVA_HOME=c:\jdk-1.5.0.05
	PATH ;%ANT_HOME%\bin