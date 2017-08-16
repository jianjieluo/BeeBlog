[toc]

Use C++11 Inheritance Control Keywords to Prevent Inconsistencies in Class Hierarchies
======================================================================================

concluded from this [article](http://blog.smartbear.com/c-plus-plus/use-c11-inheritance-control-keywords-to-prevent-inconsistencies-in-class-hierarchies/)

总结自这篇 [文档](http://blog.smartbear.com/c-plus-plus/use-c11-inheritance-control-keywords-to-prevent-inconsistencies-in-class-hierarchies/)

---

C++11 adds two inheritance control keywords: override and final. override ensures that an overriding virtual function declared in a derived class has the same signature as that of the base class. final blocks further derivation of a class and further overriding of a virtual function. Let’s see how these watchdogs can eliminate design and implementation bugs in your class hierarchies.

Virtual Functions and **override**
----------------------------------

A derived class can override a member function that was declared virtual in a base class. This is a fundamental aspect of object-oriented design. However, things can go wrong even with such a trivial operation as overriding a function. Two common bugs related to overriding virtual functions are:

-	Inadvertent overriding.
-	Signature mismatch.

In C++11, you can eliminate these two bugs by using the new keyword override. override explicitly states that a function is meant to override a base class’s virtual function. More importantly, it checks for signature mismatches between the base class virtual function and the overriding function in the derived classes. If the signatures don’t match, the compiler issues an error message.

---

When the compiler processes the declaration of H::func() it looks for a matching virtual function in a base class. Recall that “matching” in this context means:

-	Identical function names
-	A virtual specifier in the first base class that declares the function
-	Identical parameter lists, return types (with one exception), cv qualifications etc., in both the base class’s function and the derived class’s overriding function.

**If any of these three conditions isn’t met, you get a compilation error.**

Preventing the inadvertent overriding bug is trickier. In this case, it’s the lack of the keyword override that should raise your suspicion. If the derived class function is truly meant to override a base class function, it should include an explicit override specifier. Otherwise, assume that either D::func() is a new virtual function (a comment would be most appreciated in this case!), or that this may well be a bug.

---

**final** Functions and Classes
-------------------------------

The C++11 keyword final has two purposes. It prevents inheriting from classes, and it disables the overriding of a virtual function. Let’s look at final classes first.

In C++11, non-subclassable types should be declared final like this:

```cpp
class TaskManager final{/*..*/};  
class PrioritizedTaskManager: public TaskManager {
};  //compilation error: base class TaskManager is final
```

In a similar vein, you can disable further overriding of a virtual function by declaring it final. If a derived class attempts to override a final function, the compiler issues an error message:

```cpp
struct A
{
  virtual void func() const;
};
struct B: A
{
  void func() const override final; //OK
};
struct C: B
{
 void func()const; //error, B::func is final
};
```

It doesn’t matter whether C::func() is declared override. Once a virtual function is declared final, derived classes cannot override it.

---

Syntax and Terminology
----------------------

override and final become keywords in C++11, but only when used in specific contexts. Otherwise, *they are treated as plain identifiers.* The committee was reluctant to call override and final “context sensitive keywords” (which is what they truly are) though. Instead, they are formally referred to as “identifiers with special meaning.” Special indeed!

---

In Conclusion
-------------

The two new context-sensitive keywords override and final give you tighter control over hierarchies of classes, ridding you of some irritating inheritance-related bugs and design gaffes. override guarantees that an overriding virtual function matches its base class counterpart. final blocks further derivation of a class or further overriding of a virtual function. With respect to compiler support, GCC 4.7, Intel’s C++ 12, MSVC 11, and Clang 2.9 support these new keywords.
