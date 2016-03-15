参考`http://www.cnblogs.com/SunWentao/archive/2008/07/06/1236911.html`

#### 1.复制指定类型的文件

	robocopy d:\work e:\backup\work *.xls *.xlsx *.doc *.docx /s
	robocopy d:\work e:\backup\work /e /lev:2
	
/s表示复制源文件夹下的所有子目录（非空文件夹），目标文件夹如果不存在，会自动创建  
/e表示复制源文件夹下的所有子目录（含空文件夹）  
/lev:2表示只复制两个层级内的文件，例如d:\work\soft下的文件会被复制，而d:\work\soft\office下的文件不会被复制  

##### 1.1只复制文件夹，而不复制子文件

	robocopy d:\work e:\backup\work /e *.abc
	或
	robocopy d:\work e:\backup\work /e /minage:1900101
	
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
/maxage:后面加上日期，例如/maxage:20160301表示包括2016年3月1日和之后修改的文件才会被复制  
/minage:n 排除晚于 n 天/日期的文件，例如/minage:20131231，只复制2013年及以前的文件  
maxage<=`文件修改日期`<minage  


/s注意该选项，表示不复制空文件夹（包括排除子文件后的空文件夹）

#### 5.将文件复制到同一个文件夹中

	xxcopy d:\work e:\look /s /in*.txt /in*.doc /sg /yy /da:2016-01-01 /db:2016-03-31

> 注意：xxcopy非windows原生命令，需要从`http://www.xxcopy.com/`下载，并且注意在管理员身份运行的cmd中执行xxcopy命令  

/s复制文件夹及子文件夹的内容，不复制空文件夹，/s和/e等参数用法与robocopy相同  
`/in*.*`用于指定文件类型  
/sg表示复制到同一个文件夹  
/yy表示在要求用户应答时都默认为yes  
/da表示开始日期  
/db表示结束日期  
da<=`文件修改日期`<=db  

#### 6.（克隆）同步文件夹

一般情况下复制文件是增量复制，例如首次复制[a,b]->[a,b]，第二次复制[a,c]->[a,b,c]，源文件夹中b文件已被删除，但第二次复制后，目标文件夹中的b文件仍然存在  

	robocopy d:\work e:\backup\work /mir

因为是克隆，所以不需要指定/s或/e参数，目标文件夹中多余的文件将被删除  
> 备份文件服务器应该慎用此命令    

#### 7.移动文件

	robocopy d:\work e:\backup\work /move /e

/move表示移动文件  
/e注意最好使用该参数而不是/s，否则空文件夹将丢失  

#### 8.只复制文件夹，而不拷贝文件

1.1已经实现  

	xxcopy d:\work e:\backup\work /t /yy

/t表示创建文件夹结构  
/dl3表示复制的文件夹层级为3级，不指定该参数，则复制所有文件夹  

#### 9.复制文件时忽略隐藏文件

	robocopy d:\work e:\backup\work /e /xa:h
	
/xa:表示排除指定属性的文件  
h表示隐藏属性，r为只读，a为存档，s为系统文件属性  
/ia:表示复制指定属性的文件
	
	robocopy d:\work e:\backup\work /e /a-:hr

/A+:将给定的属性添加到复制的文件  
/A-:从复制的文件中删除给定的属性  

#### 10.复制文件时包含NTFS权限

	robocopy d:\work e:\backup\work /copyall

/copyall相当于/copy:datsou，表示将所有源文件夹的信息复制到目标文件夹中  
其中D:文件数据，A:文件属性，T:时间信息，S:权限信息，O:所有者信息，U:审核信息  

> 注意：需要以管理员身份运行cmd并执行，才能使用/copyall属性  

更新已复制的文件属性，而不需要重新复制文件  

	robocopy d:\work e:\backup\work /copy:sou

> 注意：经测试，只能更新NTFS权限，而不能更新系统属性  

#### 11.复制到服务器

	net use \\192.168.1.10\Sharefolder /user:USERNAME PASSWORD
	robocopy d:\work \\192.168.1.10\Sharefolder\work /e /copyall
	net use \\192.168.1.10\Sharefolder /delete

使用Powershell脚本复制文件到服务器，完成后发送日志到指定邮箱地址，参见`https://klyavlin.wordpress.com/2012/09/19/robocopy-network-usernamepassword/`  

#### 12.监视并自动复制修改过的文件

	robocopy d:\work e:\backup\work /e /copyall /mot:1 /mon:2

/mot:m如果有文件发生修改，则m分钟后再次执行检查
/mon:n至少n个文件发生修改后，进行复制

#### 13.指定时间范围内复制

	robocopy d:\work e:\backup\work /e /copyall /rh:0000-0600

/rh:hhmm-hhmm，指定开始的时间段，超出时间段则暂停，时间为24小时格式，从0000到2359，两个时间不能相同  

> 经过测试，如果在指定时间范围内复制未完成，超出时间后，复制仍然继续

#### 14.结合任务计划定期执行

	建立bat批处理文件
	robocopy d:\work e:\backup\work /e /copyall /mot:1 /mon:1
	设置任务计划，并设定开始时间
	
#### 15.清理文件夹

	删除所有tmp文件
	xxcopy d:\work\*.tmp /s /h /yy /rs

/s表示复制文件夹及子文件（夹），不复制空文件夹  
/h表示复制隐藏文件  
/yy表示确认操作，无需干预  
/rs表示删除文件而不是复制  

	删除指定日期及之前的文件夹
	xxcopy c:\temp /rmdir /db:2012-01-01 /yy

/rmdir删除文件  
/db:对此日期及之前的文件和文件夹进行操作  
	
	删除0字节文件
	xxcopy c:\temp*.* /sz:0 /s /h /yy /rs

/sz:指定文件的大小，或指定范围n-m，单位为byte  

#### 15.保存及调用作业任务
	
	robocopy d:\work e:\backup\work /e /save:D:\robojob\backup_work /L

/L :: 仅列出 - 不复制、添加时间戳或删除任何文件。

	调用任务
	robocopy /job:D:\robojob\backup_work

#### 16.保存执行日志

	robocopy d:\work e:\backup\work /e /log+:d:\robolog\backup_work.log

/log+:将日志附加到现有日志中  
/log:覆盖现有日志  

#### 17.多线程复制

	robocopy d:\test d:\test2 bigfile.rar /mt:128 /log:D:\test\test.log

/mt:多线程复制，1-128
/log:使用日志输出，以获得更好的性能

#### 18.只模拟而不执行操作

	robocopy d:\work e:\backup\work /e /log:d:\robolog\backup_work.log /L