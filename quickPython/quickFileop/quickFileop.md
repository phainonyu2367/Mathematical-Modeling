## open
```
file = open(file, mode='r')
```
python open()方法是python内置的用于文件操作的方法，可以用于打开一个文件，并返回文件对象。
- file: 文件名
- mode: 操作模式
>[!info] 完整的语法模式
>```
>open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
>```
>
>file: 必需，文件路径（相对或者绝对路径）。
 mode: 可选，文件打开模式
 buffering: 设置缓冲
 encoding: 一般使用utf8
 errors: 报错级别
 newline: 区分换行符
 closefd: 传入的file参数类型
 opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。

其中，模式控制了文本打开的方式/操作的权限。
常见的文本打开方式有：
- r: read
- w: write
- x: execute，新建一个文件，若该文件已存在则会报错
- +: 打开一个文件进行更新（可读可写）
- a: add, 在文件末尾开始操作
当然，这些模式也可以组合
- a+
- r+
- ......

## file对象方法
`file = open('text.txt', mode=a+）`
file有如下方法
- file.close()  # 关闭文件，不在读写
- file.flush() # 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
- file.next()
- file.read(size) # 读取指定数量的字符
- file.readline(size) # 读取整行
- file.tell() # 返回文件当前位置
- file.truncate(size) # 截取文件，截取的字节通过size指定，默认为当前文件位置
- file.write(str)
- file.writelines(sequence) # 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。

## 常见的用法
```
with open('text.txt', a+) as fp:
	...
```
