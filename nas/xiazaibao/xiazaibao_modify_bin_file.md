#### install squashfs-tools

	sudo apt-get install squashfs-tools

#### split bin file

	download WinHex on windows, open bin file
	search "hsqs", click on letter "h", write down the "h" Offset (in WinHex status bar), this is beginning of second part.
	page down, and locate the chars are "FF FF FF ...", click on the first letter "F" , this is the beginning of third part.
	beginning of first part is the beginning of the bin file where Offset is 0.

	|                   |                  |                  |
         0                   hsqs               FF FF
	 Offset1             Offset2            Offset3            LastOffset
	
	 for example:`http://downloads.pandorabox.org.cn/pandorabox/XunLei_TimeCloud/firmware/PandoraBox-ralink-mt7621-timecloud-squashfs-sysupgrade-r1454-20150925.bin`
	 0                   12DD09             D7F41E             D80003
	 0                   1236233            14152734           14155779

	use windows 10 calc to calc the size:
	1st part size = Offset2 - Offset1(0) (1236233)
	2nd part size = Offset3 - Offset2    (14152734-1236233)=12916501
	3rd part size = LastOffset - Offset3 + 1 (verify with WinHex) (14155779-14152734) + 1 = 3046

	or use below method:

	locate beginning of bin file in WinHex, Right Click the very first char, and select Beginning of block,
	and then locate the char before "hsqs", Right Click the very first char, and select End of Block,
	will find the block size in the lower right corner of WinHex.
	repeat the above steps, find the second part size ("hsqs" to the char before "FF FF ..."), and the third part size (all "FF FF ...")
 
	convert Hex to DEC and split bin file:

	dd if=image.bin of=first.bin bs=1 ibs=1 count=first-part-size
	dd if=image.bin of=second.bin bs=1 ibs=1 count=second-part-size skip=first-part-size or second Offset
	dd if=image.bin of=third.bin bs=1 ibs=1 count=third-part-size skip=third Offset

	dd if=PandoraBox-ralink-mt7621-timecloud-squashfs-sysupgrade-r1454-20150925.bin bs=1 ibs=1 count=1236233 of=first.bin
	dd if=PandoraBox-ralink-mt7621-timecloud-squashfs-sysupgrade-r1454-20150925.bin bs=1 ibs=1 count=12916501 skip=1236233 of=second.bin
	dd if=PandoraBox-ralink-mt7621-timecloud-squashfs-sysupgrade-r1454-20150925.bin bs=1 ibs=1 count=3046 skip=14152734 of=third.bin

#### extract bin file

	sudo unsquashfs second.bin
	second bin will be extract to squashfs-root/

#### modify files in squashfs-root

#### compress squashfs-root to bin file


	sudo mksquashfs squashfs-root/ new_second.bin -nopad -noappend -root-owned -comp xz -b 256k

#### combine bin files
	
	cat first.bin new_second.bin third.bin > new_image.bin
