# Note: This repository is deprecated, and the code is kept for reference about how to write a Static Website Generator.

# BeeBlog

![beeicons](./static/img/blogbanner.png)

**The Perfect Static Website Generator is the One You Write Yourself**. Personal Blog of Johnny Law written in python3.

Source files of http://www.longjj.com and https://www.longjj.com

## Change Log

- 2018-04-03 在 gitment 的使用过程中，发现了容易[因为题目太长而导致评论不能初始化 `Error: Validation Failed`](https://github.com/imsun/gitment/issues/116)，修改 `id` 项完成时间戳和题目名同时作为 gitment id的兼容。
- 2017-09-09 引入了第三方库[gitment](https://github.com/imsun/gitment)作为评论系统。该系统调用Github issue的API，将使得访客可以使用github帐号来进行评论，并且把评论的内容发送到本repo的Issue上。评论功能的引入还在beta测试当中，目前暂时可以稳定运行。

## Why BeeBlog

I have tried some blog frameworks like Jekyll or Hexo. However, I am always spending lots of time reading doc for some functions. Once I found that making a static site generator is not difficult I decided to build my own blog. Beeblog has no  complex plugins supports. I just implement some basic features I need. During the developing, I am learning docker and nginx.

I notice a code in the Internet and I think it's interesting while pretty right.

```python
def shouldWriteOwnStaticGenerator(person):
    if person.isPickyAboutTech():
        return "Yes"
    else:
        return "Use Jekyll"
```

So here's Beeblog. I chose the name **bumblebee** when I was watching Transformers' films :). There is no other specific meaning.

[Chinese Blog for More Detail: Why I implement BeeBlog](https://www.longjj.com/2017/09/09/%E8%87%AA%E5%B7%B1%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AABlog%E5%90%A7/)

## How it works

`bumblebee.py` is a python3 static page generator. Use docker to build an image and run `bumblebee.py` in a corresponding container. The nginx proxy in the container listens requests.

> Notice: If you are not in China, maybe you don't need to change the software sources in `sources.list`.

## Try it
Make sure you have installed docker in your system.

```bash
git clone https://github.com/longjj/BeeBlog
cd ./BeeBlog
make deploy
```

Then visit http://localhost:80 .

> Notice: If you want to use https, you need to have your own ssl key and put the \*.crt and \*.key files in `/ssl_key` dir. Then change the config in `longjj.com.conf` to use your own ssl key.

> Notice: All article filenames in the `articles` dir should obtain the format "xxxx-xx-xx-xxx-xxx-xxx.md" cause my name parser depends on the file name format.

You can also use `python3 bumblebee.py -c config_local.yml` command to test your static site generator.
You can use `make update` to update your resources in the docker container faster.

## Refference

1. [How To Write A Static Site Generator](https://screamingatmyscreen.com/2014/5/how-to-write-a-static-site-generator/) gives me a basic concept about static page generator.
2. [Benjamin Cane's blog repo](https://github.com/madflojo/blog) has pretty good code style and file structure and I learn a lot from his repo.
3. [Icon Refference](https://icons8.com/icon/50492/Bee).

## About this repo

**I hope you can get refferences and inspiration from this repo.** Welcome to fork it and try it by yourself. I recommend you to write your own blog as well. It's cool and you can practise a lot about docker, python3, nginx, web dev and even UI design, that is, a simple full stack development.

I will also maintain this repo, sometimes update my articles in the future.
