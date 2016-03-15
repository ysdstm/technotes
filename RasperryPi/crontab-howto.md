#### schedule tasks with cron

refer to `https://www.raspberrypi.org/documentation/linux/usage/cron.md`

##### edit crontab

$crontab -e

##### select an editor

The first time you run `crontab` you'll be prompted to select an editor; if you are not sure which one to use, choose `nano` by pressing `Enter`.

##### add a scheduled task

The layout for a cron entry is made up of six components: minute, hour, day of month, month of year, day of week, and the command to be executed.

	# m h  dom mon dow   command
	# * * * * *  command to execute
	# ┬ ┬ ┬ ┬ ┬
	# │ │ │ │ │
	# │ │ │ │ │
	# │ │ │ │ └ day of week (0 - 7) (0 to 6 are Sunday to Saturday, or use names; 7 is Sunday, the same as 0)
	# │ │ │ └ month (1 - 12)
	# │ │ └ day of month (1 - 31)
	# │ └ hour (0 - 23)

	# └ min (0 - 59)
For example:

	0 0 * * *  /home/pi/backup.sh

This cron entry would run the `backup.sh` script every day at midnight.

##### view scheduled tasks

crontab -l


##### run a task on reboot

To run a command every time the Raspberry Pi starts up, write @reboot instead of the time and date. For example:

	@reboot python /home/pi/myscript.py

This will run your Python script every time the Raspberry Pi reboots. If you want your command to be run in the background while the Raspberry Pi continues starting up, add a space and `&` at the end of the line, like this:

	@reboot python /home/pi/myscript.py &
