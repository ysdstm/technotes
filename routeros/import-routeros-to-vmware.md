#### 下载RouterOS VM文件

已保存到百度云  
下载后用VMware打开或者导入  

#### 登录并配置IP地址

输入用户名admin，密码为空，登录  
查看网络接口  
`interface print`  
进入网络接口配置模式  
`ip address`  
设置网卡1(ether1)的IP地址  
`add address 192.168.2.254/24 interface ether1`  
查看网络接口设置  
/ip `address print`  

#### 通过浏览器登录

打开`http://192.168.2.254`  
