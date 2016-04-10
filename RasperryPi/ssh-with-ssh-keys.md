#### check exist ssh keys

	ls ~/.ssh

If you see files name with `id_rsa` and `id_rsa.pub`, you have keys set up already.  
You can skip the generating keys step.  
Just goto step 2.  
Or create new keys.  

Or you can generate new ssh keys.  

#### 1. generate new ssh keys

On your local computer, execute follow commands:  

	ssh-keygen -t rsa -C yourname@yourdevice

While asked `Enter file in which to save the key (/Users/zwinzhu/.ssh/id_rsa):`  
Input new key name, such as "pi", input password to protect the keys or skip it.  
 
#### 2. copy public key to raspberry pi

ssh to pi, check folder .ssh ever exists, if not:  

	mkdir .ssh
	chmod 700 .ssh
	touch authorized_keys
	chmod 600 authorized_keys

copy content of id_rsa.pub or your new public key pi.pub, and paste to authorized_keys  

or on your computer,execute:  

	cat ~/.ssh/id_rsa.pub | ssh pi@pi-address 'cat >> .ssh/authorized_keys'
	or
	cat ~/.ssh/pi.pub | ssh pi@pi-address 'cat >> .ssh/authorized_keys'

#### 3. ssh to pi without password

if you use id_rsa key to login,just  

	ssh pi@pi-address

or if you use new key name with "pi":  

	ssh pi@pi_address -i ~/.ssh/pi
