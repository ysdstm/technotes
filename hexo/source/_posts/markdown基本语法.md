title: markdown基本语法
date: 2016-02-04 17:02:39
tags:
---

#### 文本换行
这是第1行
这是第2行
这是第3行，行的结尾都没有留两个空格，所以无法显示换行效果

这是第1行  
这是第2行  
这是第3行  

**同时要注意列表、代码等要另起两行**

#### 标题

	# 一级标题
	## 二级标题
	### 三级标题
	#### 四级标题
	##### 五级标题
	###### 六级标题


#### 列表
列表的显示只需要在文字前加上 `-` 或 `*` 即可变为无序列表，有序列表则直接在文字前加`1.` `2.` `3.` 符号要和文字之间加上一个字符的空格。例如：  

* Apple
* Banana
* Orange
 * Orange Juice


1. 项目1
2. 项目2
3. 项目3


#### 引用
在文本前加入`> `(大于号和空格)，例如：
> 这是引用  

要注意符号和文本间的空格

#### 图片与链接
图片为:`![Baidu Logo](https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png)` 

![Baidu Logo](https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png)
 
链接为:`[Baidu](http://www.baidu.com "Visit Baidu")`  

[Baidu](http://www.baidu.com "Visit Baidu")


#### 粗体 斜体 删除线
用`**`包含文本是粗体，用`*`包含文本是斜体，用`~~`包含文本是删除线，用例如

这是**粗体** 这是*斜体* 这是~~删除线~~

#### 表格

	| Tables        | Are           | Cool  |
	| ------------- |:-------------:| -----:|
	| col 3 is      | right-aligned | $1600 |
	| col 2 is      | centered      |   $12 |
	| zebra stripes | are neat      |    $1 |

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

#### 代码

只需要用两个 \` 把中间的代码包裹起来，或者在没行前插入`Tab`

例如查询所有行`select * from tablename`

SQL Code

	select name, department, salary 
	from employee
	where salary > 5000

Python Code

	#coding=utf-8
	import urllib2
	#使用raw_input()是为了与2.7版本兼容，3.x版本使用input()函数，在这里使用需要在输入的字符串两边加上单引号
	url=raw_input("url(Eg: http://www.baidu.com):\n")
	response=urllib2.urlopen(url)
	html=response.read()
	print html

#### 分隔线
分割线的语法只需要三个 * 号，例如：

***

#### 更多参考
[Markdown入门学习小结](http://www.jianshu.com/p/21d355525bdf)
