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

通过官方的简易安装方式Web Installer进行安装，首先下载`setup-owncloud.php`，到[官方下载页面](https://owncloud.org/install/#instructions-server)进行下载，或则直接点击[这里](https://download.owncloud.com/download/community/setup-owncloud.php)下载。

```shell
cd ~
mkdir owncloud
cd owncloud
wget https://download.owncloud.com/download/community/setup-owncloud.php
#在安装向导中，将自动下载最新的owncloud-latest.zip，但下载速度较慢，可以先下载https://download.owncloud.org/download/community/owncloud-latest.zip，再修改为oc.zip，与setup-owncloud.php一同放在/var/www目录下
```



