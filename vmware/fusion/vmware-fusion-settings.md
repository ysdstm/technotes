### VMWare Fusion 网络类型

先了解[VMware Fusion网络类型](https://kb.vmware.com/selfservice/search.do?cmd=displayKC&docType=kc&docTypeID=DT_KB_1_1&externalId=1022264)：

*  桥接网络

     虚拟机显示为主机所连接的物理网络上的另一台电脑。

     桥接网络的适配器是vmnet0，使用vmnet-bridge和vmnet-netifup服务。


* 仅主机

  虚拟机使用虚拟网络连接到主机。一般情况下，无法通过物理网络访问专用网络。

  仅主机网络适配器是vmnet1，使用vmnet-dhcpd服务。


* NAT网络

  虚拟机通过NAT访问外部网络。

  NAT网络适配器是vmnet8，使用vmnet-natd，vmnet-dhcpd和vmnet-netifup服务。


### VMWare Fusion DHCP 设置

参考修改[Fusion vmnet1和vmnet8 的 DHCP设置](https://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1026510)

修改vmnet1和`vmnet8`

> 注意：不要修改dhcp.conf文件文件，仅修改networking文件。修改如下

1. 关闭虚拟机并退出Fusion

2. 打开Terminal

3. 运行以下命令：

   ``` shell
   sudo nano /Library/Preferences/Vmware\ Fusion/networking
   #1.修改子网和子网掩码
   #2.修改配置，例如关闭NAT网络DHCP
   answer VNET_8_DHCP yes
   #修改为
   answer VNET_8_DHCP no
   #Fusion 4及以上版本，重启后配置生效
   #如果不想重启Fusion 4，执行以下命令
   sudo /Applications/VMware\ Fusion.app/Contents/Library/vmnet-cli --configure
   sudo /Applications/VMware\ Fusion.app/Contents/Library/vmnet-cli --stop
   sudo /Applications/VMware\ Fusion.app/Contents/Library/vmnet-cli --start

   ```

   ​

   ​

   ​