#### quit trend

方法一：  
关于卸载客户端需要密码的问题，可以通过下面的操作重置卸载密码，使用重置后的密码进行卸载：  
1.进入 ..\TrendMicro\OfficeScan Client 目录  
 
2.用记事本打开ofcscan.ini  
 
3.找到"[INI_CLIENT_SECTION]"部分  
 
4.将"Uninstall_Pwd"值改为：  
!CRYPT!5237C1A1888FAFC830342D0AB1AD8410C995F3E7C1FBB9FE857C7B1FEBE9F84A93A1B9CEF52810DBA9649332838  

5.保存文件后，Officescan客户端的卸载密码将变为"novirus"  

使用脚本删除officescan客户机  

 
方法二：  
1.打开注册表表编辑器  

2.进入HKLM\Software\TrendMicro\PCCillinNTCorp\CurrentVersion\Misc  

3.将以下2个键值的“0”改成“1”  
NoPwdProtect=1  
Allow Uninstall=1  
 
4.关闭注册表编辑器  
	
	!CRYPT!5237C1A1888FAFC830342D0AB1AD8410C995F3E7C1FBB9FE857C7B1FEBE9F84A93A1B9CEF52810DBA9649332838
	novirus
