### 第1章 虚拟机安装RedHat7.2

#### 1.7 安装VMware Tools

1. 点击 虚拟机-重新安装VMware Tools

2. 在图形环境下，自动挂载在/run/media/root/VMware Tools目录下

   手动挂载，在root身份下运行

   ```shell
   mkdir -p /media/cdrom
   mount /dev/cdrom /media/cdrom
   cd /media/cdrom
   cp VMwareTools-10.0.6-3595377.tar.gz /home
   cd /home
   tar -xzvf VMwareTools-10.0.6-3595377.tar.gz
   cd vmware-tools-distrib
   #-d参数，默认安装
   ./vmware-install.pl -d
   #重启生效
   reboot
   ```

#### 1.8 重要的守护进程

￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼有一些系统服务需要时刻等待用户的输入或随时响应用户的请求，称为守护进程（Daemon），通常会随系统启动时激活并随系统关闭时停止，一直在系统后台运行。

**常见的守护进程：**

```
crond	计划任务
dhcpd	动态IP地址分配服务(DHCP)
httpd	网站服务
lpd		打印服务器
named 	域名解析服务(DNS)
nfs		文件共享服务(NFS)
smb		文件共享域打印服务(SAMBA)
syslog	系统日志
gpm		鼠标进程
```

#### 1.9 红帽软件包管理器RPM

RPM出现前，用户需要使用源码包进行安装，需要自行编译，并解决大量依赖关系，在校验、安装、卸载、查询、升级时难度非常大。

RPM原称为Redhat Package Manager，由于被大众认可，目前使用的范围不局限于红帽系统。RPM会建立统一的数据库文件，详细记录软件信息并能够自动分析依赖关系。

**主要有以下命令：**

```shell
#安装软件
rpm -ivh package.rpm
#升级软件
rpm -Uvh package.rpm
#卸载软件
rpm -e package.rpm
#查询软件的描述信息
rpm -qpi package.rpm
#列出软件的文件信息
rpm -qpl package.rpm
#查询文件属于哪个RPM
rpm -qf package.rpm
```

#### 1.10 Yum软件仓库

Yum软件仓库是进一步简化RPM管理软件难度而设计的，能够自动分析用户所需的软件包及相关依赖关系，自动从服务器下载并安装到系统。

用户根据需求指定Yum仓库是否校验软件包。

**配置方法如下：**

所有的yum仓库配置文件以.repo结尾的，存放在/etc/yum.repos.d/目录中

```
[rhel-media]:yum源的名称，可自定义
baseurl=file:///media/cdrom 提供方式包括ftp://, http://, file:///
enabled=1 :设置此源是否可用，1为可用，0为禁用
gpgcheck=1 :设置此源是否校验源文件，1为校验，0为不校验
gpgkey=file:///media/cdrom/RPM-GPG-KEY-redhat-release :若为校验请指定公钥文件地址
```

Yum仓库中的RPM软件包可以是由红帽官方发布的，也可以是第三方组织发布的。

```
命令								作用
yum repolist all				列出所有仓库
yum list all					列出仓库中所有软件包
yum info packagename			查看软件包信息
yum install packagename			安装软件包
yum reinstall packagename		重新安装软件包
yum update packagename			升级软件包
yum remove package				移除软件包
yum clean all					清除所有仓库缓存
yum check-update				检查可更新的软件包
yum grouplist					查看系统中已经安装的软件包组
yum groupinstall packagegroup	安装指定的软件包组
yum groupremove packagegroup	移除指定的软件包组
yum groupinfo packagegroup		查询指定的软件包组信息
```



#### 1.10 Systemd初始化进程

Linux操作系统开机过程首先从BIOS开始→进入"Boot Loader"→加载内核→内核的初始化→**启动初始化进程**，初始化进程作为系统第一个进程，它需要完成相关的初始化工作，为用户提供合适的工作环境。

红帽RHEL7系统已经替换掉了大家熟悉的初始化进程**System V init**，并正式采用全新的初始化进程**systemd**。初始化进程systemd使用了并发启动机制，所以开机速度得到了不小的提升。

红帽RHEL7系统选择了**systemd**，原先的inittab将已经不再起作用，也没有了“运行级别”这个概念，Linux系统启动时要做大量的初始化工作——例如挂载文件系统和交换分区，启动各类进程服务等等操作，这些都可以看作是一个个的单元(Unit)，分析下nfs服务的单元配置文件：

```shell
# cat /etc/systemd/system/nfs.target.wants/nfs-lock.service
[Unit]
Description=NFS file locking service.
#表示rpcbind服务必须在nfs服务启动前已经运行。
Requires=rpcbind.service network.target
After=network.target named.service rpcbind.service
Before=remote-fs-pre.target
[Service]
Type=forking
StandardError=syslog+console
EnvironmentFile=-/etc/sysconfig/nfs
#启动nfs服务前需要执行的命令：
ExecStartPre=/usr/libexec/nfs-utils/scripts/nfs-lock.preconfig
#启动nfs服务具体的命令语法：
ExecStart=/sbin/rpc.statd $STATDARG
# Make sure lockd's ports are reset
ExecStopPost=-/sbin/sysctl -w fs.nfs.nlm_tcpport=0 fs.nfs.nlm_udpport=0
[Install]
WantedBy=nfs.target
```

红帽RHEL7系统中**systemd**用"**目标(target)**"代替了“**运行级别**”这个概念

```
Sysvinit运行级别	Systemd目标名称							作用
0				runlevel0.target, poweroff.target		关机
1				runlevel1.target, rescue.target			单用户模式
2				runlevel2.target, multi-user.target		等同于级别3
3				runlevel3.target, multi-user.target		多用户的文本界面
4				runlevel4.target, multi-user.target		等同于级别3
5				runlevel5.target, graphical.target		多用户的图形界面
6				runlevel6.target, reboot.target			重启
emergency		emergency.target						紧急Shell
```

将默认的运行级别修改为“多用户，无图形模式”：

```shell
ln -sf /lib/systemd/system/multi-user.target /etc/systemd/system/default.target
```

将默认的运行级别修改为“图形化模式”：

```shell
ln -sf /lib/systemd/system/graphical.target /etc/systemd/system/default.target
```

红帽RHEL6系统使用service、chkconfig等命令来管理系统服务，在红帽RHEL7系统中管理服务的命令是"**systemctl**"，使用方法大致相同：

```
Sysvinit命令(红帽RHEL6系统)	Systemctl命令（红帽RHEL7系统）		作用
service foo start			systemctl start foo.service		启动服务
service foo restart			systemctl restart foo.service	重启服务
service foo stop			systemctl stop foo.service		停止服务
service foo reload			systemctl reload foo.service	重新加载配置文件（不终止服务）
service foo status			systemctl status foo.service	查看服务状态
```

**systemctl设置服务的开机启动、不启动、查看各级别下服务启动状态的命令：**

```
Sysvinit命令(红帽RHEL6系统)	Systemctl命令（红帽RHEL7系统）	作用
chkconfig foo on			systemctl enable foo.service				开机自动启动
chkconfig foo off			systemctl disable foo.service				开机不自动启动
chkconfig foo				systemctl is-enabled foo.service			查看特定服务是否为开机自启动
chkconfig --list			systemctl list-unit-files --type=service	查看各个级别下服务的启动与禁用情况
```

### 第2章 新手必须掌握的Linux命令

##### 2.1 Shell简介

计算机硬件是由处理器、控制器、输入输出设备组成的，而在Linux中，这些物理设备是由Shell调用的，负责驱动硬件、管理活动、分配硬件资源等任务。

一般用户不能直接修改内核，需要通过系统调用接口，开发程序和服务来管理计算机。

Shell能够调用相应的程序和服务，在大多数热门的Linux系统中，主流的默认字符Shell是Bash(Bourne-Again Shell)。

什么是bash，shell是一种通用的说法，bash是shell的一种实例，除了bash还有ksh，zsh

```
shell 是一个交互性命令解释器。shell独立于操作系统，这种设计让用户可以灵活选择适合自己的shell。shell让你在命令行键入命令，经过shell解释后传送给操作系统（内核）执行。

shell是一个命令处理器（command processor）——是一个读入并解释你输入的命令的程序。除了是一个命令中断器以外，shell还是一个程序设计语言。你可以编写shell可以解释的程序（被称为源程序），这些源程序可以包含shell程序设计命令等等。shell除了解释命令以外，还有其他工作，它也可以配置和编程。

shell拥有自己的语言允许用户编写程序并以一种复杂方式运行。shell编程语言具有许多常用的编程语言的特征，例如：循环和控制结构等。用户可以生成像其他应用程序一样复杂的shell程序。 

以下是shell功能的一个汇总： 
查找命令的位置并且执行相关联的程序； 
为shell变量赋新值；
执行命令替代； 
处理 I/O重定向和管道功能；
提供一个解释性的编程语言界面，包括tests、branches和loops等语句。

bash是borne again shell的缩写，它是shell的一种,Linux上默认采用的是bash。
当你在命令行中敲入bash命令时，相当于进入bash环境，如果本身就是bash环境，那么就是进入一个子bash环境（相当于开了一个子进程）。
```



##### 2.2 查看帮助命令

常见的命令格式：

**命令名称** \[命令参数\] \[命令对象\]

命令参数可以使用长格式(完整的选项名称)，也可以使用短格式(单个字母的缩写)，分别用"- -"和"-"作前缀

例如：

```shell
man --help
man -h
```

man命令的可用帮助文档分类有：

| 代码   | 代表内容       |
| ---- | ---------- |
| 1    | 普通的命令      |
| 2    | 内核调用的函数与工具 |
| 3    | 常见的函数与函数库  |
| 4    | 设备文件的说明    |
| 5    | 配置文件       |
| 6    | 游戏         |
| 7    | 惯例与协议      |
| 8    | 管理员可用的命令   |
| 9    | 内核相关的文件    |



man命令的帮助文档目录结构：

| 结构名称        | 代表意义         |
| ----------- | ------------ |
| NAME        | 命令的名称        |
| SYNOPSIS    | 参数的大致使用方法    |
| DESCRIPTION | 介绍说明         |
| EXAMPLES    | 演示（附带简单说明）   |
| OVERVIEW    | 概述           |
| DEFAULTS    | 默认的功能        |
| OPTIONS     | 具体的可用选项（带介绍） |
| ENVIRONMENT | 环境变量         |
| FILES       | 用到的文件        |
| SEE ALSO    | 相关的资料        |
| HISTORY     | 维护历史与联系方式    |



man命令的操作按键：

| 按键          | 用处                     |
| ----------- | ---------------------- |
| 空格键         | 向下翻一页。                 |
| [Page Down] | 向下翻一页。                 |
| [Page Up]   | 向上翻一页。                 |
| [HOME]      | 直接前往首页。                |
| [END]       | 直接前往尾页。                |
| /关键词        | 从上至下搜索某个关键词,如"/linux"。 |
| ?关键词        | 从下至上搜索某个关键词,如"?linux"。 |
| n           | 定位到下一个搜索到的关键词。         |
| N           | 定位到上一个搜索到的关键词。         |
| q           | 退出帮助文档。                |



##### 2.3 常用系统工作命令

###### **echo命令用于在终端显示字符串或变量**

echo \[字符串|变量]

```shell
echo abc
echo $SHELL
echo $HOSTNAME
```

###### **date命令用于显示/设置系统的时间或日期**

date \[选项][+指定的格式]

要显示指定格式的日期和时间，输入"+"号开头的字符串指定格式，例如

```shell
date "+%Y-%m-%d %H:%M:%S"
```

详细格式参数：

| 参数   | 作用                      |
| ---- | ----------------------- |
| %t   | 跳格[TAB键]                |
| %H   | 小时(00-23)               |
| %I   | 小时(01-12)               |
| %M   | 分钟(00-59)               |
| %S   | 秒（00-60）                |
| %X   | 相当于%H:%M:%S             |
| %Z   | 显示时区                    |
| %p   | 显示本地AM或PM               |
| %A   | 星期几 (Sunday-Saturday)   |
| %a   | 星期几 (Sun-Sat)           |
| %B   | 完整月份 (January-December) |
| %b   | 缩写月份 (Jan-Dec)          |
| %d   | 日(01-31)                |
| %j   | 一年中的第几天(001-366)        |
| %m   | 月份(01-12)               |
| %Y   | 完整的年份                   |

其他常用命令：

```shell
#查看系统日期和时间
date
#按照"年-月-日 小时:分钟:秒"的格式：
date "+%Y-%m-%d %H:%M:%S"
#设置系统时间为2015年9月1日8点半：
date -s "20150901 8:30:00"

#查看本地系统时区：
date "+%Z"
#查看星期几：
date "+%A"
#查看当前是上午还是下午：
date "+%p"
#判断今天是一年中的第几天：
date "+%j"
```



###### **reboot命令用于重启系统**

```shell
#重启系统
reboot
```

###### **wget命令用于使用命令行下载网络文件，**

wget [参数] 下载地址

| 参数   | 作用                  |
| ---- | ------------------- |
| -b   | 后台下载模式。             |
| -O   | 下载到指定目录。            |
| -t   | 最大尝试次数。             |
| -c   | 断点续传                |
| -p   | 下载页面内所有资源,包括图片、视频等。 |
| -r   | 递归下载                |

```shell
#下载文件
wget http://www.linuxprobe.com/Tools/RHEL-server-7.0-x86_64-LinuxProbe.Com.iso
#下载整站
wget -r -p http://www.linuxprobe.com
```

###### **ps命令用于查看系统中的进程状态**

ps [参数]

| 参数   | 作用               |
| ---- | ---------------- |
| -a   | 显示所有的进程（包括其他用户的） |
| -u   | 用户以及其他详细信息       |
| -x   | 显示没有控制终端的进程      |

```shell
#查看进程与状态
ps -aux
#查找某个特定的进程信息
ps -aux | grep 进程名

```

Linux系统中时刻运行着许许多多的进程，如果能够合理的管理它们，绝对有益于系统的性能优化，系统进程总共有5种不同的状态：

```
R(运行):正在运行或在运行队列中等待。
S(中断):休眠中, 在等待某个条件的形成或接受到信号。
D(不可中断):收到信号不唤醒和不可运行, 进程必须等待直到有中断发生。
Z:(僵死):进程已终止, 但进程描述符存在, 直到父进程调用wait4()系统调用后释放。
T:(停止):进程收到SIGSTOP, SIGSTP, SIGTIN, SIGTOU信号后停止运行。
```



```shell

#第1行:系统时间，运行时间，登陆用户数，系统负载（分别为1分钟、5分钟、15分钟的平均值）。
top - 12:11:23 up  1:56,  3 users,  load average: 0.00, 0.01, 0.05
#第2行:进程总数，运行中的，睡眠中的，停止的，僵尸的。
Tasks: 498 total,   1 running, 497 sleeping,   0 stopped,   0 zombie
#第3行:用户占用资源，系统内核占用资源，改变过优先级的进程，空闲的资源，等待输入输出的时间。
#此行数据均为CPU数据并以百分比格式显示，例如"99.7 id"意味着有99.7%的CPU资源正在空闲中。
%Cpu(s):  0.0 us,  0.3 sy,  0.0 ni, 99.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
#第4行:物理内存总量，使用量，空闲量，作为内核缓存的内存量。
KiB Mem :  1868692 total,   722396 free,   566428 used,   579868 buff/cache
#第5行:虚拟内存总量，使用量，空闲量，已被提前加载的内存数据。
KiB Swap:  2097148 total,  2097148 free,        0 used.  1080480 avail Mem 

   PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                                  
 17461 root      20   0  146412   2416   1432 R   0.7  0.1   0:00.50 top 
```

进程详细信息：

```
PID:进程ID号
USER:进程的所有者
PR:优先级
NI:优先级（负值表示优先级更高）
VIRT:虚拟内存使用量
RES:物理内存使用量
SHR:共享内存大小
S:进程状态（上文中有提到）
%CPU:运算器的使用百分比
%MEM:内存的使用百分比
TIME+:使用CPU的时间(单位是1/100秒)
COMMAND:命令名称
```

###### **pidof命令用于查询某个特定程序的进程PID值**

pidof \[参数][程序名称]

```ssh
pidof sshd
```

###### **kill命令用于终止某个特定PID号码的进程**

kill \[参数][进程PID号]

```shell
#强制终止PID为4674的进程:
kill -9 4674
#其中的"-9"代表强制终止(SIGKILL)，也是最常用的一种信号参数，查看全部请执行"kill -l"
```

###### **killall命令用于终止某个特定名称的所有进程**

killall \[参数][进程名称]

```shell
killall sshd
```

> 在终端中运行一个命令后如果想立即的停止它，可以使用组合键"**Ctrl+C**"，这样命令的进程将会彻底的被终止。
>
> 另一个命令是"**Ctrl+Z**"，它是将命令的进程暂停（也叫挂载到后台或扔到后台）

通过实例比较两种命令，以及jobs，bg，fg等命令：

````shell
#1.以下命令每秒向jobs.txt中追加一个字符串
(while true ;do echo -n " working " >> ~/jobs.txt;sleep 1 ;done;)
#2.新建一个会话查看命令是否一直在运行
tail -f ~/jobs.txt
#3.在前一个会话中按下Ctrl+Z，命令被暂停
^Z
[1]+  已停止               ( while true; do
    echo -n " working " >> ~/jobs.txt; sleep 1;
done )
#4.使用jobs命令可以查看到所有在后台运行着的进程:
jobs
[1]+  已停止               ( while true; do
    echo -n " working " >> ~/jobs.txt; sleep 1;
done )
#5.运行bg命令让后台的程序继续执行，现在后台中只有一个进程，所以省略了编号，完整格式应为"bg 1"：
bg
[1]+ ( while true; do
    echo -n " working " >> ~/jobs.txt; sleep 1;
done ) &
#命令恢复运行，通过第二个会话可以看到
#6.运行fg命令将后台的进程再调回前台，程序依然在运行，此时可以敲击组合键"Ctrl+C"：
fg
( while true; do
    echo -n " working " >> ~/jobs.txt; sleep 1;
done )
#7.终止命令
^C

#8.有些命令在执行时会不断的在终端上输出信息，影响到我们继续输入命令了，此时便可以在这条命令后面添加个"&"符号,那么从一开始执行该命令就会是在后台执行
(while true ;do echo -n " working " >> ~/jobs.txt;sleep 1 ;done;)&
````

##### 2.4 系统状态检测命令

###### ifconfig用于获取网卡配置与网络状态等信息 

ifconfig \[网络设备][参数]

###### uname命令用于查看系统内核版本等信息

uname [-a]

```shell
#在红帽系统中也可以查看redhat-release文件
cat /etc/redhat-release
```

###### uptime命令用于查看系统的负载情况

uptime

```shell
#实时查看系统负载
watch -n 1 uptime
```

###### free命令用于显示当前系统中内存的使用量情况

```shell
free -m
              总计内存      已使用       可用       进程共享 磁盘缓存       可用
              total        used        free      shared  buff/cache   available
Mem:           1824         603         460          10         761        1002
Swap:          2047           0        2047
```

###### who命令用于查看当前登入主机的用户情况

```shell
who
zwinzhu  :0           2016-06-30 10:15 (:0)
zwinzhu  pts/0        2016-06-30 10:15 (:0)
zwinzhu  pts/1        2016-07-01 11:03 (172.16.1.13)
```

###### last命令用于查看所有系统的登入记录

```shell
last
zwinzhu  pts/1        172.16.1.13      Fri Jul  1 11:03   still logged in   
zwinzhu  pts/2        172.16.1.13      Thu Jun 30 12:47 - 17:31  (04:44)    
zwinzhu  pts/1        172.16.1.13      Thu Jun 30 10:16 - 17:31  (07:15)
```

###### history命令用于显示历史执行过的命令

```shell
history 
    1  sudo -i
    2  ls
    3  sudo service vmware-tools status
    4  sudo -i
    5  ls
    6  ifconfig
    7  cat /etc/redhat-release
#清除历史
history -c
#历史命令保存在
cat ~/.bash_history
#修改history保存数量
nano /etc/history
#修改 HISTSIZE=1000
```

###### sosreport命令用于收集系统系统配置并诊断信息后输出结论文档

> 当红帽系统出现故障需要联系红帽厂商或其他技术支持时，大多数情况都需要提供使用到这个命令。

```shell
sosreport

sosreport (version 3.2)

This command will collect diagnostic and configuration information from
this Red Hat Enterprise Linux system and installed applications.

An archive containing the collected information will be generated in
/var/tmp and may be provided to a Red Hat support representative.

Any information provided to Red Hat will be treated in accordance with
the published support policies at:

  https://access.redhat.com/support/

The generated archive may contain data considered sensitive and its
content should be reviewed by the originating organization before being
passed to any third party.

No changes will be made to system configuration.

Press ENTER to continue, or CTRL-C to quit.

Please enter your first initial and last name [redhat7.2vm]: 
Please enter the case id that you are generating this report for []: 

 Setting up archive ...
 Setting up plugins ...
 Running plugins. Please wait ...

  Running 92/92: yum...                      
Creating compressed archive...

Your sosreport has been generated and saved in:
  /var/tmp/sosreport-redhat7.2vm-20160701133607.tar.xz

The checksum is: 09b026b5ad2539a88cb19e681757cc31

Please send this file to your support representative.
```



##### 2.5 工作目录切换

###### pwd命令用于显示当前工作目录

```shell
#当前工作目录
pwd
#当前实际工作目录，非链接地址
pwd -P

```

###### cd用于切换工作目录

```shell
#切换到上一次目录
cd -
#进入当前用户home目录
cd ~
#切换到其他用户的home目录
cd ~zwinzhu
#进入上层目录
cd ..
```

###### ls命令查看目录中的文件及文件夹

ls \[选项] [文件]

```shell
ls -a #查看全部文件
ls -d #查看目录本身
ls -h #易读的文件大小
ls -l #显示文件的详细信息

ls -ldh ./
dr-xr-x---. 15 root root 4.0K 6月  30 12:46 ./
```

##### 2.6 文本编辑命令

###### cat用于查看纯文本文件

cat \[选项] [文件]

```shell
cat -n #显示行号
cat -b #显示行号，不包括空行
cat -A #显示不可见的符号，例如空格，tab等
```

###### more用于查看较长的文本文件

```shell
more -数字 #预先显示的行数，默认为一页
more -d #显示提示语句与报错信息
```

###### head用于查看纯文本文件的前n行

```shell
head -n 10 #显示10行
head -n -10 #显示不包括最后10行的内容
```

###### tail用于查看纯文本文件的后n行

```shell
tail -n 10 #显示最后10行
tail -f #持续刷新显示的内容
```

###### od命令用于查看特殊的文件格式

| 参数      | 作用      |
| ------- | ------- |
| od -t a | 默认字符    |
| od -t c | ASCII字符 |
| od -t o | 八进制     |
| od -t d | 十进制     |
| od -t x | 十六进制    |
| od -t f | 浮点数     |

###### tr命令用于转换文本文件中的字符

```shell
#将把小写字母转换为大写字母
cat a.txt | tr [a-z] [A-Z]
```

###### wc命令用于统计文本的行数、字数、字节数

wc [参数] 文本

| 参数   | 作用     |
| ---- | ------ |
| -l   | 只显示行数  |
| -w   | 只显示单词数 |
| -c   | 只显示字节数 |

###### cut命令用于通过列来提取文本字符

cut [参数] 文本

| 参数     | 作用            |
| ------ | ------------- |
| -d 分隔符 | 指定分隔符，默认为Tab。 |
| -f     | 指定显示的列数。      |
| -c     | 单位改为字符        |

```shell
#参数作用：-d以":"来做分隔符，-f参数代表只看第一列的内容
cut -d: -f1 /etc/passwd
#获取root用户的默认SHELL解释器
grep ^root /etc/passwd | cut -d: -f 7
```

###### diff命令用于比较多个文本文件的差异

| 参数         | 命令         |
| ---------- | ---------- |
| -b         | 忽略空格引起的差异。 |
| -B         | 忽略空行引起的差异。 |
| --brief或-q | 仅报告是否存在差异。 |
| -c         | 使用上下文输出格式。 |

```shell
diff diff_A.txt diff_B.txt
```

##### 2.7 文件管理命令

###### touch命令用于创建空白文件与修改文件时间

touch \[选项][文件]

在Linux中的文件有三种时间：

> 更改时间(mtime):内容修改时间（不包括权限的）
>
> 更改权限(ctime):更改权限与属性的时间
>
> 读取时间(atime):读取文件内容的时间

| 参数   | 作用                  |
| ---- | ------------------- |
| -a   | 仅修改“访问时间”（atime）    |
| -m   | 仅修改“更改时间”（mtime）    |
| -d   | 同时修改atime与mtime     |
| -t   | 要修改成的时间[YYMMDDhhmm] |

```shell
#将访问与修改时间修改为2天前
touch -d "2 days ago" test
```

###### mkdir用于创建空白文件夹

| 参数      | 作用                   |
| ------- | -------------------- |
| -m=MODE | 默认的文件目录权限，如"-m 755"  |
| -p      | 连续创建多层目录（若文件夹已存在则忽略） |
| -v      | 显示创建的过程              |

```shell
mkdir folder
#进入folder，变量!$或(键盘按键)代表上一条命令的参数
cd !$
#一次创建5个目录
mkdir -p a/b/c/d/e
```

###### cp用于复制文件或目录

cp [选项] 源文件 目标文件

复制命令的三种情况:

> 目标文件是一个目录，会将源文件复制到该目录中。
> 目标文件是一个文件，会将源文件覆盖该文件。
> 目标文件不存在，将会复制源文件并修改为目标文件的名称（重命名）。

| 参数   | 作用                       |
| ---- | ------------------------ |
| -p   | 保留原始文件的属性                |
| -d   | 若对象为"链接文件"，则保留该"链接文件"的属性 |
| -r   | 递归持续复制（用于目录）             |
| -i   | 若目标文件存在则询问是否覆盖           |
| -a   | 相当于-pdr（p,d,r为上述的参数）     |

###### mv用于移动文件或改名

mv [选项] 文件名 [目标路径|目标文件名]

###### rm用于删除文件或目录

| 参数   | 作用     |
| ---- | ------ |
| -f   | 忽略警告信息 |
| -i   | 删除前先询问 |
| -r   | 删除文件夹  |

###### dd命令用于指定大小的拷贝的文件或指定转换文件

| 参数         | 作用           |
| ---------- | ------------ |
| if         | 输入的文件名称。     |
| of         | 输出的文件名称。     |
| bs         | 设置每个“块”的大小。  |
| count      | 设置要拷贝“块”的个数。 |
| conv=ucase | 将字母从小写转换为大写。 |
| conv=lcase | 把字符从大写转换为小写。 |

```shell
#将光驱设备拷贝成镜像文件：
dd if=/dev/cdrom of=RHEL-server-7.0-x86_64-LinuxProbe.Com.iso
#生成一个560m的空白文件：
dd if=/dev/zero of=560_file count=1 bs=560M
#将硬盘的MBR信息拷贝出来：
dd if=/dev/sda of=sda_image count=1 bs=512K
```

##### 2.8 打包压缩文件

###### tar命令用于对文件打包压缩或解压

tar \[选项][文件]

> 打包并压缩文件:“tar -czvf 压缩包名.tar.gz 文件名”



> 解压并展开压缩包:“tar -xzvf 压缩包名.tar.gz”

| 参数   | 作用          |
| ---- | ----------- |
| -c   | 创建压缩文件      |
| -x   | 解开压缩文件      |
| -t   | 查看压缩包内有那些文件 |
| -z   | 用Gzip压缩或解压  |
| -j   | 用bzip2压缩或解压 |
| -v   | 显示压缩或解压的过程  |
| -f   | 目标文件名       |
| -p   | 保留原始的权限与属性  |
| -P   | 使用绝对路径来压缩   |
| -C   | 指定解压到的目录    |

```shell
#将/etc目录内文件打包并通过gzip格式压缩：
tar -czvf etc.tar.gz /etc
#将etc.tar.gz解压到/root/etc目录中：
mkdir /root/etc
tar xzvf etc.tar.gz -C /root/etc
```



##### 2.9 文件查询搜索

grep 关键词 文本文件

| 参数   | 作用                            |
| ---- | ----------------------------- |
| -b   | 将可执行文件(binary)当作文本文件（text）来搜索 |
| -c   | 仅显示找到的行数                      |
| -i   | 忽略大小写                         |
| -n   | 显示行号                          |
| -v   | 反向选择——仅列出没有“关键词”的行。           |

```shell
#搜索在/etc/passwd中"/sbin/nologin"出现的行，找出系统中不允许登陆的用户
grep /sbin/nologin /etc/passwd
```

###### find命令用于查找文件

find [查找路径] 寻找条件 操作

| 参数                 | 作用                                       |
| ------------------ | ---------------------------------------- |
| -name              | 匹配名称                                     |
| -perm              | 匹配权限（mode为完全匹配，-mode为包含即可）               |
| -user              | 匹配所有者                                    |
| -group             | 匹配所有组                                    |
| -mtime -n +n       | 匹配修改内容的时间（-n指n天以内，+n指n天以前）               |
| -atime -n +n       | 匹配访问文件的时间-n指n天以内，+n指n天以前                 |
| -ctime -n +n       | 匹配修改权限的时间-n指n天以内，+n指n天以前                 |
| -nouser            | 匹配无所有者的文件                                |
| -nogroup           | 匹配无所有组的文件                                |
| -newer f1 !f2      | 匹配比文件f1新却比f2旧的文件                         |
| --type b/d/c/p/l/f | 匹配文件类型（块设备、目录、字符设备、管道、链接文件、文件文件）         |
| -size              | 匹配文件的大小（+50k查找超过50k的文件,而-50k则代表查找小于50k的文件） |
| -prune             | 忽略某个目录                                   |
| -exec {} \;        | 后面可接对搜索到结果进一步处理的命令（下面会有演示）               |

```shell
#其中的"host*"表示所有以host开头的文件：
find /etc -name "host*" -print
#搜索整个系统中所有包含SUID的文件（因SUID的数字表示法是4，而减号表示只要包含即可）。
find / -perm -4000 -print
#找出用户linuxprobe的文件并复制到/root/findresults目录
#重点是"-exec {} \;"其中的{}代表find命令搜索出的文件，记住结尾必须是\
find / -user linuxprobe -exec cp -arf {} /root/findresults/ \;
```

#### 第3章 管道符 重定向与环境变量

##### 3.1 管道命令符

管道命令符“**|**”的作用是将前一个命令的标准输出当作是后一个命令的标准输入，格式为“命令A**|**命令B”。

将下面这两条命令进行结合：

> 找出被限制登陆用户的命令是:**grep "/sbin/nologin" /etc/passwd**
>
> 统计文本行数的命令则是:**wc -l**

```shell
grep "/sbin/nologin" /etc/passwd | wc -l
#用翻页的形式查看/etc目录中有那些文件：
ls -l /etc/ | more
#向linuxprobe用户发送一封邮件：
echo "Content" | mail -s "Subject" linuxprobe
#检查邮件
su - linuxprobex
mail
#使用非交互式设置用户密码，将root的密码修改为linuxprobe。
echo "linuxprobe" | passwd --stdin root
```

##### 3.2 输入与输出重定向

要想通过Linux命令让数据的处理更加的高效，就特别有必要搞明白输入和输出重定向的原理，简单描述即“使用输入重定向能够将文件导入到命令中，而输出重定向则是能够将原本要输出到屏幕的信息写入到指定文件中”。

重定向分为标准输出重定向和错误输出重定向：

```shell
ls ~
ls xxx/
ls: xxx: No such file or directory
```

刚刚我们先查看了~目录内的文件，后又尝试查看名为"xxx"目录内的文件，显示该目录并不存在。虽然好像命令都执行成功了，但其实有所差异，前者执行后返回的是标准输出，而后者执行失败返回的是错误输出。

> 标准输入(STDIN，文件描述符为0)：默认从键盘输入，为0时表示是从其他文件或命令的输出。
>
> 标准输出(STDOUT，文件描述符为1)：默认输出到屏幕，为1时表示是文件。
>
> 错误输出(STDERR，文件描述符为2)：默认输出到屏幕，为2时表示是文件。

[here](http://www.linuxprobe.com/chapter-03.html#32)

