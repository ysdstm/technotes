#### 查看及结束进程

	ps 查看进程，仅显示当前控制台下的当前用户的进程
	ps -ef e所有进程，f扩展显示
	UID：启动这个进程的用户
	PID：进程的进程号（PID）
	PPID：父进程的进程号
	C：进程申明周期中的CPU利用率
	STIME：进程启动时的系统时间
	TTY：进程启动时的终端设备
	TIME：运行进程需要的累计CPU时间
	CMD：启动的程序名称

	ps -l
	F：内核分配给进程的系统标记
	S：进程的状态，O正在运行，S正在休眠，R可运行，正在等待运行；Z表示僵化，进程已结束但父进程已不存在；T代表停止
	PRI：进程的优先级，数字越大优先级越低
	NI：谦让度，用来参与决定优先级
	ADDR：进程的内存地址
	SZ：假如进程被换出，所需交换空间的大致大小
	WCHAN：进程休眠的内核函数的地址

	ps -efH 树状方式显示父子进程


	top 实时显示进程信息
	第一行显示当前时间、系统的运行时间、登入的用户数以及系统的平均负载
	平均负载：最近1分钟、5分钟、15分钟的平均负载，值越大负载越高
	最近1分钟的负载高很正常，15分钟的平均负载高就不正常了，超过2说明负载高
	第二行显示概要的进程信息，处于运行、休眠、停止或者僵化状态（子进程完成了，父进程没有响应）的进程数量
	第三行显示CPU信息，
	第四行显示系统内存的状态，系统的物理内存：总共内存和空闲内存
	最后一行显示当前运行中的进程详细列表
	PID：进程的进程号
	USER：进程属主的名字
	PR：进程的优先级
	NI：进程的谦让度值
	VIRT：进程占用的虚拟内存总量
	RES：进程占用的物理内存总量
	SHR：进程和其他进程共享的内存总量
	S：进程的状态：D可总段的休眠状态，R正在运行，S休眠状态，T跟踪状态或停止状态，Z僵化
	%CPU：进程使用的CPU时间比例
	%MEM：进程使用的内存占可用内存的比例
	TIME+：自进程启动到目前位置的CPU时间总量
	COMMAND：进程的命令行名称，也就是启动的程序名

	默认情况下，按照%CPU值来排序
	h 显示帮助

	kill 3940 PID为进程号，需要root权限
	kill -s HUP 3940 HUP或INI强制终止进程
	killall http* 支持进程名和通配符

#### 挂载设备

	mount 输出当前系统上挂载的设备列表
	提供四部分信息：
	媒体的设备文件名
	媒体挂载到虚拟目录的挂载点
	文件系统类型
	已挂载媒体的访问状态

	手动挂载设备，root用户状态：
	mount -t type device directory
	type: vfat ntfs iso9660(CD-ROM文件系统）
	mount -t vfat /dev/sdb1 /media/disk
	命令参数
	-a 挂载/etc/fstab/文件中指定的所有文件系统
	-f 模拟挂载设备，但不真的挂载
	-F 和参数-a一起使用，将会挂载所有文件系统
	-v 详细模式，将会说明挂载设备的每一步
	-I (i)不启用任何/sbin/mount.filesystem下的文件系统帮助文件
	-l (L)给ext2、ext3或XFS文件系统自动添加文件系统标签
	-n 挂载设备，但不注册到/etc/fstab已挂载的设备文件中
	-p num 对加密文件进行挂在时，从文件描述符num中获得密码短语
	-s 忽略该文件系统不支持的挂载选项
	-r 将设备挂载为只读的
	-w 将设备挂载为刻度写的（默认）
	-L lable 将设备按指定的label挂载
	-U uuid 将设备按指定的uuid挂载
	-O 和-a参数一起使用，限制命令只作用到特定的一组文件系统上
	-o 给文件系统添加特定的选项

	-o参数允许添加的额外选项，用逗号分隔
	ro：只读
	rw：读写
	user：允许普通用户挂载文件系统
	check=none：挂载文件系统时不进行完整性校验
	loop：挂载一个文件
	例如：
	mount -t iso9600 -o loop MEPIS-KDE4-LIVE-DVD_32.iso ./mnt

	卸载设备：当前目录不能是挂载目录，否则 device is busy
	umount /home/rich/mnt
	ls -l mnt
	total 0
	不能卸载，提示设备忙时，可以用lsof命令获取正在使用它的进程信息
	lsof /path/to/device/node
	lsof /path/to/mount/point

	df 查看已挂载磁盘的使用情况
	df -h 以M和G为单位来显示使用情况

	du 显示当前目录下的所有文件、目录和子目录的磁盘使情况
	参数：
	-c 显示已列出文件的总大小
	-h 用K、M、G显示大小
	-s 显示每个输出参数的总计

	du -sh * | sort -nr
	从大到小

#### 处理数据文件

	cat file1 不能将内容排序
	sort file1 将默认按照首字母和首数字排序

	sort -n file1 将把数字从小到大排序

	sort -M file1 将含有时间戳日期（Jan-Dec）的文件排序
	sort参数
	-b 忽略起始的空白
	-c 检查是否排序，未排序则报告
	-d 按字典排序，仅考虑空格和字母，补考虑特殊字符
	-g 按通用数值排序，与-n不同，把值当作浮点数值来排序
	-i 排序时忽略不可打印字符
	-k 键序位置选择，见下面示例
	-M 用三字符月份按月份排序
	-m 将两个已排序数据文件合并
	-n 按字符串数值来排序，并不转换为浮点数
	-o 将排序结果写出到指定的文件中
	-R 按随机生成的哈希表的键值排序
	-r 反序排序
	-S 指定使用的内存大小
	-T 指定一个位置来存储临时工作文件
	-t 指定一个用来区分键未知的字符
	-u 和-c参数一起使用时，检查严格排序，不和-c参数一起使用时，仅输出第一列相似的两行
	-z 用NULL字符来为没一行结尾而不是用换行符

	-k和-t参数在对按字段分割的数据进行排序时非常有用，例如/etc/passwd文件
	根据用户ID进行数值排序：
	sort -t':' -k 3 -n /etc/passwd

	-n参数常用来排序数值
	du -sh * | sort -nr

	搜索数据
	grep [options] pattern [file]
	搜索three
	grep three file1

	grep -v three file1 反向搜索
	grep -n three file1 现实匹配模式的行所在的行号
	grep -c three file1 输出有多少行中含有three

	grep -e three -e four file1 搜索包含three或four的行
	正则表达式：
	grep [tf] file1 搜索包含t或f的行，详见第19章


#### 压缩及解压数据

|工具 |文件扩展名|
|----|---------|
|bzip2|.bz2|
|compress|.z|
|gzip|.gz|
|zip|.zip|

	1.bzip2工具
	bzip2：用来压缩文件
	bzcat：用来显示压缩的文本文件的内容
	bunzip2：用来解压.bz2文件
	bzip2recover：用来尝试恢复损坏的压缩文件

	bzip2 myprog 压缩myprog文件，生成myprog.bz2并删除原文件
	bzcat test.bz2 显示压缩文本的内容

	2.gzip工具
	gzip
	gzcat
	gunzip

	gzip myprog 用法和bzip2一样
	gzip my* 使用通配符一次压缩几个文件，生成数个.gz文件

	3.zip工具
	zip 创建一个压缩文件，包含指定的文件和目录
	zipcloak 创建加密的压缩文件，包含指定的文件和目录
	zipnote 从zip文件中提取批注
	zipsplit 将一个现有zip文件分割成多个更小的固定大小的文件
	unzip 解压zip文件中的文件和目录

	zip 显示zip的用法和命令
	zip -r testzip test 创建testzip.zip文件，并递归目录test，根据文件类型决定是否压缩以及压缩比例

	归档数据
	tar是Unix和Linux上最广泛使用的归档工具

	tar function [options] object1 object2 ...

	功能
	-A 将一个tar归档文件追加到另一个tar归档文件
	-c 创建一个新的tar归档文件
	-d 检查归档文件和系统文件的不同之处
	-r 追加文件到已有tar归档文件的末尾
	-u 列出已有tar归档文件的内容
	-x 从tar归档文件中提取文件

	-C dir 切换到指定目录
	-f file 输出结果到文件或设备file
	-j 将输出重定向给bzip2命令来压缩内容
	-p 保留所有文件权限
	-v 在处理文件时显示文件
	-z 将输出重定向给gzip命令来压缩内容

	tar -cvf test.tar test/ test2/ 压缩test和test2目录内容到test.tar文件
	tar -tf test.tar 列出内容，但不解压
	tar -xvf test.tar 提取内容

	.tgz文件是gzip压缩过的tar文件，可用命令tar -zxvf file.tgz来解压
