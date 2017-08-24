# Chapter 2 操作系统结构

@(Operating System)

[toc]

## 2.1 操作系统服务
一组操作系统服务提供对用户很有用的函数：
- **用户界面**： 命令行界面和图形化界面
- **程序执行**：系统必须能将程序装入内存并运行程序。程序必须能结束执行，包括正常或不正常结束（指明错误）
- **I/O操作**：运行程序可能需要I/O，这些I/O可能涉及文件或者设备。为了提高效率和进行保护，用户通常不能直接控制I/O设备，因此，操作系统必须提供进行I/O操作的方法
- **文件系统操作**：读写文件和目录，创建删除搜索文件，访问权限控制
- **通信**：在许多情况下，一个进程需要与另一个进程交换信息。这种通信主要有两种形式：
	- 同一台计算机运行的两个进程之间
	- 由网络连接起来的不同的两个计算机的进程之间。
	- 实现方式有*共享内存*或*消息交换技术*
- **错误检测**

还有一组操作系统函数用于确保系统本身高效运行：
- **资源分配**：当同时有多个用户或多个作业运行时，系统必须为他们中的每一个分配资源。
- **统计**：需要记录哪些用户使用了多少和什么类型的资源。
- **保护和安全**

## 2.2 操作系统的用户界面（略）

## 2.3 系统调用

系统调用（system call）
:	提供了操作系统提供的有效服务界面。这些调用通常用C或C++编写。指运行在使用者空间的程序向操作系统内核请求需要更高权限运行的服务。系统调用提供用户程序与操作系统之间的接口。大多数系统交互式操作需求在内核态执行。如设备IO操作或者进程间通信。

向操作系统传递参数有三种方法：
1. 寄存器，但参数数量可能比寄存器多
2. 存在内存的块和表中，将块的地址通过寄存器来传递
3. 通过程序把参数压入堆栈中，并通过操作系统弹出。

## 2.4 系统调用类型
系统调用大致可分为五大类：
1. 进程管理（process control）
	2. end, abort
	3. load, execute
	4. create process, terminate process
	5. wait for time
	6. wait event, signal event
	7. allocate and free memory
2. 文件管理（file management）
	3. create file, delete file
	4. open, close 
	5. read, write, reposition(重定位)
	6. get file attributes, set file attributes
3. 设备管理（device management）
	4. request device, release device 
	5. read, write, reposition
	6. get device attributes, set device attributes
	7. logically attach or detach devices
4. 信息维护（information maintenance）
	5. get time or date, set time or date
	6. get system data, set system data
	7. get process, file, or device attributes
	8. set process, file, or device attributes
5. 通信（communication）
	6. create, delete communication connection
	7. send, receive messages
	8. transfer status information
	9. attach or detach remote devices 

## 2.5 系统程序

计算机逻辑层次：**最底层是硬件，上面是操作系统，接着是系统程序，最后是应用程序**。系统程序提供了一个方便的环境，一开发程序和执行程序。其中一小部分只是系统调用的简单接口，其他的可能是相当复杂的。

系统程序可分为如下几类：
- 文件管理
- 状态信息
- 文件修改
- 程序语言支持
- 程序装入和执行
- 通信
- 应用程序

## 操作系统的设计和实现（略）

## 2.7 操作系统结构

### 2.7.1 简单结构（略）

![UNIX_system_structure](http://or5jajfqs.bkt.clouddn.com/osnote/chapter2/UNIX_system_structure.png)

### 2.7.2 分层方法
操作系统分成若干层（级）。最底层（层0）为硬件，最高层（层n）为用户接口。

![分层操作系统|left](http://or5jajfqs.bkt.clouddn.com/osnote/chapter2/layered_os.png)

分层法的<font color=#FF0000>主要**优点**<font>在于构造和调试的简单化。每层只能利用较低层的功能和服务。从低层来向高层逐层进行调试.
**缺点**在于与其他方法相比其效率较差。

### 2.7.3 微内核
目的：所有非基本部分从内核中移走，并将它们实现为系统程序或用户程序。
主要功能：使客户程序和运行在用户空间的各种服务之间进行通信。
好处：便于扩充操作系统，操作系统便于移植，且拥有更好的安全性和可靠性。
缺点：由于系统功能总开销的增加而导致系统性能的下降。

## 2.8 虚拟机

虚拟机的基本思想是单个计算机（CPU、内存、磁盘、网卡等）的硬件抽象为几个不同的执行部件，从而造成一种幻觉，仿佛每个独立的执行环境都在自己的计算机上运行一样。

实现方法是利用CPU调度和虚拟内存技术。

分层方法逻辑可延伸为虚拟机（virtual machine）概念。虚拟机将硬件和操作系统内核都视为硬件。
<font color=#FF0000>优点</font>：不同的系统资源具有完全的保护。用于研究和开发操作系统。
<font color=#FF0000>缺点</font>：实现困难，主要困难与磁盘系统有关。

## 2.10 系统启动
装入内核以启动计算机的过程称为引导（booting）系统。
绝大多数计算机系统都有一小块代码（放在ROM内），它称为引导程序或引导装载程序（bootstrap program）。这段代码能定位内核，将它装入内存，开始执行。