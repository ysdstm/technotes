#### 参考文章

http://www.jslink.org/openwrt/openwrt-rc-local-for-sdcard.html

#### 挂载SD卡

下载宝的SD插槽是用来自动备份SD卡到移动硬盘或者U盘的，插入SD卡便自动挂载，SD卡本来是树莓派上用的，有两个分区，想用fdisk重新分区的，但是openwrt的fdisk太精简，只能先用两个分区了，另一个分区是vfat，和其他系统交换文件也方便 

自动挂载： 

	/dev/mmcblk0p1          239.2M     20.5M    218.7M   9% /data/UsbDisk2/Volume1
	/dev/mmcblk0p2            3.3G      7.8M      3.1G   0% /data/UsbDisk2/Volume2

200多M，比自带存储还多些，足够了

#### 修改软件源

本来尝试用openwrt.org上的源，但是不适配，今天解压了pandorabox的固件，发现都是14.09的版本，在网站上也找到了源  
`http://downloads.pandorabox.org.cn/pandorabox/ralink/mt7621/packages/base/`  

尝试了一下，合适  

`vi /etc/opkg.conf`  

	dest root /
	dest sd /data/UsbDisk2/Volume2
	dest ram /tmp
	lists_dir ext /var/opkg-lists
	option overlay_root /overlay
	src/gz 14.09_base http://downloads.pandorabox.org.cn/pandorabox/ralink/mt7621/packages/base
	#src/gz 14.09_base http://downloads.openwrt.org/snapshots/trunk/ralink/packages/base
	# src/gz 14.09_packages http://downloads.openwrt.org/snapshots/trunk/ralink/packages/packages
	# src/gz 14.09_routing http://downloads.openwrt.org/snapshots/trunk/ralink/packages/routing
	# src/gz 14.09_telephony http://downloads.openwrt.org/snapshots/trunk/ralink/packages/telephony
	# src/gz 14.09_management http://downloads.openwrt.org/snapshots/trunk/ralink/packages/management
	# src/gz 14.09_oldpackages http://downloads.openwrt.org/snapshots/trunk/ralink/packages/oldpackages

增加了以下行`dest sd /data/UsbDisk2/Volume2`，等下可以装到SD卡，发现也可以装到`/tmp`，但重启后会丢失   

可以把包全部下载，使用本地源，但是xzb默认的http服务有问题，有时间再来鸟你  

	#使用本地源
	src/gz PandoraBox http://127.0.0.1/packages

#### 配置系统环境

注意有STORAGE和$STORAGE字样的都是新增加的，增加了可执行文件的路径和库的路径  
修改完成后，重新初始化环境变量`source /etc/profile`

	vi /etc/profile
	
	#!/bin/sh
	[ -f /etc/banner ] && cat /etc/banner
	
	export STORAGE=/data/UsbDisk2/Volume2
	export PATH=/usr/bin:/usr/sbin:/bin:/sbin:$STORAGE/bin:$STORAGE/sbin:$STORAGE/usr/bin:$STORAGE/usr/sbin
	export LD_LIBRARY_PATH=/lib:/usr/lib:$STORAGE/lib:$STORAGE/usr/lib
	export HOME=$(grep -e "^${USER:-root}:" /etc/passwd | cut -d ":" -f 6)
	export HOME=${HOME:-/root}
	#export PS1='\u@\h:\w\$ '
	export PS1='[\[\033[35;1m\]\u\[\033[0m\]@\[\033[31;1m\]\h\[\033\[0m\]:\[\033[32;1m\]$PWD\[\033[0m\]]\$'
	
	[ -x /bin/more ] || alias more=less
	[ -x /usr/bin/vim ] && alias vi=vim || alias vim=vi
	
	[ -z "$KSH_VERSION" -o \! -s /etc/mkshrc ] || . /etc/mkshrc
	
	[ -x /usr/bin/arp ] || arp() { cat /proc/net/arp; }
	[ -x /usr/bin/ldd ] || ldd() { LD_TRACE_LOADED_OBJECTS=1 $*; }
	
	alias df='df -h'
	alias free='free -m'
	#alias ls='ls -hF --color=auto'
	alias ll='ls -alh'
	alias la='ll -A'
	#alias top='top -d1'

#### 安装到外置SD卡

	opkg install tcpdump -d sd

#### 需要自启动的还要参考文章