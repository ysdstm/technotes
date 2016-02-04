### Register
1.Register an account on github.com with a E-mail address.  

### Create New Repository
2.Click New repository, with select **Initialize this repository with a README**.  
3.If didn't select, need to follow instuctions to create README.md.  

### Install git

	apt-get install git

### Configure git

Create local ssh key  

	ssh-keygen -t rsa -C "your_email@domain.com"

Input account name and password.  
Go to ~/.ssh, find id_rsa.pub and copy the rsa key, paste it to git-settings-SSH keys.

### Test git

	ssh -T git@github.com

### Configure commit name and email

	git config --global user.name "your name"
	git config --global user.email "your email"

### Clone git

	git clone https://github.com/username/respositoryname.git

### Modify local files

### Commit modify

	git add .
	git commit -m 'update'
	git push
