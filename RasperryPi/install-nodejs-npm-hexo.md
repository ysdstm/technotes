#### Install Node.js v4.* without comply

see `http://blog.wia.io/installing-node-js-v4-0-0-on-a-raspberry-pi/`  

##### for Raspberry Pi Model A, B, B+

##### for Raspberry Pi 2 Model B

goto `https://nodejs.org/en/download/`  
check ARMv7 version  

	wget https://nodejs.org/dist/v4.2.6/node-v4.2.6-linux-armv7l.tar.xz
	xz -d node-v4.2.6-linux-armv7l.tar.xz
	tar xvf node-v4.2.6-linux-armv7l.tar
	cd node-v4.2.6-linux-armv7l/
	sudo cp -R * /usr/local/

check  

	node -v
	npm -v


##### Install hexo

	sudo npm install hexo -g
	or
	sudo npm install --unsafe-perm --verbose -g hexo
	mkdir hexo
	hexo init hexo
	cd hexo
	npm install --save
	npm install hexo-server --save
	npm generate
	npm server

#### Install Node.js with comply

see `http://andyfelong.com/2015/11/node-js-v4-1-0-on-raspberry-pi-2/`  

> Need gcc/g++ version 4.8 or better, need to upgrade Wheezy or use Jesse  

##### Build Node.js on Rasbian Jesse

check `https://nodejs.org/en/download/`, download `Source Code`  

	wget https://nodejs.org/dist/v4.2.6/node-v4.2.6.tar.gz
	tar -xzf node-v4.2.6.tar.gz
	cd node-v4.2.6
	./configure
	make
	sudo make install


