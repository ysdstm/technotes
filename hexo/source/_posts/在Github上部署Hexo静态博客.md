title: 在Github上部署Hexo静态博客
date: 2016-02-04 16:11:06
tags: [hexo,github]
---

#### 注册github帐号并建立仓库

**重要:**使用Github Page搭建博客, 需要遵循一定的规则, 需要在github建立仓库,仓库名为Github用户.github.io   

#### 安装brew

在Mac上通过[brew](http://brew.sh/)安装`git`和`npm`  
安装`brew`的命令如下:  

	/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

#### 安装 Node.js

	brew install node
	验证是否安装成功
	node -v
	npm -v

#### 安装Hexo

	nom install hexo -g
	-g 表示全局安装

#### 配置Hexo

	mkdir hexo
	hexo init hexo
	cd hexo
	npm install -g
	hexo generate
	hexo server

#### 添加文章

	hexo new "PostName"
	#新建文章，名称为PostName
	#自动生成 source/_post/postName.md
	#文件自动格式：
	title: hello
	date: 2016-02-04 14:14:45
	tags: #多标签格式为 [Tag1,Tag2]
	---
	
	#添加阅读全文，并影藏部分内容
	添加<!--more-->

#### 更换主题

	在博客根目录下克隆主题
	git clone https://github.com/wuchong/jacman.git themes/jacman
	启用主题，修改根目录下_config.yml，theme: jacman
	注意空格
	
	查看效果：
	hexo g
	hexo s

#### 配置主题

参见jacman[配置指南](https://github.com/wuchong/jacman/wiki/配置指南)或者[如何使用](http://wuchong.me/blog/2014/11/20/how-to-use-jacman/)

#### 部署到Github

修改_config.yml配置文件，使用编辑器而不是notepad修改  
修改以下内容:

	# Deployment
	## Docs: http://hexo.io/docs/deployment.html
	deploy:
	  type: git
	  repository: git@github.com:zwinzhu/zwinzhu.github.io.git
	  branch: master

执行安装

	npm install hexo-deployer-git --save
	
生成静态网页并上传

	hexo generate
	hexo deploy
	
#### 删除文章

	进入 resource/_post/目录，删除不需要的.md文件
	重新生成并上传