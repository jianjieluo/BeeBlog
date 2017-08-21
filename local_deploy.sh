docker stop blog
docker rm blog
docker build -t myblog .
docker run -d -p 80:80 --name=blog myblog
