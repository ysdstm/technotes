#### OwnCloud简介

暂时忽略，下次再写

#### 系统选用Ubuntu Server 16.04

这里首选Ubuntu，主要是易用，owncloud官方主要推荐使用RedHat或者CentOS，主要是出于稳定性的考虑。

#### 安装过程

##### 1.搭建LAMP环境

[参考教程](https://ittutorials.net/linux/owncloud/installing-owncloud-in-ubuntu/)

######  1.1 设定静态IP地址

`nano /etc/network/interfaces`

```shell
address 192.168.x.x
netmask 255.255.255.0
gateway 192.168.x.x
dns-nameservers 8.8.8.8 8.8.4.4
```

###### 1.2 安装Apache,PHP,MySQL

通过`tasksel`安装，tasksel是Debian自带的软件安装程序，如果没有安装tasksel，首先`sudo apt-get install tasksel`

`tasksel`的界面和安装Ubuntu过程中选择组件的安装界面相同，安装LAMP甚为简单，适合新手使用。

```shell
sudo tasksel install lamp-server
#安装过程中提示设置MySQL的root密码，安装过程自动完成
```

安装之后打开`http://host-ip-address/`将显示欢迎页面。

默认的网站目录为`/var/www/html`，可以修改`/etc/apache2/sites-available/000-default.conf`配置文件，并修改`/etc/apache2/apache2.conf`中的目录权限：

```shell
#修改默认网站目录
cd /etc/apache2/sites-available
sudo cp 000-default.conf 000-default.conf.bak
sudo nano 000-default.conf
#修改为
DocumentRoot /var/www

#如果修改为其他目录还要修改目录权限
cd /etc/apache2/
sudo cp apache2.conf apache2.conf.bak

#将以下内容
<Directory /var/www/>
	Options Indexes FollowSymLinks
	AllowOverride None
	Require all granted
</Directory>
#修改为
<Directory /var/www/>
	Options FollowSymLinks
	AllowOverride None
	Require all granted
</Directory>

#重启服务生效
sudo service apache2 reload
```



###### 1.3 修改PHP文件最大上传大小限制

主要是修改php.ini中`upload_max_filesize`和`post_max_size`的大小

```shell
cd /etc/php/7.0/apache2/
sudo cp php.ini php.ini.bak
sudo nano php.ini
#Ctrl+W查找，修改为以下内容，这里设置为可以上传最大为4G大小
upload_max_filesize = 4096M
post_max_size = 4096M

#修改后执行
sudo service apache2 reload
```

##### 2.安装owncloud

###### 2.1 准备文件并安装

通过官方的简易安装方式Web Installer进行安装，首先下载`setup-owncloud.php`，到[官方下载页面](https://owncloud.org/install/#instructions-server)进行下载，或则直接点击[这里](https://download.owncloud.com/download/community/setup-owncloud.php)下载。

```shell
cd ~
mkdir owncloud
cd owncloud
wget https://download.owncloud.com/download/community/setup-owncloud.php
#在安装向导中，将自动下载最新的owncloud-latest.zip，但下载速度较慢，可以先下载https://download.owncloud.org/download/community/owncloud-latest.zip，再修改为oc.zip，与setup-owncloud.php一同放在/var/www目录下
```

拷贝下载好的文件到`/var/www`目录下

```shell
cd ~/owncloud
sudo cp setup-owncloud.php /var/www/
sudo cp owncloud-latest.zip /var/www/oc.zip
```

访问`http://ipaddress/setup-owncloud.php`，点击Next，将提示缺少依赖组件，网站目录无法写入

```
Dependency check

Dependencies not found.
The following PHP modules are required to use ownCloud:
zip
dom
XMLWriter
libxml
mb multibyte
GD
SimpleXML
curl
Please contact your server administrator to install the missing modules.
Can't write to the current directory. Please fix this by giving the webserver user write access to the directory.
```

安装依赖组件

```shell
#zip组件
sudo apt-get install php7.0-zip
#dom XMLWriter libxml SimpleXML 组件
sudo apt-get install php7.0-xml
#mb组件
sudo apt-get install php7.0-mbstring
#gd组件
sudo apt-get install php7.0-gd
#curl组件
sudo apt-get install php7.0-curl
```

修改目录权限

```shell
sudo chown -R www-data:www-data /var/www
```

继续安装，提示输入"."以安装到当前目录，或者输入owncloud，安装到`/var/www/owncloud`目录下

```
Enter a single "." to install in the current directory, or enter a subdirectory to install to:
```

这里默认点击Next，安装到owncloud目录下，将会解压oc.zip，点击Next

提示创建管理员帐号，并输入管理员密码。

指定存储数据目录，这将是同步文件的保存目录，**谨慎考虑后再选择**，默认目录是`/var/www/owncloud/data`

输入MySQL数据库的管理员帐号和密码，以及创建owncloud数据库的名称。

> 这里选择默认目录，数据库名称为owncloud

设置完毕后，将进入文件管理页面，生成的配置文件保存在`/var/www/owncloud/config/config.php`中

###### 2.2 查看owncloud数据库

由于使用了mysql数据库，在不安装phpMyAdmin的情况下，只能使用命令行查看

```shell
#连接数据库
mysql -u root -p
#查看数据库
show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| owncloud           |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.01 sec)

use owncloud;
show tables;
+-----------------------------+
| Tables_in_owncloud          |
+-----------------------------+
| oc_activity                 |
| oc_activity_mq              |
| oc_addressbookchanges       |
| oc_addressbooks             |
| oc_appconfig                |
| oc_calendarchanges          |
| oc_calendarobjects          |
| oc_calendars                |
| oc_calendarsubscriptions    |
| oc_cards                    |
| oc_cards_properties         |
| oc_comments                 |
| oc_comments_read_markers    |
| oc_credentials              |
| oc_dav_shares               |
| oc_file_locks               |
| oc_filecache                |
| oc_files_trash              |
| oc_group_admin              |
| oc_group_user               |
| oc_groups                   |
| oc_jobs                     |
| oc_mimetypes                |
| oc_mounts                   |
| oc_notifications            |
| oc_preferences              |
| oc_privatedata              |
| oc_properties               |
| oc_schedulingobjects        |
| oc_share                    |
| oc_share_external           |
| oc_storages                 |
| oc_systemtag                |
| oc_systemtag_object_mapping |
| oc_trusted_servers          |
| oc_users                    |
| oc_vcategory                |
| oc_vcategory_to_object      |
+-----------------------------+
38 rows in set (0.00 sec)
```

###### 2.3 备份owncloud数据库

注意-p参数与密码之间没有空格

```shell
sudo mysqldump --lock-tables -h localhost -u root -p[password] owncloud > owncloud-sqlbackup_`date +"%Y%m%d"`.bak
```

###### 2.4 安装客户端

安装图形客户端很简单，先说一下怎样安装命令行客户端，安装方法可以[参考](https://software.opensuse.org/download/package?project=isv:ownCloud:desktop&package=owncloud-client)这个页面，这里主要是安装Ubuntu的客户端，对于16.04

```shell
#添加源
sudo sh -c "echo 'deb http://download.opensuse.org/repositories/isv:/ownCloud:/desktop/Ubuntu_16.04/ /' >> /etc/apt/sources.list.d/owncloud-client.list"
#添加信任密钥
wget http://download.opensuse.org/repositories/isv:ownCloud:desktop/Ubuntu_16.04/Release.key
sudo apt-key add - < Release.key
#更新源并安装
sudo apt-get update
sudo apt-get install owncloud-client
#安装完成后，只有两个命令，在没有桌面图形的情况下，只能使用owncloudcmd
owncloud     owncloudcmd
#同步文件，例如同步home目录
owncloudcmd -u [username] -p [password] ~/ http://localhost/owncloud/remote.php/webdav/home/zwinzhu
```

安装时提示需要安装以下组件

```shell
sudo apt-get install owncloud-client
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  fontconfig gstreamer1.0-plugins-base libavahi-client3 libavahi-common-data libavahi-common3 libcdparanoia0 libcups2
  libdouble-conversion1v5 libdrm-amdgpu1 libdrm-intel1 libdrm-nouveau2 libdrm-radeon1 libegl1-mesa libevdev2 libgbm1
  libgl1-mesa-dri libgl1-mesa-glx libglapi-mesa libgraphite2-3 libgstreamer-plugins-base1.0-0 libgstreamer1.0-0
  libgudev-1.0-0 libharfbuzz0b libice6 libinput10 libllvm3.8 libmtdev1 libogg0 libopus0 liborc-0.4-0 libowncloudsync0
  libpciaccess0 libpcre16-3 libproxy1v5 libqt5core5a libqt5dbus5 libqt5gui5 libqt5keychain0 libqt5network5
  libqt5opengl5 libqt5printsupport5 libqt5qml5 libqt5quick5 libqt5sql5 libqt5sql5-sqlite libqt5svg5 libqt5webkit5
  libqt5widgets5 libqt5xml5 libsm6 libtheora0 libtxc-dxtn-s2tc0 libvisual-0.4-0 libvorbis0a libvorbisenc2
  libwacom-bin libwacom-common libwacom2 libwayland-client0 libwayland-server0 libx11-xcb1 libxcb-dri2-0
  libxcb-dri3-0 libxcb-glx0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-present0 libxcb-randr0
  libxcb-render-util0 libxcb-render0 libxcb-shape0 libxcb-shm0 libxcb-sync1 libxcb-util1 libxcb-xfixes0 libxcb-xkb1
  libxcomposite1 libxdamage1 libxfixes3 libxi6 libxkbcommon-x11-0 libxkbcommon0 libxrender1 libxshmfence1 libxxf86vm1
  owncloud-client-l10n qttranslations5-l10n x11-common
Suggested packages:
  gvfs cups-common libvisual-0.4-plugins gstreamer1.0-tools opus-tools libthai0 libqt5libqgtk2
  qt5-image-formats-plugins qtwayland5
The following NEW packages will be installed:
  fontconfig gstreamer1.0-plugins-base libavahi-client3 libavahi-common-data libavahi-common3 libcdparanoia0 libcups2
  libdouble-conversion1v5 libdrm-amdgpu1 libdrm-intel1 libdrm-nouveau2 libdrm-radeon1 libegl1-mesa libevdev2 libgbm1
  libgl1-mesa-dri libgl1-mesa-glx libglapi-mesa libgraphite2-3 libgstreamer-plugins-base1.0-0 libgstreamer1.0-0
  libgudev-1.0-0 libharfbuzz0b libice6 libinput10 libllvm3.8 libmtdev1 libogg0 libopus0 liborc-0.4-0 libowncloudsync0
  libpciaccess0 libpcre16-3 libproxy1v5 libqt5core5a libqt5dbus5 libqt5gui5 libqt5keychain0 libqt5network5
  libqt5opengl5 libqt5printsupport5 libqt5qml5 libqt5quick5 libqt5sql5 libqt5sql5-sqlite libqt5svg5 libqt5webkit5
  libqt5widgets5 libqt5xml5 libsm6 libtheora0 libtxc-dxtn-s2tc0 libvisual-0.4-0 libvorbis0a libvorbisenc2
  libwacom-bin libwacom-common libwacom2 libwayland-client0 libwayland-server0 libx11-xcb1 libxcb-dri2-0
  libxcb-dri3-0 libxcb-glx0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-present0 libxcb-randr0
  libxcb-render-util0 libxcb-render0 libxcb-shape0 libxcb-shm0 libxcb-sync1 libxcb-util1 libxcb-xfixes0 libxcb-xkb1
  libxcomposite1 libxdamage1 libxfixes3 libxi6 libxkbcommon-x11-0 libxkbcommon0 libxrender1 libxshmfence1 libxxf86vm1
  owncloud-client owncloud-client-l10n qttranslations5-l10n x11-common
0 upgraded, 90 newly installed, 0 to remove and 0 not upgraded.
Need to get 41.4 MB of archives.
After this operation, 260 MB of additional disk space will be used.
Do you want to continue? [Y/n] 
```

##### 3.其他

###### 3.1 关于Version Control

owncloud的文件版本可以参考[官方用户手册](https://doc.owncloud.org/server/9.0/user_manual/files/version_control.html)，根据手册中的描述，owncloud的文件版本控制是简单的版本控制。

owncloud支持回收站和文件版本，是使用owncloud的最主要原因之一。

**回收站**很简单，用户无论是删除了本地文件还是通过网页客户端删除了文件，都将被存放到回收站中。但首次同步时仍需小心，防止删除了未同步过的文件。

**文件版本**需要重点了解一下。以下是手册中的原文。

文件版本app（在owncloud可以通过启用和添加app，来达到更多的功能）自动控制旧版本文件以防止用户文件超出存储空间。这个模式是用于删除旧的文件版本：

* 过去的每秒内，保存一个版本
* 在前10秒内，保留每2秒的文件版本
* 过去的1分钟内，保留每10秒的文件版本
* 过去的1个小时内，保留每1分钟的文件版本
* 过去的24小时内，保留每1小时的文件版本
* 过去的30天内，保留每1天的文件版本
* 超过30天后，保留每周的文件版本

文件版本随着每个新的文件版本被创建而使用以上模式

文件版本app不会使用超过用户当前剩余空间的50%，如果超过了这个界限，ownCloud将删除最早的版本，直到满足磁盘空间的限制要求。

> 实际测试中，owncloud还是能够很好地保存不同版本的文件的。

```
The versioning app expires old versions automatically to make sure that the user doesn’t run out of space. This pattern is used to delete old versions:

For the first second we keep one version
For the first 10 seconds ownCloud keeps one version every 2 seconds
For the first minute ownCloud keeps one version every 10 seconds
For the first hour ownCloud keeps one version every minute
For the first 24 hours ownCloud keeps one version every hour
For the first 30 days ownCloud keeps one version every day
After the first 30 days ownCloud keeps one version every week
The versions are adjusted along this pattern every time a new version gets created.

The version app never uses more that 50% of the user’s currently available free space. If the stored versions exceed this limit, ownCloud deletes the oldest versions until it meets the disk space limit again.
```

##### 4.启用Memcache

参见[官方手册](https://doc.owncloud.org/server/9.0/admin_manual/configuration_server/caching_configuration.html#id4)，在第一次配置时，以为16.06上的PHP7.0无法支持，后来又尝试了一下，可以安装。

```shell
apt-get install redis-server
apt-get install php-redis
#检查redis-server是否已运行
ps ax | grep redis
#检查一下php7.0的redis模块是否启用
cd /etc/php/7.0/mods-available/
cat redis.ini
#检查是否有以下行
extension=redis.so
#执行以下命令，或者查看phpinfo()
php --ri redis

redis

Redis Support => enabled
Redis Version => 2.2.8-devphp7
#重启apache2
service apache2 restart
#配置owncloud目录下的config.php
nano config.php
#添加以下内容，并启用文件缓存锁定
  'memcache.local' => '\OC\Memcache\Redis',
  'filelocking.enabled' => 'true',
  'memcache.locking' => '\OC\Memcache\Redis',
  'redis' => array(
        'host' => 'localhost',
        'port' => 6379,
        ),
```

配置完成后，登录owncloud，进入Admin页面检查是否有错误。

