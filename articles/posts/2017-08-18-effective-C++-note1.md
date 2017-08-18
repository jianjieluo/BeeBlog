
《Effective C++》中文版阅读摘要 （不定时更新）
===


30. Understand the ins and outs of inlining.
    - inline函数背后的整体观念是：将“对此函数的每一个调用”都以函数本体替换之
    - inline只是对编译器的一个申请，不是一个强制命令
    - inline的声明可以隐喻也可以显式
        - 隐喻的方式是将函数定义于class的定义式内
        - 显式的方式是直接在前面加上 inline 的字段
    - inline 可以减少函数调用所招致的额外开销，但是也可能造成代码的膨胀，使得程序体积太大
    - 大部分的编译器是拒绝将virtual 函数设置为inline的，因为virtual需要等待，而inline则是在生成之前就要插入的
    - 构造函数和析构函数往往是inlining的糟糕候选
        - **尤其是在代码有继承的情况下**
            - 因为可能在构造函数里面，插入大量的基类的构造代码
        - 这和我们大学上课时打的简单代码题有所不同
    - 必须评估“将函数声明为inline”所带来的冲击，因为其无法随程序库的升级而升级
    - 大部分的调试器对于inline的函数束手无策，**因为不能在一个并不存在的函数内设置断点**
    - 在开发时，一开始先不要将任何函数声明为inline，或至少将inlining施行的范围局限。我们应该要做的是开发完成后，再应用程序的80-20经验法则，对花费时间多的那20%的代码上用inline或其他方法来瘦身。

1. Accustoming Yourself to C++
    - View C++ as a federation of languages
    - 将c++看成4个次语言
        - C
        - Object-Oriented C++
        - Template C++
        - STL

2. Prefer consts, enums, and inlines to #defines
    - 对于单纯常量，最好以const对象或enums替换#defines
    - 对于形似函数的宏(macros), 最好改用inline-template 函数替换#defines

3. Use const whenever possible.
    - const std::vector<int>::iterator iter = vec.begin();  // iter的作用像个T* const
    - std::vector<int>::const_iterator cIter = vec.begin();  // iter的作用像个const T*
    - const 成员函数内是不能修改成员变量的
    - mutable关键字使得被修饰的成员变量可能总是会被更改，即使在const成员函数内
    - const 和 non-const 成员函数中避免重复
        - 当两者有着实质等价的实现时，令 non-const 版本调用const版本可以避免代码重复
    - cosnt 可被施加于任何作用域内的对象，函数参数，函数返回类型，成员函数本体

4. Make sure that objects are initialized before they're unsigned
    - 为内置型对象进行手工初始化，因为c++不保证初始化它们
    - 过哦早函数最好使用 member initialization list ，而不要在构造函数本体内使用赋值操作(assignment).初始值列出的成员变量，其排列次序应该和它们在class中的声明次序相同

5. Know what functions C++ silently writes and calls
    - 4 functions
        - copy Constructor
        - copy assignment operator
        - destructor
        - Constructor
   - all the functions are public and inline
   - 编译器产生出的析构函数是non-virtual 的，除非这个class的base class 声明为 virtual
   - 若声明了一个构造构函数，编译器就不会再创建default构造函数
   - C++并不允许“让reference改指向不同对象”
   - class 内含 reference 成员， const 成员时， 编译器无法生成copy Constructor.
   - base class 中 copy 为 private, 则 derived class 中也无法自动生成。

6. Explicitly disallow the use of compiler-generated functions you do not want
    - 将相应的成员函数声明为private并且不予实现
    - 使用像 Uncopyable 这样的 base class （可以把错误提早到编译期）
        ```cpp
        class Uncopyable {
        protected:
          Uncopyable() {}
          ~Uncopyable() {}
        private:
          Uncopyable(const Uncopyable&);
          Uncopyable& operator=(const Uncopyable&);
        };

        class haha : private Uncopyable {
          ...
        };
        ```

7. Declare destructors virtual in polymorphic base classes
    - polymorphic base classes 应该声明一个 virtual 析构函数。如果class带有任何 virtual 函数， 它就应该拥有一个 virtual 析构函数。
    - Classes 的设计目的如果不是作为 base classes 使用， 或不是为了具备多态性， 就不该声明 virtual destructor.

8. Prevent exceptions from leaving destructors. （还不是很懂）
    - 析构函数绝对不要吐出异常， 如果一个被析构函数调用的函数可能会抛出异常，析构函数应该捕捉任何异常，然后吞下它们（不传播）或者结束程序

9. Never call virtual functions during construction or destruction
    - 在构造和析构期间不要调用virtual函数，因为这类调用从不下降至 derived class.

10. Have assignment operators return a reference to \*this.
    - 只是一个约定而已，最好随众，为的是可以实现连续赋值的效果
11. Handle assignment to self in operator=
    ```cpp
    class Bitmap {...};
    class A {
      ...
    private:
      Bitmap* pb;
    };

    A& A::operator=(const A& rhs) {
      delete pb;
      pb = new Bitmap(*rhs.ph);
      return *this;
    }   // 当this与rhs指的是同一个区域的时候，就会出现问题
    ```
    - 两种方法： 证同测试 and "copy and swap" 法则
      1. 在操作开始之前，判断两者是否是同一个东西，如果是，就不做任何事情  // 这样简单，但是会降低速度，因为加入了一个if结构，而且会扩大代码
      2. copy and swap : 先拷贝一个副本，然后交换副本与\*this的内容

12. Copy all parts of an object.
    - 若你为class添加一个成员变量，则必须同时修改copying函数-> 以及所有构造函数（编译器不会因为你复制漏了而报错）
    - Copying 函数应该确保赋值对象内的所有成员变量“及”所有base class 成分”
        - 在派生类的拷贝构造函数中，用初始值列表显式调用积累的拷贝构造函数
        - 在派生类的assignment operator 中， 显式调用=的重载
    ```cpp
    DerivedClass::operator=(const DerivedClass& rhs) {
      BaseClass::operator=(rhs);
      ...
      return *this;
    }
    ```
    - 不要尝试以某个copying函数实现另一个copying函数。应该将共同机能放进第三个函数中，并由两个coping函数共同调用. **这个函数往往是private而且常常被命名为init**。
