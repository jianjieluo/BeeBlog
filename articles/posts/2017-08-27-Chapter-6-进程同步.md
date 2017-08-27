@(Operating System)

[toc]

# Chapter 6 进程同步

## 6.1 背景

竞争条件(race condition)
:    多个进程并发访问和操作统一数据且执行结果与访问发生的特定顺序有关。（感觉上英文的意思是“情况”，它是指一种情形，而不是指一种条件）

## 6.2 临界区问题

程序在其称为**临界区**（critical section）的代码段内可能改变变量、更新一个表、写一个文件等。（就是说会对某些数据资源做出修改）。程序在**进入区**（entry section）请求允许进入临界区。临界区之后可有**退出区**（exit section），其他代码为**剩余区**（remainder section）。

临界区问题（critical-section problem）：设计一个以便进程协作的协议。
临界区问题的解答必须满足如下三项要求：
1. 互斥（mutual exclusion）（无空等待）：同一时间只有一个进程能在其临界区内执行
2. 前进（progress）（有空让进）：如果没有进程在临界区内且有进程需要进入临界区，那么选择下一个进入临界区进程的操作不能被无限延迟。
3. 有限等待（bounded waiting）：从一个进程做出进入临界区的请求，直到该请求允许为止，其它进程允许进入其临界区的次数有上限。

对于操作系统内的临界区问题的解决办法，分为抢占内核和非抢占内核，区别在于是否允许处于内核模式的进程被抢占。

## 6.3 Peterson 算法
Peterson算法需要在两个进程之间共享两个数据项：

```cpp
int turn;
Boolean flag[2];
```

变量`turn`表示哪个进程可以进入其临界区。数组`flag`表示哪个进程想要进入其临界区。

如何证明这个解答的正确性？依次证明满足了前面的三项要求。

## 6.4 硬件同步
通过要求临界区用**锁**（lock）来防护，就可避免竞争条件，即一个进程在进入临界区之前必须得到锁，而在其退出临界区时释放锁。

缺点：
1. 对不能进入临界区的进程，采用**忙等待**测试法，浪费CPU时间。
2. 将测试是否进入临界区的责任推给各个竞争的进程会削弱系统的可靠性，加重了用户编程负担。

## <font color="red">6.5 信号量</font>

信号量
:	是一种与临界区资源相联系的变量

Wait() = P()
Signal = V()
解决了有限缓冲区和读者写者问题的实验。

### 6.5.1 用法
计数信号量（counting semaphore）的值域不受限制。
二进制信号量（binary semaphore）的值只能为0或1。有的系统将二进制信号量称为互斥锁（mutex），因为它们可以提供互斥。

Hint: 互斥锁 = 二进制信号量，非也，区别还在于归属性问题。

```cpp
do {
	waiting(mutex);
		// critical section
	signal(mutex);
		// remainder section
} while (TRUE);
```

### 6.5.2 实现

之前提到的Peterson算法和硬件同步，对于等待信号量的进程，使用的是本质上与while(1)相同的忙等待。这种实现方式会浪费CPU时钟。

这里提出新的实现方式，通过阻塞操作，将等待信号量的进程放入到阻塞队列。阻塞队列中没轮到的进程切换到等待状态，轮到的时候就用wakeup()操作重新执行。（这个是用来解决忙等待的问题的）。显然这种实现方式解决的CPU时钟浪费的问题，但是比起忙等待则多了上下文切换的额外开销。

在居于忙等的信号量的经典定义下，信号量的值不可能为负，但是新的实现可以出现负的信号值，负的信号量的绝对值就是等地啊该信号量的进程的个数。

自旋锁（spinlock）
:	进程在等待锁时还在运行（自旋锁的优点是：避免了上下文切换的时间）

信号量的关键之处是它们**原子地执行**。必须确保没有两个进程能同时对同一信号量执行操作wait()和signal()。

### 6.5.3 死锁与饥饿

死锁
:	两个或者多个进程无限地等待一个事件，而该事件只能由这些等待进程之一来产生。这里的事件是由signal()操作的执行。

**无限期阻塞**(indefinite blocking)或**饥饿**(starvation)
:	进程在信号量内无限期等待。

### 6.6 经典同步问题

#### 6.6.1 有限缓冲问题
有n(>=1)个生产者产生某种类型的数据，并放置在缓冲区，有m(>=1)个消费者从缓冲区取数据，每次取一项。缓冲区大小为n。

共享数据包括：
1. 信号量full，表示满缓冲项的个数，初始化为0
2. 信号量empty，表示空缓冲项的个数，初始化为n
3. 信号量mutex，提供对缓冲池访问的互斥要求，初始化为1

####6.6.2 读者-写者问题
存在两组并发进程：读者和写者，它们共享一个文件F，要求：
任意多个读者可以同时读文件；一次只有一个写者可以往文件中写；写者执行写操作前，禁止任何读者读文件。
共享数据包括：
1. 数据集合
2. 信号量mutex，用于确保在更新readerCount时的互斥，初始化为1
3. 信号量wrt，供写者作为互斥信号量，初始化为1
4. 整数readerCount，用来跟踪有多少金城正在读对象，初始化为0

####6.6.3 哲学家就餐问题
共享数据包括：
1. 一碗米饭（数据集合）
2. 信号量chopStick[5]初始化为1

--- 

## 额外学习知识

### 1. pthread_mutex_t  vs  sem_t
**semaphores can be used between different processes to synchronise access to some shared object** i.e. a file or shared memory.

If you have two processes which require read/write access to some resource you need to make sure that both are not trying to change the shared resource at the same time.  You can then use a semaphore to protect the access to the shared resource i.e each process has to acquire the semaphore before being allowed to perform an update on the shared resource.  Once the update is complete the process then releases the semaphore to allow another process to access/update the shared resource.

**pthread_mutex_t is a similar concept but shared between multiple threads of a single process.**  If for example you have a multithreaded program which contains global data accessible/updatable by multiple threads then you would a mutex to protect the access in the same way.(while actually, it seems that if init the mutex value not 0, then it can be shared among processes.)

>Semaphores have a synchronized counter and mutex's are just binary (true / false).
>
>A semaphore is often used as a definitive mechanism for answering how many elements of a resource are in use -- e.g., an object that represents n worker threads might use a semaphore to count how many worker threads are available.

>One significant difference (since I've seen people make this mistake before): a semaphore may be procured and vacated by any thread in any sequence (so long as the count is never negative), but a mutex may only be unlocked by the thread that locked it. Attempting to unlock a mutex which was locked by another thread is undefined behavior.


[Lock, mutex, semaphore… what's the difference?
](https://stackoverflow.com/questions/2332765/lock-mutex-semaphore-whats-the-difference?rq=1)

Mutex: Is a key to a toilet. 
Semaphore: Is the number of free identical toilet keys.

1. [Mutex vs. Semaphores – Part 1: Semaphores](https://blog.feabhas.com/2009/09/mutex-vs-semaphores-%E2%80%93-part-1-semaphores/)
2. [Mutex vs. Semaphores – Part 2: The Mutex](https://blog.feabhas.com/2009/09/mutex-vs-semaphores-%E2%80%93-part-2-the-mutex/)
	3. [Mutex vs. Semaphores – Part 3 (final part): Mutual Exclusion Problems](https://blog.feabhas.com/2009/10/mutex-vs-semaphores-%E2%80%93-part-3-final-part-mutual-exclusion-problems/)