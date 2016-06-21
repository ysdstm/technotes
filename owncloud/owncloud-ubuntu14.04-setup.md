#### Ubuntu14.04安装owncloud

##### 1. 安装Lamp环境

先参考[官方手册](https://doc.owncloud.org/server/9.0/admin_manual/installation/source_installation.html#example-installation-on-ubuntu-14-04-lts-server)，搭建Lamp环境，数据库使用的是Mariadb

```shell
#安装过程中，需要配置数据库root密码
apt-get install apache2 mariadb-server libapache2-mod-php5
apt-get install php5-gd php5-json php5-mysql php5-curl
apt-get install php5-intl php5-mcrypt php5-imagick
#配置虚拟目录
cd /etc/apache2/sites-available/
touch owncloud.conf
nano owncloud.conf
#输入以下内容
Alias /owncloud "/var/www/owncloud/"

<Directory /var/www/owncloud/>
  Options +FollowSymlinks
  AllowOverride All

 <IfModule mod_dav.c>
  Dav off
 </IfModule>

 SetEnv HOME /var/www/owncloud
 SetEnv HTTP_HOME /var/www/owncloud

</Directory>
#创建软链接
ln -s /etc/apache2/sites-available/owncloud.conf /etc/apache2/sites-enabled/owncloud.conf

#配置Apache
#必须启用mod_rewrite
a2enmod rewrite
#启用其他模块
a2enmod headers
a2enmod env
a2enmod dir
a2enmod mime
#其他配置详见手册
#修改文件上传大小限制
cd /etc/php5/apache2
cp php.ini php.ini.bak
#修改以下内容，最好根据实际情况进行测试
upload_max_filesize = 4096M
max_file_uploads = 50
post_max_size = 4096M
max_execution_time = 3600
max_input_time = 3600
memory_limit = 512M
#重启Apache服务
service apache2 restart
```

##### 2.安装owncloud

```shell
#将准备好的安装向导文件setup-owncloud.php和最新的owncloud包拷贝到/var/www目录
cp owncloud-latest.zip /var/www/oc.zip
cp setup-owncloud.php /var/www/
#配置目录权限
chown -R www-data:www-data /var/www/
```
接下来到浏览器上操作

##### 3.配置Memcache

按照[官方手册](https://doc.owncloud.org/server/9.0/admin_manual/configuration_server/caching_configuration.html#id4)中安装`redis-server`和`php5-redis`，最后不成功，Admin页面显示

> Memcache \OC\Memcache\Redis not available for local cache Is the matching PHP module installed and enabled?

到论坛上[参考](https://forum.owncloud.org/viewtopic.php?t=31993)这个解决方法

```shell
#以下命令无法正确安装
#apt-get install redis-server php5-redis
#如果已安装，清除php5-redis
aptitude purge php5-redis
#使用pecl安装redis扩展
aptitude install php-pear php5-dev
pecl install redis
#添加扩展
echo 'extension=redis.so' > /etc/php5/mods-available/redis.ini
#启用redis
php5enmod redis
#重启apache服务
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

