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
