#### 启动sqlite3  

$ `sqlite3`  

#### sqlite帮助

`sqlite>.help` 
sqlite中的命令称为点命令，以`.`开头，结尾不需要加`;`  

#### sqlite常用命令

显示当前打开或附加的数据库  
`.databases`  

以SQL文本格式转存数据库  
`.dump ?TABLE?`  

打开或关闭行标题显示  
`headers on|off`  

设置输出模式  
`mode MODE`,MODE 可以是:  

	csv		逗号分隔的值
	column	左对齐的列
	html	HTML 的 <table> 代码
	insert	TABLE 表的 SQL 插入（insert）语句
	line	每行一个值
	list	由 .separator 字符串分隔的值
	tabs	由 Tab 分隔的值
	tcl	TCL 列表元素

在NULL值的地方输出字符串  
`.nullvalue STRING`  

发送输出到FILENAME文件  
`.output FILENAME`  

发送输出到屏幕  
`.output stdout`  

设置"column"模式的列宽度  
`.width NUM NUM`  

#### 格式化输出

	sqlite>.header on
	sqlite>.mode column
	sqlite>.timer on

---

#### 创建数据库

创建空白数据库  
$`sqlite3 DBNAME.db`  

从SQL文件恢复  
$`sqlite3 DBNAME.db < DBNAME.sql`  

#### 导出数据库

$`sqlite3 DBNAME.db .dump > DBNAME.sql`  

---

#### sqlite数据类型

	NULL	值是一个 NULL 值。
	INTEGER	值是一个带符号的整数，根据值的大小存储在 1、2、3、4、6 或 8 字节中。
	REAL	值是一个浮点值，存储为 8 字节的 IEEE 浮点数字。
	TEXT	值是一个文本字符串，使用数据库编码（UTF-8、UTF-16BE 或 UTF-16LE）存储。
	BLOB	值是一个 blob 数据，完全根据它的输入存储。

#### 创建表

	CREATE TABLE notes
	(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	title TEXT,
	content TEXT,
	comment TEXT,
	categoryid INTEGER,
	date DATETIME DEFAULT (datetime('now','localtime')));
	
	CREATE TABLE category
	(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	categoryname TEXT,
	fathercategoryid INTEGER);

> 自增列类型只能是INTEGER，插入一个新数据时，只需要将这个字段的值指定为NULL，即可由引擎自动设定其值，引擎会设定为最大的rowid+1

#### 修改表

修改表名称
	
	ALTER TABLE table_name RENAME TO new_table_name;
	
新增列
	
	ALTER TABLE table_name ADD COLUMN time INTEGER;

> 已存在的数据行在该列的数据为NULL

删除列

	ALTER TABLE table_name DROP column_name

修改列数据类型

	ALTER TABLE table_name ALTER COLUMN column_name datatype

