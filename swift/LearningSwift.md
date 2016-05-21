### Learning Swift

> 《Swift for Beginners - Develop and Design》

#### Chapter 1. Introducing Swift

#### 1.3 Ready, Set... 环境设定

首先，安装Xcode6或Xcode7  

在OS X EI Captain和XCode7环境下，执行以下命令  

```
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer/
再执行
xcrun swift
或
swift
```

> 但是会报错，估计需要升级到最新10.11，暂时只能放弃Terminal了  

#### 1.4 Diving into Swift

```
$ swift
Welcome to Apple Swift version 2.1.1 (swiftlang-700.1.101.15 clang-700.1.81). Type :help for assistance.
  1>  
```

退出REPL  

```
:exit
```

#### 1.4.1 帮助和退出

```
:help
:exit
```

1.4.2 Hello World

输出到控制台

```
print("Bonjour, monde")
println("!")
注意println只在控制台有用
```

#### 1.5 声明的威力

```
var x = 12
var y = 42.0
如果在控制台中，将显示以下内容
x: Int = 12
y: Double = 42.0
说明Swift能够将变量自动声明为合适的类型
```

