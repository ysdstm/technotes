#### 登录错误提示

ash: /usr/libexec/sftp-server: not found  

安装openssh-sftp-server到SD卡  
```
opkg install openssh-sftp-server -d sd
cd /usr
mkdir libexec
cd libexec
ln -s /data/UsbDisk2/Volume2/usr/libexec/sftp-server sftp-server
```

再尝试登录，能够正常登陆了  
