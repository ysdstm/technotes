#### 准备工作

```
su
mkdir ~/temp
cd temp
wget http://python.org/ftp/python/2.7.3/Python-2.7.3.tar.bz2
#解压
tar -jxvf Python-2.7.3.tar.bz2
#安装openssl
yum install openssl-devel
#开启ssl
vi Python-2.7.3/Modules/Setup.dist
#修改为以下内容
# Socket module helper for socket(2)
_socket socketmodule.c

# Socket module helper for SSL support; you must comment out the other
# socket line above, and possibly edit the SSL variable:
#SSL=/usr/local/ssl
_ssl _ssl.c \
        -DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
        -L$(SSL)/lib -lssl -lcrypto
```

#### 安装Python

```
./configure
make all
make install
make clean
make distclean
```

#### 查看安装的Python版本
```
/usr/local/bin/python2.7 -V
```

#### 备份python2.6

```
cd /usr/bin
ls python*
#查看是否有python2.6，若没有
mv /usr/bin/python /usr/bin/python2.6
ln -s /usr/local/bin/python2.7 /usr/bin/python
```

#### 防止yum无法工作

```
vim /usr/bin/yum
#将第1行修改为
#!/usr/bin/python2.6
```

#### 安装easy_install

```
wget https://pypi.python.org/packages/source/s/setuptools/setuptools-15.2.tar.gz#md5=a9028a9794fc7ae02320d32e2d7e12ee
tar -xzvf setuptools-15.2.tar.gz
cd setuptools-15.2
python setup.py install
```

#### 安装最新版easy_install

```
wget https://bootstrap.pypa.io/ez_setup.py
python ez_setup.py
easy_install --version
```


#### 安装pip

```
easy_install pip
#或者
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
```

