docker stop blog
docker rm blog
docker build -t beeblog .
docker run -d -p 80:80 -p 443:443 --name=blog beeblog
