参考`http://blog.163.com/haijun_huang/blog/static/1675913772010989506585/`

#### 1.复制指定类型的文件

	robocopy d:\work e:\backup\work *.xls *.xlsx *.doc *.docx /s
	robocopy d:\work e:\backup\work /e /lev:2
	
/s表示复制源文件夹下的所有子目录（非空文件夹），目标文件夹如果不存在，会自动创建  
/e表示复制源文件夹下的所有子目录（含空文件夹）  
/lev:2表示只复制两个层级内的文件，例如d:\work\soft下的文件会被复制，而d:\work\soft\office下的文件不会被复制  

##### 1.1只复制文件夹，而不复制子文件

	robocopy d:\work e:\backup\work /e *.a
	
通过指定/e拷贝所有目录，和实际不存在的文件类型，可以达到复制文件夹，而不复制文件的目的


#### 2.排除指定类型的文件

	robocopy d:\work e:\backup\work /e /xf *.tmp *.bak
	robocopy d:\work e:\backup\work /e /xd d:\work\temp
	
/xf用于指定不执行复制操作的文件类型  
/xd用于指定不执行复制操作的文件夹  

#### 3.排除大文件和小文件

	robocopy d:\work e:\backup\work /e /max:6000000

/max:表示复制最大为6000000 bytes的文件，大于该数值的忽略，数值单位为字节byte  
/min:1024表示复制不小于1k的文件

#### 4.复制指定天数内修改的文件

	robocopy robocopy d:\work e:\backup\work /s /maxage:7
	
/maxage:n 排除早于 n 天/日期的文件  
/maxage:后面直接加上数字，表示天数，但必须小于1900  
/maxage:后面加上日期，例如/maxage:20160301表示2016年3月1日之后修改的文件才会被复制  
/minage:n 排除晚于 n 天/日期的文件，例如/minage:20131231，只复制2013年及以前的文件  

/s注意该选项，表示不复制空文件夹（包括排除子文件后的空文件夹）