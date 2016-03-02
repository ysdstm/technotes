## 学习正则表达式

### 什么是正则表达式

#### 1.2 匹配北美电话号码

例如：  
707-825-7019 或 (707)-825-7019  

#### 1.3 使用字符组匹配数字

匹配数字`[0-9]`  

正则表达式将方括号视为特殊的`元字符`，因此方括号不参与匹配  
`元字符`是在正则表达式中有特殊含义的字符，也是保留字符  
`[0-9]`这种形式的正则表达式称作`字符组`，也叫`字符集`  

进一步限定数字，可以是`[012789]`  

#### 1.4 使用字符组简写式

`\d`也可以匹配任意阿拉伯数字，相当于`[0-9]`  
这种正则表达式叫做`字符组简写式`，也叫`转移字符`，但很容易造成误解  
`\D`则表示任意一个非数字字符  

#### 1.5 匹配任意字符

点号`.`是一个通配符，可以匹配任意字符，某些情况下不能匹配行起始符，比如换行符(U+000A)    

#### 1.6 捕获分组和后向引用

要创建捕获分组，需要将匹配字符的正则表达式放在括号中，例如(\d)  
反向引用使用\1来捕获，(\d)\d\1匹配电话号码中的区号707，\1表示捕获的第1个字符或字符串，\2则是捕获的第2个字符或字符串  

#### 1.7 使用量词

`\d{3}`表示