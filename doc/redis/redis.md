Run Redis with:redis-server
interact with Redis using the built-in client: redis-cli
性能测试工具：redis-benchmark


	SET server:name "fido"
	GET server:name => "fido"
	INCR connections => 11		# 增加
	DEL
	SETNX						# set if not exist 
