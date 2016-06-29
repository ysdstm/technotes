### Windows Server 2008 配置DHCP

[参考](http://wenku.baidu.com/link?url=7WAiIQ5SINoe8Wszi3foC5_k0jSxigwJtgPgoLFcKzHlnw4Mx6JoLyGHKLVTo16qS7ziXyxs1BxnuwsOUpXLtTieaCevHOtn-VJvkkxpF37)

1. 打开管理工具-服务器管理器-角色

2. 添加角色

   点击下一步，选择DHCP服务器，点击下一步

   ​

   * 网络连接绑定，选择网络连接，一般只有一块网卡，则只有一个网络连接，点击下一步
   * IPv4 DNS 设置，在已加入域的情况下，父域及首选DNS服务器IPv4地址默认已填好，点击下一步
   * IPv4 WINS设置，WINS服务器先跳过设置，点击下一步
   * DHCP 作用域，添加作用域，点击添加，作用域名称例如AMC，设置起始及结束IP地址，例如192.168.1.101-192.168.1.200，以及子网掩码255.255.255.0，默认网关192.168.1.254，其他默认，点击下一步
   * DHCPv6无状态模式，IPv6设置，选择对此服务器禁用DHCPv6无状态模式，点击下一步
   * DHCP服务器授权，选择使用当前凭据，点击下一步
   * 点击安装


1. 打开管理工具-DHCP，查看配置，检查是否正常运行
2. 打开客户机，自动获取IP，检查是否能正常获取，网络是否正常工作
3. 打开DHCP服务器，检查地址租用


### Windows Server 2008 迁移DHCP

#### 操作界面模式

1. 打开管理工具-DHCP
2. 在DHCP服务器上点击右键，点击备份，默认备份路径为C:\Windows\System32\dhcp\backup
3. 在新服务器上安装DHCP服务
4. 在新DHCP服务器上点击右键，点击还原，选择备份文件夹

#### 命令行模式

参考微软[官方KB](https://support.microsoft.com/en-us/kb/962355)以及该[博客](https://blogs.technet.microsoft.com/networking/2008/06/27/steps-to-move-a-dhcp-database-from-a-windows-server-2003-or-2008-to-another-windows-server-2008-machine/)

1. 以管理员身份登录服务器
2. 以管理员身份运行cmd
3. 输入`netsh dhcp server export C:\dhcp.txt all`，回车
4. 拷贝导出的DHCP数据库文件到新的服务器上
5. 在新服务器上安装DHCP角色
6. 停止新服务器上的DHCP服务，打开cmd，输入`net stop dhcpserver`，或者打开DHCP，在服务器上点右键，回车
7. 删除新服务器上的C:\windows\system32\dhcp\dhcp.mdb文件
8. 开启新服务器上的DHCP服务
9. 在cmd中输入`netsh dhcp server import C:\dhcp.txt`
10. 重启DHCP，检查数据库是否正常转移
以上经实际测试，可行