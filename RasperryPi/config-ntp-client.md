#### Install ntp client

	sudo apt-get install ntpdate

#### Modify timezone

	tzselect
	select 5) Aisa
	select 9) China
	select 1) Beijing
	ensure new date-time is correct
	select 1)Yes

#### Update date

	ntpdate cn.pool.ntp.org

> RaspberryPi should update date and time on every boot. 
> If not, make sure correct network include dns resolve has been configured.
> Be attention, dns resolve in /etc/resolv.conf will be flushed on every reboot.
> Should config dns-nameservers in /etc/network/interfaces.
