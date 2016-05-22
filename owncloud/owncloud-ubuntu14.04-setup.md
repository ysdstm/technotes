```shell
    1  apt-get install apache2 mariadb-server libapache2-mod-php5
    2  apt-get install php5-gd php5-json php5-mysql php5-curl
    3  apt-get install php5-intl php5-mcrypt php5-imagick
    4  ifconfig
    5  cd /etc/apache2/
    6  ls
    7  cd sites-available/
    8  ls
    9  cp 000-default.conf 000-default.conf.bak
   10  nano 000-default.conf
   11  touch owncloud.conf
   12  nano owncloud.conf 
   13  ln -s /etc/apache2/sites-available/owncloud.conf /etc/apache2/sites-enabled/owncloud.conf
   14  ls
   15  cd ..
   16  cd sites-enabled/
   17  ls
   18  a2enmod rewrite
   19  a2enmod headers
   20  a2enmod env
   21  a2enmod dir
   22  a2enmod mime
   23  service apache2 restart
   24  cd /home/zwinzhu/
   25  ls
   26  cp owncloud-latest.zip /var/www/oc.zip
   27  cp setup-owncloud.php /var/www/
   28  cd /var/www
   29  ls
   30  cd /etc/apache2/
   31  ls
   32  cd sites-available/
   33  ls
   34  nano 000-default.conf
   35  service apache2 restart
   36  cd /var/www
   37  chown -R www-data:www-data /var/www/
   38  ls
   39  touch info.php
   40  nano info.php 
   41  apt-get install redis php-pecl-redis
   42  apt-get install redis-server php5-redis
   43  ps ax | grep redis
   44  redis-server /h
   45  service apache2 restart
   46  cd owncloud/
   47  ls
   48  c con
   49  cd config/
   50  ls
   51  cp config.php config.php.bak
   52  nano config.php
   53  cd /etc/php5/
   54  ls
   55  cd mods-available/
   56  ls
   57  cat redis.ini 
   58  php5enmod redis
   59  service apache2 restart
   60  aptitude purge php5-redis
   61  aptitude install php-pear php5-dev
   62  pecl install redis
   63  cat readline.ini 
   64  ls
   65  echo 'extension=redis.so' > /etc/php5/mods-available/redis.ini
   66  ls
   67  php5enmod redis
   68  service apache2 restart
   69  history
```

修改文件上传大小