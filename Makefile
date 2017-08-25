rebuild:
	docker stop blog
	docker rm blog
	docker build -t beeblog .
	docker run -d -p 80:80 -p 443:443 --name=blog beeblog

deploy:
	docker build -t beeblog .
	docker run -d -p 80:80 -p 443:443 --name=blog beeblog

update:
	docker cp ./templates blog:build/
	docker cp ./static blog:build/
	docker cp ./bumblebee.py blog:build/
	docker cp ./config.yml blog:build/
	docker cp ./articles blog:build/
	docker cp ./nginx/nginx.conf blog:etc/nginx/nginx.conf
	docker cp ./nginx/htmlglobal.conf blog:etc/nginx/globals/
	docker cp ./nginx/longjj.com.conf blog:etc/nginx/sites-enabled/
	docker exec -it blog bash -c 'cd /build; python3 bumblebee.py -c config.yml'