# AUTOMATE THE BORING STUFF WITH PYTHON

python编程快速上手—让繁琐的工作自动化

[美]AI Sweigart	王海鹏	译

#### 本书的对象和编写本书的意义、

本书的对象是所有的人，所以内容主要是PYthon的基础

编写本书的意义在于：

学过了可以进行一些简单的任务自动化，比如：

* 移动并重命名几千个文件，将它们分类，并放入文件夹
* 填写在线表单，不需要打字
* 在网站更新时，从网站下载文件或复制文本
* 让计算机向客户发出短信通知
* 更新或格式化Excel电子表格
* 检查电子邮件并发出预先写好的回复

#### 什么是编程

所有程序都使用基本指令作为构件块。下面是一些常用的指令，用自然语言的形式来表示：

“做这个 ，然后做那个”

“如果这个条件为真，执行这个动作，否则，执行那个动作”

“按照指定次数执行这个动作”

“一直做这个，直到条件为真”



示例：

```
passwordFile = open('secretPasswordFile.txt') `打开文件secretPasswordFile.txt
secretPassword = passwordFile.read()	`读取其中的密码
print('Enter your password:')	`提示用户输入一个密码
typedPassword = input()	`输入密码
if typedPassword == secretPassword:	`比较这两个密码若一样
    print('Access granted')	`就输出Access granted
if typedPassword == '12345':	`若typedPassword等于12345
    print('That password is one that an ideiot puts on their luggage.')
else:
    print('Access denied') 

```

#### Python是什么

Phthon指的是Python编程语言（包括语法法则，用于编写被认为是有效的Python代码），以及Python解释器软件 ，它读取源代码（用Python语言编写），并执行其中的指令，Python解释器可以从http://python.org免费下载。

Python的名字来自英国超现实主义喜剧团体，而不是来自于蛇。Python程序员被亲切地称为Pythonistas。Monty        Python和与蛇相关的引用常常出现在Python的指南和文档中

#### 程序员不需要知道太多数学知识

***我听到的关于学习编程的最觉的顾虑，就是人们认为学习编程需要很多数学知识。其实，大多数编程需要的数学知识并不会超过基本算术。实际上，善于编程和善于解决数独问题并没有太大差别。***

***像所有技能一样，编程越多，你就掌握的越多***

#### 编程是一项创造性活动

***编程是一项创造性活动，有点类似于用乐高积木构建一个城堡，不同之处在于，你创建城堡的原材料都在计算机里，不需要购买额外的材料***

#### 本书简介

**第一部分 Python编程基础**



“第一章：Python基础”介绍了表达式，Python指令的最基本类型，以及如何使用Python交互式环境来尝试运行代码。

“第二章：控制流”解释了如何让程序如何定义自己的函数，以便将代码组织成可管理的部分。

“第三章：函数”介绍了如何定义自己的函数，以便将代码组织成可管理的部分。

“第四章：列表”介绍了列表数据类型，解释了如何组织数据。

“第五章：字典和结构化数据“介绍了字典数据类型，展示了更强大的数据组织方法。

”第六章：字符串操作“介绍了处理文本数据（在Python中称为字符串）。



**第二部分 自动化任务**



“第七章：模式匹配与正则表达式”介绍了Python如何用正则表达式处理字符串，以及查找文本模式。

“第八章：读写文件”解释了程序如何读取文本文件的内容，并将信息保存到硬盘的文件中。

“第九章：组织文件”展示了Python如何用手工操作快得多的速度，复制、移动、重命名和删除大量的文件，也解释了压缩和解压缩文件。

“第十章：调试”展示了如何使用Python的缺陷查找和缺陷修复工具。

“第十一章：从Web抓取信息”展示了如何编程来自动下载网页，解析它们，获取信息，这称为从Web抓取信息。

“第十二章：处理Excel电子表格”介绍了编程处理Excel电子表格，这样你就不必去阅读它们，如果你必须分析成百上千的文档，这是很有帮助的。

“第十三章：处理PDF和WORD文档”介绍了编程读取Word和Pdf文档。

“第十四章：处理CSV文件和JSON数据”解释了如何编程操作CSV和JSON文件。

“第十五章：保持时间、计划任务和启动程序”解释了Python程序如何处理肌肤今天日期，如何安排计算机在特定时间执行任务。这一章也展示了Python程序如何启动非Python程序。

'第十六章：发送电子 邮件和短信“解释了如何编程来发送电子邮件和短信。

”第十七章：操作图像“解释了如何编程来JPG或PNG这样的图像。

"第十八章：用GUI自动化控制那般和鼠标”解释了如何编程控制鼠标和那般，自动化鼠标点击和击键。



#### 根据操作系统的类型和位数来下载安装相应的Python软件

操作系统的类别：

Windows

Linux

OS X

操作系统的位别

32位

64位

#### Python解释器IDLE

```c
C:\Program Files\Python39
λ dir
 驱动器 C 中的卷是 系统
 卷的序列号是 F070-971A

 C:\Program Files\Python39 的目录

2021-04-24  10:58    <DIR>          .
2021-04-24  10:58    <DIR>          ..
2021-04-24  10:58    <DIR>          DLLs
2021-04-24  10:57    <DIR>          Doc
2021-04-24  10:57    <DIR>          include
2021-04-24  10:57    <DIR>          Lib
2021-04-24  10:57    <DIR>          libs
2021-04-06  14:14            32,628 LICENSE.txt
2021-04-06  14:15         1,054,193 NEWS.txt
2021-04-06  14:14           101,552 python.exe
2021-04-06  14:14            59,568 python3.dll
2021-04-06  14:14         4,459,696 python39.dll
2021-04-06  14:14           100,016 pythonw.exe
2021-04-24  10:58    <DIR>          Scripts
2021-04-24  10:58    <DIR>          tcl
2021-04-24  10:57    <DIR>          Tools
2021-04-06  14:14            96,144 vcruntime140.dll
2021-04-06  14:14            36,752 vcruntime140_1.dll
               8 个文件      5,940,549 字节
              10 个目录 49,732,665,344 可用字节

C:\Program Files\Python39
λ python
Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win3211
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## 第一章 Python基础

### 1.1 操作符与表达式

| 操作符 | 操作          | 例子  | 求值为 |
| ------ | ------------- | ----- | ------ |
| **     | 指数          | 2**3  | 8      |
| %      | 取模/取余数   | 22%8  | 6      |
| //     | 整除/商数取整 | 22//8 | 2      |
| /      | 除法          | 22/8  | 2.75   |
| *      | 乘法          | 3*5   | 15     |
| -      | 减法          | 5-2   | 3      |
| +      | 加法          | 2+2   | 4      |

数学操作符的操作顺序（也称为“优先级）与数学中类似。”“操作符首先求值，接下来是*、/、%和//，+和-操作符最后求值，也是从左到右。

```c
C:\Program Files\Python39
λ python
Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 3 * 6
20
>>> (2 + 3) * 6
30
>>> 354739571 * 1938570983
687687838862468293
>>> 2 ** 8
256
>>> 23 // 7
3
>>> 2 + 2
4
>>> (5 - 1)*((7 + 1) / (3 - 1))
16.0
>>>
```

在每个例子中，作为程序员，你必须要输入表达式，但Python完成较难的工作，将它求值为单个值，Python将继续求值表达式的各个部分，直到它成为单个值 。

**将操作符和值 放在一起构成表达工的这些规则，是Python编程语言的基本部分，就像帮助我们沟通的语法规则一样**

#### 1.2 整型、浮点型和字符串数据类型

常见数据类型
整型 -2, -1, 0, 1, 2, 3, 4, 5
浮点型 -1.25, -1.0, - -0.5, 0.0, 0.5, 1.0, 1.25
字符串 'a', 'aa', 'aaa', 'Hello!', '11 cats'    没有字符的字符串，称为“空字符串”**用单引号引起来**

#### 1.3	字符串连接和复制

> 'Alice' + 'Bob'
>
> ‘AliceBob'

>'Alice' * 5
>'AliceAliceAliceAliceAlice'

#### 1.4	在变量中保存值

“变量”就像计算机内存中的一个盒子，其中可以存放一个值。如果你的程序
稍后将用到一个已求值的表达式的结果，就可以将它保存在一个变量中。

>spam = 'Hello'
>spam
>'Hello'
>spam = 'Goodbye'
>spam
>'Goodbye'

1．只能是一个词。
2．只能包含字母、数字和下划线。
3．不能以数字开头。

有效的变量名 无效的变量名
balance 				    	current-balance（不允许中划线）
currentBalance 		   current balanc（不允许空格）
current_balance 		   4account（不允许数字开头）
spam 							   42（不允许数字开头）
SPAM 								total_$um（不允许$这样的特殊字符）
account4 						'hello'（不允许'这样的特殊字符）
**变量名是区分大小写的。这意味着，spam、 SPAM、Spam 和sPaM 是4 个不
同的变量。变量用小写字母开头是Python 的惯例。**

#### 1.5	第一个程序

* 交互式环境窗口总是有>>>提示符

* 文件编辑器窗口没有>>>提示符

  ```python
  * #This program says hello and asks for my name.
    print('Hello world!')
    print('What is your name?') # ask for their name
    myName = input()
    print('It is good to meet you, ' + myName)
    print('The length of your name is:')
    print(len(myName))
    print('What is your age?') # ask for their age
    myAge = input()
    print('You will be ' + str(int(myAge) + 1) + ' in a year.')
  
  
  ```

  

#### 1.6程序剖析

1.6.1注释

```python
#This program says hello and asks for my name.
```



1.6.2 print()函数

```python
print('Hello world!')
print('What is your name?') # ask for their name
```



1.6.3 input()函数

```
myName = input()
```



1.6.4打印用的名字

```
print('It is good to meet you, ' + myName)
```



1.6.5len()函数

```python
print('The length of your name is:')
print(len(myName))
在交互式环境中输入以下内容试一试：
>>> len('hello')
5
>>> len('My very energetic monster just scarfed nachos.')
46
>>> len('')
0
```

就像这些例子，len(myName)求值为一个整数。然后它被传递给print()，在屏幕
上显示。请注意，print()允许传入一个整型值或字符串。但如果在交互式环境中输
入以下内容，就会报错：

>print('I am ' + 29 + ' years old.')
>Traceback (most recent call last):
>File "<pyshell#6>", line 1, in <module>
>print('I am ' + 29 + ' years old.')
>TypeError: Can't convert 'int' object to str implicitly
>
>导致错误的原因不是print()函数，而是你试图传递给print()的表达式。如果在
>交互式环境中单独输入这个表达式，也会得到同样的错误。
>
>'I am ' + 29 + ' years old.'
>Traceback (most recent call last):
>File "<pyshell#7>", line 1, in <module>
>'I am ' + 29 + ' years old.'
>TypeError: Can't convert 'int' object to str implicitly
>
>报错是因为，只能用+操作符加两个整数，或连接两个字符串。不能让一个整数和一个字符串相加，因为这不符合Python 的语法。可以使用字符串版本的整数，
>修复这个错误。这在下一节中解释。

1.6.6 str()、int()、float()

如果想要连接一个整数（如29）和一个字符串，再传递给print()，就需要获得
值'29'。它是29 的字符串形式。str()函数可以传入一个整型值，并求值为它的字符
串形式，像下面这样：

str(29)
'29'
print('I am ' + str(29) + ' years old.')
I am 29 years old.
因为str(29)求值为’29’，所以表达式'I am ' + str(29) + ' years old.'求值为'I am ' +
'29' + ' years old.'，它又求值为'I am 29 years old.'。这就是传递给print()函数的值。
str()、int()和float()函数将分别求值为传入值的字符串、整数和浮点数形式。请
尝试用这些函数在交互式环境中转换一些值，看看会发生什么。
str(0)
'0'
str(-3.14)
'-3.14'
int('42')
42
int('-99')
-99
int(1.25)
1
int(1.99)
1
float('3.14')
3.14
float(10)
10.0
前面的例子调用了str()、int()和float()函数，向它们传入其他数据类型的值，得
到了字符串、整型或浮点型的值。
如果想要将一个整数或浮点数与一个字符串连接，str()函数就很方便。如果你
有一些字符串值，希望将它们用于数学运算，int()函数也很有用。例如，input()函
数总是返回一个字符串，即便用户输入的是一个数字。在交互式环境中输入spam =
input()，在它等待文本时输入101。
spam = input()
101
spam
'101'
保存在spam 中的值不是整数101，而是字符串'101'。如果想要用spam 中的值进
行数学运算，那就用int()函数取得spam 的整数形式，然后将这个新值存在spam 中。

spam = int(spam)
spam
101
现在你应该能将spam 变量作为整数，而不是字符串使用。
spam * 10 / 5
202.0
请注意，如果你将一个不能求值为整数的值传递给int()，Python 将显示出错信息。
int('99.99')
Traceback (most recent call last):
File "<pyshell#18>", line 1, in <module>
int('99.99')
ValueError: invalid literal for int() with base 10: '99.99'
int('twelve')
Traceback (most recent call last):
File "<pyshell#19>", line 1, in <module>
int('twelve')
ValueError: invalid literal for int() with base 10: 'twelve'
如果需要对浮点数进行取整运算，也可以用int()函数。
int(7.7)
7
int(7.7) + 1
8
在你的程序中，最后3 行使用了函数int()和str()，取得适当数据类型的值。
. print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
myAge 变量包含了input()函数返回的值。因为input()函数总是返回一个字符串
（即使用户输入的是数字），所以你可以使用int(myAge)返回字符串的整型值。这个
整型值随后在表达式int(myAge) + 1 中与1 相加。
相加的结果传递给str()函数：str(int(myAge) + 1)。然后，返回的字符串与字符
串'You will be '和' in a year.'连接，求值为一个更长的字符串。这个更长的字符串最
终传递给print()，在屏幕上显示。
假定用户输入字符串'4'，保存在myAge 中。字符串'4'被转换为一个整型，所以
你可以对它加1。结果是5。str()函数将这个结果转化为字符串，这样你就可以将它
与第二个字符串'in a year.'连接，创建最终的消息。这些求值步骤如图1-4 所示。

***文本和数字相等判断
虽然数字的字符串值被认为与整型值和浮点型值完全不同，但整型值可以与
浮点值相等。***

42 == '42'
False
42 == 42.0
True

42.0 == 0042.000
True
***Python 进行这种区分，因为字符串是文本，而整型值和浮点型都是数字。***

![image-20210531200655051](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210531200655051.png)





## 第二章 控制流

![image-20210531200814403](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210531200814403.png)

一张流程图，告诉你下雨后该怎么做

#### 2.1 布尔值

虽然整型、浮点型和字符串数据类型有无数种可能的值，但“布尔”数据类型
只有两种值：True 和False。Boolean（布尔）的首字母大写，因为这个数据类型是
根据数学家George Boole 命名的。在作为Python 代码输入时，布尔值True 和False
不像字符串，两边没有引号，它们总是以大写字母T 或F 开头，后面的字母小写。
在交互式环境中输入下面内容，其中有些指令是故意弄错的，它们将导致出错信息。
. >>> spam = True

spam
True
. >>> true
Traceback (most recent call last):
File "<pyshell#2>", line 1, in <module>
true
NameError: name 'true' is not defined
. >>> True = 2 + 2
SyntaxError: assignment to keyword
像其他值一样，布尔值也用在表达式中，并且可以保存在变量中.。如果大小
写不正确.，或者试图使用True 和False 作为变量名.，Python 就会给出错误信息。

#### 2.2 比较操作符

“比较操作符”比较两个值，求值为一个布尔值。表2-1 列出了比较操作符。
表2-1 比较操作符
操作符 含义
== 等于
!= 不等于
< 小于
大于
<= 小于等于
= 大于等于
这些操作符根据给它们提供的值，求值为True 或False。现在让我们尝试一些
操作符，从==和！=开始。
42 == 42
True
42 == 99
False
2 != 3
True
2 != 2
False
如果两边的值一样，==（等于）求值为True。如果两边的值不同，!=（不等于）
求值为True。==和!=操作符实际上可以用于所有数据类型的值。
'hello' == 'hello'
True
'hello' == 'Hello'
False
'dog' != 'cat'
True
True == True
True
True != False
True
42 == 42.0
True
. >>> 42 == '42'
False
请注意，整型或浮点型的值永远不会与字符串相等。表达式42 == '42'.求值为
False 是因为，Python 认为整数42 与字符串'42'不同。
另一方面，<、>、<=和>=操作符仅用于整型和浮点型值。
42 < 100
True
42 > 100
False
Python 编程快速上手——让繁琐工作自动化
42 < 42
False
eggCount = 42
. >>> eggCount <= 42
True
myAge = 29
. >>> myAge >= 10
True
操作符的区别
你可能已经注意到，==操作符（等于）有两个等号，而=操作符（赋值）只
有一个等号。这两个操作符很容易混淆。只要记住：
. ==操作符（等于）问两个值是否彼此相同。
. =操作符（赋值）将右边的值放到左边的变量中。
为了记住谁是谁，请注意==操作符（等于）包含两个字符，就像!=操作符（不
等于）包含两个字符一样。
你会经常用比较操作符比较一个变量和另外某个值。就像在例子eggCount <=
42.和myAge >= 10.中一样（毕竟，除了在代码中输入'dog' != 'cat'以外，你本来也
可以直接输入True）。稍后，在学习控制流语句时，你会看到更多的例子。

#### 2.3 布尔操作符

3 个布尔操作符（and、or 和not）用于比较布尔值。像比较操作符一样，它们
将这些表达式求值为一个布尔值。让我们仔细看看这些操作符，从and 操作符开始。
2.3.1 二元布尔操作符
and 和or 操作符总是接受两个布尔值（或表达式），所以它们被认为是“二元”
操作符。如果两个布尔值都为True，and 操作符就将表达式求值为True，否则求值
为False。在交互式环境中输入某个使用and 的表达式，看看效果。
True and True
True
True and False
False
“真值表”显示了布尔操作符的所有可能结果。表2-2 是操作符and 的真值表。
表2-2 and 操作符的真值表
表达式 求值为
True and True True
True and False False
False and True False
False and False False
第2 章 控制流
另一方面，只要有一个布尔值为真，or 操作符就将表达式求值为True。如果都
是False，所求值为False。
False or True
True
False or False
False
可以在or 操作符的真值表中看到每一种可能的结果，如表2-3 所示。
表2-3 or 操作符的真值表
表达式 求值为
True or True True
True or False True
False or True True
False or False False
2.3.2 not 操作符
和and 和or 不同，not 操作符只作用于一个布尔值（或表达式）。not 操作符求
值为相反的布尔值。
not True
False
. >>> not not not not True
True
就像在说话和写作中使用双重否定，你可以嵌套not 操作符.，虽然在真正的
程序中并不经常这样做。表2-4 展示了not 的真值表。
表2-4 not 操作符的真值表
表达式 求值为
not True False
not False True

#### 2.4 混合布尔和比较操作符

既然比较操作符求值为布尔值，就可以和布尔操作符一起，在表达式中使用。
回忆一下，and、or 和not 操作符称为布尔操作符是因为，它们总是操作于布尔
值。虽然像4 < 5 这样的表达式不是布尔值，但可以求值为布尔值。在交互式环境
中，尝试输入一些使用比较操作符的布尔表达式。
(4 < 5) and (5 < 6)
True
(4 < 5) and (9 < 6)
False
Python 编程快速上手——让繁琐工作自动化
(1 == 2) or (2 == 2)
True
计算机将先求值左边的表达式，然后再求值右边的表达式。知道两个布尔值后，
它又将整个表达式再求值为一个布尔值。你可以认为计算机求值(4 < 5)和(5 < 6)的
过程，如图2-2 所示。
图2-2 (4 < 5)和 (5 < 6) 求值为True 的过程
也可以在一个表达式中使用多个布尔操作符，与比较操作符一起使用。
2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
True
和算术操作符一样，布尔操作符也有操作顺序。在所有算术和比较操作符求值
后，Python 先求值not 操作符，然后是and 操作符，然后是or 操作符。

#### 2.5控制流的元素

条件：Ture  False

代码块

1．缩进增加时，代码块开始。
2．代码块可以包含其他代码块。
3．缩进减少为零，或减少为外面包围代码块的缩进，代码块就结束了。

```python
name = input()
password = input()
if name == 'Mary':
    print('Hello Mary')
if password == 'swordfish':
    print('Access granted')
else:
    print('Wrong password'
```

#### 2.7控制流语句

2.7.1 if语句

**if语句包含以下部分

* if关键字；
* 条件（妈耶求值 为True或False的表达式）；
* 冒号
* 在下一行开始，缩进的代码块（称为If子句）
* 所有的控制流语名都以冒号结尾，后面跟着一个新的代码块（子句）

if语句流程图

![image-20210531203347290](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210531203347290.png)

if name == 'Alice':

print(''HI, Alice)

2.7.2 else 语句

* else关键字
* 冒号；
* 在下一行开始，缩进的代码块（称为else子句）

if name == 'Alice':

​	print('Hi,Alice')

else:

print('Hello,stranger')

流程图

![image-20210531203825592](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210531203825592.png)

2.7.3

**精采的来了，if elif else，如果希望至少一条子句被执行**

if name == 'Alice':

​	print('Hi, Alice.')

elif age < 12:

​	print('You are not Alice, kiddo.')

else:

​	print('You are neither Alice nor a little kid.')

流程图：

![image-20210601150740223](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210601150740223.png)

## 2.7.4	while循环语句

* 关键字
* 条件（求值为True或False的表达式）
* 冒号
* 从新行开始，缩进的代码块（称为while子句）

