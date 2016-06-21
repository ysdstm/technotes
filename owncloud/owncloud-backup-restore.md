#### 备份和恢复owncloud

无论是什么数据，备份很重要，在故障发生之前，先模拟一下数据迁移，当故障真的发生了，可以迅速转移数据库和文件。

备份数据[参考](https://doc.owncloud.org/server/9.0/admin_manual/maintenance/restore.html)官方手册，需要备份3个地方：配置目录，数据目录，owncloud数据库

###### 1.备份owncloud

备份owncloud网页目录和数据目录到另外的存储中

```shell
rsync -Aax owncloud/ owncloud-bkpdir_`date + "%Y%m%d"`/
```

备份owncloud mysql数据库

```shell
mysqldump --lock-tables -h [server] -u [username] -p[password] [db_name] > owncloud-sqlbkp_`date + "%Y%m%d"`.bak
```

###### 2.恢复owncloud

恢复owncloud网页目录和数据目录

```shell
rsync -Aax owncloud-dirbkp/ owncloud/
```

恢复数据库

```sync
mysql -h [server] -u [username] -p[password] [db_name] < owncloud-sqlbkp.bak
```

##### 备份和恢复实战

###### 1.环境介绍

原主机情况简介：

系统：Ubuntu 16.04 安装于物理主机

数据库：Mysql

IP地址：192.168.1.134

数据物理路径：/dev/sdb1 挂载在 /mnt/databackup

网页及数据目录：/mnt/databackup/www和/mnt/databackup/www/data



新主机情况简介：

系统：Ubuntu 14.04 安装于VMWare

数据库：Mariadb

IP地址：192.168.228.146

数据路径：/var/www/owncloud/data

###### 1.1准备工作

将所有owncloud客户端退出，备份owncloud数据库，按照官方的指示，应该先进入[维护模式](https://doc.owncloud.org/server/9.0/admin_manual/maintenance/index.html)

```shell
mysqldump --lock-tables -h localhost -u root -p[password] owncloud > owncloud-sqlbackup_`date +"%Y%m%d"`.bak
```

在安装时，将网页目录和数据目录都放在了第二块硬盘上，数据目录使用了默认路径`owncloud/data`

由于新环境中，主机ip地址和原来的主机地址不一样，数据库也已安装好，owncloud在安装时创建了mysql用户oc_admin，两个环境中oc_admin的密码也不一样，数据库中有些条目记录了原主机的ip地址信息

> 看来只能也只要恢复owncloud数据库，和数据目录就可以了，配置文件使用新主机的配置文件，修改一下数据目录

###### 2.备份新主机数据库和配置文件

```shell
cd /var/www/owncloud_data
mysqldump --lock-tables -h localhost -u root -p[password] owncloud > owncloud-sqlbackup_`date +"%Y%m%d"`.bak

cd /var/www/owncloud/config
cp config.php config.php.bak2
```

###### 3.恢复旧主机的owncloud数据库

```shell
cd /mnt/databackup/owncloud_data/
mysql -u root -p[password] owncloud < owncloud-sqlbackup_20160523.bak

cd /var/www/owncloud/config
#修改数据目录
nano config.php
'datadirectory' => '/mnt/databackup/www/owncloud/data',
```

###### 3.登录并测试

无需重启服务，使用原环境中的帐号登录，查看文件是否可以正常下载。下载客户端很慢只能绕道下载了，曲线救国你懂的

```shell
wget --no-check-certificate https://download.owncloud.com/desktop/stable/ownCloud-2.2.0.3358.pkg -4
```



###### 4.迁移结果

经过测试，可以正常下载和同步上传文件

既然上传了文件，本应该备份迁移测试的数据库，并还原到原原主机上，但万不得已，也不会迁移主机，就不恢复数据库了，只能把上传的文件删除，文件在数据库中没有记录，也无法同步和下载，网页中也不会显示。

###### 5.恢复模拟环境

```shell
cd /var/www/owncloud_data/
mysql -u root -p[password] owncloud < owncloud-sqlbackup_20160523.bak

cd /var/www/owncloud/config
#修改数据目录
nano config.php
'datadirectory' => '/var/www/owncloud/data',

#重新打开网页，竟然是500错误，配置都没有改变，只能修改下用户和用户组了
chown -R www-data:www-data /var/www
#修复后，能够正常显示了
```

