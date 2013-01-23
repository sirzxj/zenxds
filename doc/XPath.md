	//a[contains(@href, "image")]/text()
	//base/@href 		# base的href属性值
	//hxs.select('//a[contains(@href, "image")]/text()').re(r'Name:\s*(.*)')
	//div[@class="wp-pagenavi"]/a[not(@title)]

	nodename 	选取此节点的所有子节点。
	example: 	bookstore 选取 bookstore 元素的所有子节点。

	/ 	从根节点选取。
	example: 	/bookstore 选取根元素 bookstore。

	// 	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
	. 	选取当前节点。
	..	选取当前节点的父节点
	@	选取属性。


	/bookstore/book[1] 		选取属于 bookstore 子元素的第一个 book 元素。
	/bookstore/book[last()] 选取属于 bookstore 子元素的最后一个 book 元素。
	/bookstore/book[last()-1]	
	/bookstore/book[position()<3]	选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
	//title[@lang]
	//title[@lang='eng']
	/bookstore/book[price>35.00]	选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。
	//title[@*]