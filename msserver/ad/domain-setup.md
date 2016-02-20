#### 创建域

更改计算机名称  
设置固定IP，运行->dcpromo，一路下一步即可  

#### 修改域控制器名称

悲剧！忘记修改计算机明，又不想重装系统  
参考`http://freemanluo.blog.51cto.com/636588/498907/`

例如原名称是WIN-LB8MTVXI17V.DOMAIN.LOCAL  
简单概括：  
查看  
netdom computername WIN-LB8MTVXI17V.DOMAIN.LOCAL /enumerate  
增加  
netdom computername WIN-LB8MTVXI17V.DOMAIN.LOCAL /add:DCO1.DOMAIN.LOCAL  
提升  
netdom computername WIN-LB8MTVXI17V.DOMAIN.LOCAL /makeprimary:DC01.DOMAIN.LOCAL  
重启服务器  
删除
netdom computername DC01.DOMAIN.LOCAL /remove:WIN-LB8MTVXI17V.DOMAIN.LOCAL  
打开DNS管理器，进入DOMAIN.LOCAL，删除旧的主机名解析WIN-LB8MTVXI17V.DOMAIN.LOCAL，检查其他项目是否都已改成DC01.DOMAIN.LOCAL  
打开AD用户和计算机，查看Domain Controllers是否为DC01  
打开AD站点和服务，查看Default-First-Site-Name -> Servers 是否为DC01  

#### 创建第一个域用户

打开管理工具->组策略管理->计算机配置->Windows设置->安全设置->账户策略->密码策略  
将`密码必须符合复杂性要求`禁用，密码长度最小值改为0，修改其他选项  
在cmd中执行gpupdate /force  

创建OU，创建域帐号，可以使用简单密码  
