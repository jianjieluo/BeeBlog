OCLint Learning Note
===


usually used
---
for example:
```
$ oclint [options] <source> -- [compiler flags]


$ oclint sample.cpp -- -c  // for c and cpp


$ oclint -report-type html -o report.html sample.cpp -- -c


$ oclint -report-type html -o report.html JudgerChoice.cpp -- -I /usr/include/mysql++ -I/usr/include/mysql/ -I /usr/lib -I /usr/local/include/mysql++/ -w -std=c++11 -c

```

(先是要编译过了才会开始进行oclint的检查！！！！)



[Reference Tutorial](http://docs.oclint.org/en/stable/intro/tutorial.html)
