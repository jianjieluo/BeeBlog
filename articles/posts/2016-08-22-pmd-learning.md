java静态代码检查工具——pmd的使用笔记
===

`选择了pmd作为Matrix的java语言静态检查工具，以下是初步的pmd在ubuntu环境下的使用笔记。`

---
## 1.概述
静态代码检查对于提高代码质量，减少后期对于代码的维护成本有着十分重要的作用，其详细的重要性在这里就不赘述。

### why pmd?
java的代码检查工具并不少，比较主流的有pmd,checkstyle,sonarlint等等，其中，checkstyle只是检查代码风格，pmd和sonarlint的内容和oclint的检查方面非常类似。sonarlint-cli是sonar的一个分支项目，提供的内容十分全面，输出格式html非常炫酷，阅读起来非常方便，但是由于它的github项目开始不久，格式提供并不丰富，难以集成在第三方的软件中，所以sonarlint-cli更加适合于直接的java develop。想比较而言pmd相对成熟，输出虽然没有Matrix想要的json格式，但是也有比较方便处理的xml格式，所以最终选择它。

### 使用方法
pmd可以作为插件集成在eclipse等ide下使用，也可以在linux和windows下的命令行下直接使用，由于需求需要此处只说明pmd在linux下的使用方法。

### Installation
pmd的下载使用，只需要通过官网下载二进制的发行版即可以使用。

>[链接](https://pmd.github.io/pmd-5.5.1/usage/installing.html)

（ps:自行编译pmd的话需要用到maven。）

### 规则文件
pmd通过自己的规则文件(.xml)进行静态检测，pmd内置有30余种规则，用户可以选择自己需要的规则，也可以自己制定规则，这给pmd的使用带来了很大的自由性。

pmd的内置规则暂时够用，还没有能够完全弄懂自行编译规则的全部方法，给出**[官方链接](https://pmd.github.io/pmd-5.5.1/customizing/howtowritearule.html)**

---
## 2.Command Line Usage

` ./run.sh pmd -d [filename|jar or zip file containing source code|directory] -f [report format] -R [ruleset file] [other options]`


### 常用的几个参数

+ -dir / -d  : 需要检测的代码所在的文件夹
+ -rulesets / -R : 检测java的规则文件
+ -format / -f
+ -help : 帮助文档
+ -shortnames ： 	Prints shortened filenames in the report.
+ -stress / -S ： Performs a stress test.
- -minimumpriority / -min： 设置问题priority的范围，最低的范围默认是5
- -reportfile / -r： 	Send report output to a file; default to System.out
- -version / -v ： Specify version of a language PMD should use.

### 样例运行

#### 待测代码
```
# 结构
simple_Test/
├── ComplexJava.java
├── test2.java
└── test.java
0 directories, 3 files
```

```java
class ComplexJava {
  public static void main(String[] args) {
    System.out.println("Hello Java");
    boolean flag = true;
    if (!flag) {
      // do something
    }
    for (int i = 0; i < 10; ++i) {
      // do something
    }
    if (flag) {

    }
    String s = "Hello";
    if ("Hello".equals(s)) {

    }
    if (false) {}
    if (true) {}
    if (false) {}
    if (true) {}
    if (false) {}
  }
}
```

```java
public class test2 {
  public void count(int n) {
    for (int i = 0; i < n; ++i) {
      System.out.println(i);
    }
    if (false) {
      System.out.println("hehe");
    }
  }
}
```

#### 运行命令及结果

```shell
./pmd-bin-5.5.1/bin/run.sh pmd -d simple_Test/ -R ./java_rulesets/basic.xml

/home/longj/simple_Test/ComplexJava.java:18:Do not use if statements that are always true or always false
/home/longj/simple_Test/ComplexJava.java:19:Do not use if statements that are always true or always false
/home/longj/simple_Test/ComplexJava.java:20:Do not use if statements that are always true or always false
/home/longj/simple_Test/ComplexJava.java:21:Do not use if statements that are always true or always false
/home/longj/simple_Test/ComplexJava.java:22:Do not use if statements that are always true or always false
/home/longj/simple_Test/test2.java:7:	Do not use if statements that are always true or always false
```

### 处理输出
pmd 通过 -r 参数可以指定结果输出到的文件，-f参数可以指定输出格式，常用格式有

- codeclimate: Renderer for Code Climate JSON format.
- emacs: GNU Emacs integration.
- html: HTML format.
- text: Text format.
- textcolor: Text format, with color support (requires ANSI console support, e.g. xterm, rxvt, etc.).
- xml: XML format.

（其他输出可以参考[官方文档](https://pmd.github.io/pmd-5.5.1/usage/running.html)）

> 这里主要使用处理起来比较方便的codeclimate和xml格式输出，集合两部分的所需信息。

### 用python来xmltodict模块来处理xml
`$ pip install xmltodict`

[github address](https://github.com/martinblech/xmltodict)

```python
import xmltodict, json

if __name__=="__main__":
  file_object = open("result.xml")
  o = xmltodict.parse(file_object.read())
  report_file = open("report.json", "w")
  report_file.write(json.dumps(o))
  file_object.close()
  report_file.close()
```
先通过pmd输出到result.xml,再进行转换成为更加容易处理的json格式

处理后的部分结果如下：
```json
{
  "pmd": {
    "@version": "5.5.1",
    "@timestamp": "2016-08-13T10:45:11.992",
    "file": [
      {
        "@name": "/home/longj/simple_Test/ComplexJava.java",
        "violation": [
          {
            "@beginline": "1",
            "@endline": "24",
            "@begincolumn": "1",
            "@endcolumn": "1",
            "@rule": "CommentRequired",
            "@ruleset": "Comments",
            "@externalInfoUrl": "${pmd.website.baseurl}/rules/java/comments.html#CommentRequired",
            "@priority": "3",
            "#text": "headerCommentRequirement Required"
          },
          {
            "@beginline": "2",
            "@endline": "23",
            "@begincolumn": "17",
            "@endcolumn": "3",
            "@rule": "CommentRequired",
            "@ruleset": "Comments",
            "@class": "ComplexJava",
            "@method": "main",
            "@externalInfoUrl": "${pmd.website.baseurl}/rules/java/comments.html#CommentRequired",
            "@priority": "3",
            "#text": "publicMethodCommentRequirement Required"
          }
        ]
      },
      {
        "@name": "/home/longj/simple_Test/test2.java",
        "violation": [
          {
            "@beginline": "2",
            "@endline": "15",
            "@begincolumn": "8",
            "@endcolumn": "1",
            "@rule": "CommentRequired",
            "@ruleset": "Comments",
            "@externalInfoUrl": "${pmd.website.baseurl}/rules/java/comments.html#CommentRequired",
            "@priority": "3",
            "#text": "headerCommentRequirement Required"
          },
          {
            "@beginline": "7",
            "@endline": "7",
            "@begincolumn": "9",
            "@endcolumn": "13",
            "@rule": "UnconditionalIfStatement",
            "@ruleset": "Basic",
            "@class": "test2",
            "@method": "count",
            "@externalInfoUrl": "${pmd.website.baseurl}/rules/java/basic.html#UnconditionalIfStatement",
            "@priority": "3",
            "#text": "Do not use if statements that are always true or always false"
          }
        ]
      }
    ]
  }
}
```

---
最后再次给出pmd的[官方文档链接](https://pmd.github.io/pmd-5.5.1/usage/installing.html)

> pmd的使用方法还有很多地方值得探索，上述的用法只是非常简单的用法，但是可以勉强应付日常的开发需要。以后有机会了解更深入了就再与大家分享：）
