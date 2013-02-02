## install
	test requirements: http://hostname/path/to/yii/requirements/index.php
	
## create Yii webapp
	./yiic webapp 要创建的目录

## create Controller
	Controller ID: r=Controller ID 
	Action IDs: render ->Action IDs r=Controller ID/action ID

## connect to database
*	 SQLite: sqlite:/path/to/dbfile
*	 MySQL: mysql:host=localhost;dbname=testdb
*	 PostgreSQL: pgsql:host=localhost;port=5432;dbname=testdb
*	 SQL Server: mssql:host=localhost;dbname=testdb
*	 Oracle: oci:dbname=//localhost:1521/testdb

## shell
	./protected/yiic shell(必须在webapp主目录使用该命令)
	test db connect: echo Yii::app()->db->connectionString;

## test
under the directory protected/tests/
	XxxTest.php(a class extends CTestCase
) > xxxTest(a method)
	phpunit unit/xxx.php

## install PHPUnit
[PHPUnit](https://github.com/sebastianbergmann/phpunit/)

	apt-get install php5-curl,php-pear
	pear install phpunit/phpunit_selenium

## install selenium

## database migration
	yiic migrate create <name>





