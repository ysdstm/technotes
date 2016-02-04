#### 列出文件及目录

	ls -F 方便区分目录和文件，目录后面加了/
	ls -R 输出了目录下包含的文件
	ls -F -R

	ls -l
	文件类型，目录d，文件-，字符型c，块文件b
	文件的权限
	文件的硬连接总数
	文件属主的用户名
	文件属组的组名
	文件的大小 字节为单位
	文件的上次修改时间
	文件名活目录名

	ls -sail 组合参数

	ls -l test1
	ls -l test?
	ls -l test*

	touch file1 创建文件
	touch -t 201112251200 test1  创建特定时间的文件

#### 拷贝、移动、删除文件

	copy file1 file2
	copy file1 dir1
	copy /home/zwinzhu/dir1/test1 .  拷贝到当前目录

	cp -p file1 file2 为目标文件保留源文件的访问时间和修改时间

	cp -R dir1 dir2

	cp -f test* dir2

	cp -l file1 file2 创建硬链接
	cp -s file1 file3 创建软链接

	mv test1 test2 重命名文件名
	mv dir1 dir2  重命名目录名

	rm -i test1 删除文件，带提示

	mkdir dir1 创建文件夹
	rmdir dir1 只能删除空文件夹

	rm -r dir1 删除目录及其中所有内容
	rm -rf dir1 不再提示是否删除，慎用！

#### 输出文本文件

	stat file1 显示详细的文件信息
	file file1 查看文件类型 文本文件|可执行文件|数据文件

	cat file1 显示文件内容
	cat -n file1 显示行号
	cat -b file1 只给有文本的行加上行号
	cat -s file1 合并多余的空格
	cat -T file1 不输出制表符

	cat file1 | more
	more的命令选项
	H 帮助菜单
	spacebar 下一屏
	enter 下一行
	q 退出
	b 上一屏
	/expression 在文件中查找匹配文本表达式的内容
	n 查找下一处匹配的内容
	' （单引号）跳到匹配内容的第一处
	!cmd 执行shell命令
	v 在当前行启动vi编辑器
	= 显示当前行在文件中的行号
	. 重复执行前一个命令

	上下箭头

	cat file1 |less

	tail file1 查看部分文件：末尾10行
	head file1 前10行