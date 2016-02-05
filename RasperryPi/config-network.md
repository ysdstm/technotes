### Config wired network address

	sudo nano /etc/network/interfaces

#### wired static address

	auto lo
	iface lo inet loopback

	auto eth0
	#allow-hotplug eth0
	iface eth0 inet static
	address 192.168.1.247
	netmask 255.255.255.0
	gateway 192.168.1.254
	dns-nameservers 192.168.1.9

#### wired dhcp address

	auto lo
	iface lo inet loopback
	
	iface eth0 inet dhcp

#### wireless dhcp address

	auto wlan0
	allow-hotplug wlan0
	iface wlan0 inet dhcp
        wpa-ssid wifi_name
        wpa-psk wifi_pass

#### wireless dhcp address -2

	auto lo

	iface lo inet loopback
	iface eth0 inet dhcp

	allow-hotplug wlan0
	iface wlan0 inet dhcp
	pre-up wpa_supplicant -B -Dwext -iwlan0 -c/etc/wpa_supplicant/wpa_supplicant.conf
	post-down killall -q wpa_supplicant
	

	sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

	ctrl_interface=/var/run/wpa_supplicant
	ctrl_interface_group=0
	ap_scan=2
	network={   
	    ssid="WIFI名称"
	    proto=WPA2
	    key_mgmt=WPA-PSK
	    pairwise=TKIP
	    group=TKIP
	    psk="WIFI密码"
	    }
