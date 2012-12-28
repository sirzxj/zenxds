* Run Redis with:redis-server /path/to/redis.conf
* Redis client: redis-cli
* pkill redis-server or redis-cli shutdown
* config /etc/redis/redis.conf
* dbfile /var/lib/redis/dump.rdb

性能测试工具：redis-benchmark

select 1 			# 选择数据库


	SET server:name "fido"
	GET server:name => "fido"
	INCR connections => 11		# 增加1
	incrby 10/-10 			# 增加10/-10
	decr
	decrby
	DEL
	SETNX						# set if not exist, if exists, return 0,不覆盖
	SETEX name 10 zenxds 				# 设置过期时间, 10s
	SETRANGE name 2 gmail.com 			# 从index 2位开始替换为gmail.com，返回新字符串长度
	MSET 一次设置多个值 k1 v1 k2 v2
	mget
	msetnx 同上
	getset 			# 设置新值,返回旧值
	append
	strlen			# str length

	hset hashname hashitem hashvalue
	hget 