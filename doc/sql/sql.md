# 关键字最好大写，表名列名小写方便调试
## 常用命令
	show databases;
	use database;
	
## show命令
	show columns from 表名;	或者describe 表名;	--显示表列（字段名，数据类型等）
	show status;		--服务器状态信息
	show create table/database 表名;  			--显示创建表/数据库的sql语句
	show grants;
	help show
	
## select
	select id, name from rss_album limit 5;
	select DISTINCT id, name from rss_album limit 5; 		--结果唯一，，不能单独对一个字段使用
	select id, name from rss_album limit 10， 5;				--第十行开始取条
	order by id, name 
	order by id, name DESC
	where a BETWEEN 6 AND 10
	where a is NULL
	IN （100， 200）
	and优先级高于or
	LIKE '%ikea%'  %多个任意字符，_单个任意字符
	group by having
	
	UNION 将多个select结果并起来
	
## INSERT
	insert into xx values ()  
	insert into xx(id, name, ....) values		#明确指定列名
	
## UPDATE 
	UPDATE xx set xx='' where;

## 正则
	select from where id REGEXP '100|200'		默认不区分大小写，REGEXP BINARY
	\\n
	a-z
	.
	[:alpha:]
	*+?{n}{n,}
	
## 函数
	select Concat(RTrim(id), ',', name) from rss_album limit 5;
	Upper,Lower
	where Date(order_date) = '2005-09-01'
	
## 汇总
	selct AVG(DISTINCT price) as xx from xx where id<10 
	
## 外键
	外键是另一张表的主键
	ALTER TABLE rss_image_album ADD CONSTRAINT image_id_refs_id_79679fe3 FOREIGN KEY (image_id) REFERENCES rss_image (id);

	
## 多表查询
	select md5, album_id from rss_image AS r, rss_image_album where r.id=rss_image_album.image_id;	#可以使用别名
	
## 修改表
	ALTER table rss add name char(20) default '';
	ALTER table rss DROP COLUMN char(20) default '';
	RENAME table nameold to namenew
	
## 视图
	create view xx as 复杂的select语句 where
