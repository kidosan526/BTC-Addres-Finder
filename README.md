# BTC-Addres-Finder


这是一个利用python编写的，生成含有指定字符串的比特币地址的脚本。
***注：对大小写敏感***
运行 finder.py 输入指定字符串，脚本会不断生成随机私钥，并计算对应的比特币地址。地址类型为Legacy，即以“ 1 ”开头。私钥以“ L ”开头，为52位支持压缩格式的私钥。
在本电脑测试，每秒大约检验15个比特币地址，与CPU性能无关，目前没找到优化方式，如有好的意见，必将采纳并感谢。
---
---

This is a script written in python that generates a bitcoin address containing a specified string.
***Note: sensitive to case***
Run finder.py Enter the specified string, the script will continuously generate a random private key and calculate the corresponding Bitcoin address. The address type is Legacy, which starts with "1". The private key starts with "L" and is a 52-bit private key that supports compressed format.
In this computer test, about 15 Bitcoin addresses are checked every second, which has nothing to do with CPU performance. Currently, no optimization method has been found. If you have any good comments, you will surely be adopted and thanked.
