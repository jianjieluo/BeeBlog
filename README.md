# BeeBlog

![beeicons](./static/img/blogbanner.png)

**The Perfect Static Website Generator is the One You Write Yourself**. Personal Blog of Johnny Law written in python3.

Source files of http://www.longjj.com and https://www.longjj.com

> Notice: 由于在中国原因，我的博客网站仍然在备案中，http协议暂时无法访问，估计2017.09左右才能正常访问。https协议的访问应该可以work。

## Why BeeBlog

I have tried some blog frameworks like Jekyll or Hexo. However, I am always spending lots of time reading doc for some functions. Once I found that making a static page generator is not difficult I decided to build my own blog. Beeblog has no  complex plugins supports. I just implement some basic features I need. During the developing, I am learning docker and nginx.

I notice a code in the Internet and I think it's interesting while pretty right.

```python
def shouldWriteOwnStaticGenerator(person):
    if person.isPickyAboutTech():
        return "Yes"
    else:
        return "Use Jekyll"
```

So here's Beeblog. I chose the name **bumblebee** when I was watching Transformers' films :). There is no other specific meaning.

## How it works

`bumblebee.py` is a python3 static page generator. Use docker to build a image and run `bumblebee.py` in a corresponding container. The nginx proxy in the container listens requests.

> Notice: If you are not in China, maybe you don't need to change the software sources in `sources.list`.

## Try it
Make sure you have installed docker in your system.

```bash
git clone https://github.com/longjj/BeeBlog
cd ./BeeBlog
bash ./local_deploy.sh
```

Then visit http://localhost:80 .

> Notice: If you want to use https, you need to have your own ssl key and put the \*.crt and \*.key files in `/ssl_key` dir. Then change the config in `longjj.com.conf` to use your own ssl key.

> Notice: All the article files name should be ASCII characters since my docker container system doesn't support utf-8. And it should obtain the format "xxxx-xx-xx-xxx-xxx-xxx.md" cause my name parser depends on the file name format.

## Refference

1. [How To Write A Static Site Generator](https://screamingatmyscreen.com/2014/5/how-to-write-a-static-site-generator/) gives me a basic concept about static page generator.
2. [Benjamin Cane's blog repo](https://github.com/madflojo/blog) has pretty good code style and file structure and I learn a lot from his repo.
3. [Icon Refference](https://icons8.com/icon/50492/Bee).

## About this repo

**I hope you can get refferences and inspiration from this repo.** Welcome to fork it and try it by yourself. I recommend you to write your own blog as well. It's cool and you can practise a lot about docker, python3, nginx, web dev and even UI design, that is, a simple full stack development.

I will also maintain this repo, sometimes update my articles in the future.
