#### refer articles

```shell
http://bbs.ybty.net/thread-686-1-1.html
http://www.openwrt.org.cn/bbs/thread-14787-1-1.html
```

#### install squashfs-tools

```shell
sudo apt-get install squashfs-tools
```

#### split bin file

```shell
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

xiazaibao fw-7621-xiazaibao-5.000.182.bin
 0                   11DA32             E08330             E40003
 0                   1169970            14713648           14942211
|-----1169970-------|-----13543678-----|------228564------|         

xiazaibao fw-7621-xiazaibao-5.000.186.bin
 0                   11DA55             E23F35             E40003
 0                   1170005            14827317           14942211
|-----1170005-------|-----13657312-----|------114895------|  

xiazaibao fw-7621-xiazaibao-5.000.188.bin
 0                   11D9FB             E356D5             E40003
 0                   1169915            14898901           14942211
|-----1169915-------|-----13728986-----|------43311-------|

xiazaibao fw-7621-xiazaibao-5.000.190.bin
 0                   11DA33             E81949             EC0003
 0                   1169971            15210825           15466499
|-----1169971-------|-----14040854-----|------255675------|

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

dd if=fw-7621-xiazaibao-5.000.182.bin of=first.bin bs=1 ibs=1 count=1169970
dd if=fw-7621-xiazaibao-5.000.182.bin of=second.bin bs=1 ibs=1 count=13543678 skip=1169970
dd if=fw-7621-xiazaibao-5.000.182.bin of=third.bin bs=1 ibs=1 count=228564 skip=14713648

dd if=fw-7621-xiazaibao-5.000.186.bin of=first.bin bs=1 ibs=1 count=1170005
dd if=fw-7621-xiazaibao-5.000.186.bin of=second.bin bs=1 ibs=1 count=13657312 skip=1170005
dd if=fw-7621-xiazaibao-5.000.186.bin of=third.bin bs=1 ibs=1 count=114895 skip=14827317

dd if=fw-7621-xiazaibao-5.000.188.bin of=first.bin bs=1 ibs=1 count=1169915
dd if=fw-7621-xiazaibao-5.000.188.bin of=second.bin bs=1 ibs=1 count=13728986 skip=1169915
dd if=fw-7621-xiazaibao-5.000.188.bin of=third.bin bs=1 ibs=1 count=43311 skip=14898901

dd if=fw-7621-xiazaibao-5.000.190.bin of=first.bin bs=1 ibs=1 count=1169971
dd if=fw-7621-xiazaibao-5.000.190.bin of=second.bin bs=1 ibs=1 count=14040854 skip=1169971
dd if=fw-7621-xiazaibao-5.000.190.bin of=third.bin bs=1 ibs=1 count=255675 skip=15210825
```

#### extract bin file

```shell
sudo unsquashfs second.bin
second bin will be extract to squashfs-root/
```

#### modify files in squashfs-root

#### compress squashfs-root to bin file


```shell
sudo mksquashfs squashfs-root/ new_second.bin -nopad -noappend -root-owned -comp xz -b 256k
```

#### combine bin files

```shell
cat first.bin new_second.bin third.bin > new_image.bin
```

### 中文简明教程

用WinHex打开bin文件，查找并定位到hsqs的h字符，记录下16进制值，得到值h1，用计算器转换成10进制，得到值d1  
定位到大片FFFF开头的F，记录下16进制值，得到值h2，转换成d2  
定位到最后的字符，记录下16进制值，得到h3，转换成d3  

切割文件  
count是切割后bin文件的大小，skip是跳过的字节数  

```shell
dd if=image.bin of=1.bin bs=1 ibs=1 count=d1  
dd if=image.bin of=2.bin bs=1 ibs=1 count=d2-d1 skip=d1  
dd if=image.bin of=3.bin bs=1 ibs=1 count=d3-d2+1 skip=d2  
```

也可以用WinHex获取每段的大小，定位到开头，右键->Beginning of block，定位到hsqs之前的一个字符，右键->End of Block，在右下角找到Size，转换成10进制  
定位到hsqs的h，Begin，得到h1，定位到FFFF前的字符，End，得到第二段大小    
定位到FFFF的第一个F，Begin，得到h2，定位到最后一个字符，End，得到第三段大小  


