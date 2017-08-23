docker stop blog
docker rm blog
docker build -t BeeBlog .
docker run -d -p 80:80 --name=blog BeeBlog
