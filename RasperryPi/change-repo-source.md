#### Find Raspbian Mirrors

visit `https://www.raspbian.org/RaspbianMirrors`  

find Aisa China source, e.g. Zhejiang University `https://www.raspbian.org/RaspbianMirrors`  

#### Update repo source

	#backup
	sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
	#edit
	sudo nano /etc/apt/sources.list

update sources.list

	deb http://mirrors.zju.edu.cn/raspbian/raspbian/ jessie main contrib non-free rpi
	# Uncomment line below then 'apt-get update' to enable 'apt-get source'
	#deb-src http://archive.raspbian.org/raspbian/ jessie main contrib non-free rpi	

	#Update and Upgrade 
	sudo apt-get update
	sudo apt-get upgrade
