#### ping: icmp open socket: Operation not permitted

ping命令在运行中采用了ICMP协议，需要发送ICMP报文。但是只有root用户才能建立ICMP报文。而正常情况下，ping命令的权限应为-rwsr-xr-x，即带有suid的文件，一旦该权限被修改，则普通用户无法正常使用该命令。

	pi@raspberrypi2:~ $ ping www.baidu.com
	ping: icmp open socket: Operation not permitted

	sudo -i
	chmod u+s /bin/ping

#### modify host name

	sudo nano /etc/hostname
	sudo nano /etc/hosts

#### install shadowsocks server

	1.install pip
	apt-get install python-pip python-gevent python-m2crypto

	2.install shadowsocks
	pip install shadowsocks
	
	3.create config file /etc/shadowsocks.json:
	{
		"server":"0.0.0.0",
		"server_port":22333,
		"local_address":"127.0.0.1",
		"local_port":1080,
		"password":"passwordhere",
		"timeout":300,
		"method":"aes-256-cfb",
		"fast_open":false,
		"workers":1
	}

	4.start server
	nohup ssserver -c /etc/shadowsocks.json &

	5.set auto startup
	写入 nohup ssserver -c /etc/shadowsocks.json & 到 /etc/rc.local 文件的exit之前 

#### pptp client
	
	check `https://wiki.archlinux.org/index.php/PPTP_Client`
	
	sudo apt-get install pptp-linux
	
	quick-setup
	pptpsetup --create VPNNAME --server VPNSERVER --username USERNAME --password PASSWORD --encrypt
	check config file
	/etc/ppp/peers/VPNNAME
	
	connect
	pon VPNNAME
	ifconfig to check ppp0 connection

	disconnect
	poff VPNNAME

	debug
	pon VPNNAME debug dump logfd 2 nodetach
	if everything has been configured correctly, the pon command should not terminate itself.
	and if connect successfully, terminate this pon

	routing
	
	split tunneling
	ip route add 192.168.10.0/24 dev ppp0
	all the trafic with a destination of 192.168.10.* through your VPN interface ppp0

	route all traffic
	ip route add default dev ppp0
	
	anymore, please check this wiki
