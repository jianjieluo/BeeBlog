# -*- coding: utf-8 -*-

"""
bumblebee.py - A sample static website generater writen in python for Johnny Law's blog
"""

import os
from io import open
import shutil
import yaml

from markdown2 import markdown
from jinja2 import FileSystemLoader, Environment

ARTICLES_DIR = "./articles"
TEMPLATE_DIR = "./templates"
SITE_DIR = "site"

if __name__ == '__main__':
    ARTICLES = {}
    STATICPAGES = {}

    # STEP 1 - read files
    for current in os.listdir(ARTICLES_DIR):
        fqp = os.path.join(ARTICLES_DIR, current)
        
        curr_name = ''
        if (current.lower().endswith(('.md', '.markdown'))):
            curr_name = os.path.splitext(current)[0] + '.html'

        with open(fqp, 'r', encoding='utf-8') as infile:
            ARTICLES[curr_name] = infile.read()

    # STEP 2 - markup
    for post in ARTICLES:
        ARTICLES[post] = markdown(ARTICLES[post])

    # STEP 3 - template
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

    # generate the article page
    for post in ARTICLES:
        template = env.get_template("article.html")
        ARTICLES[post] = template.render(
            article={
                'title': os.path.splitext(post)[0],
                'content': ARTICLES[post]
            },
        )
    
    # generate other pages
    template = env.get_template("index.html")
    STATICPAGES['index.html'] = template.render(
        data = {
            'sitetitle': 'Johnny Law\'s Blog Home',
            'PS': 'Study at Sun Yat-sen University, China'
        },
        article_list = ARTICLES
    )

    template = env.get_template('about.html')
    STATICPAGES['about.html'] = template.render(
        author = {
            'name': 'Johnny Law',
            'photo': '../static/img/longj_photo.png',
            'introdution': 'Study at Sun Yat-sen University',
            'github': 'https://github.com/longjj',
            'email': 'luojj26@mail2.sysu.edu.cn'
        }
    )

    # STEP 4 - write
    # remove output directory if it exists
    if os.path.exists(SITE_DIR):
        shutil.rmtree(SITE_DIR)

    # create empty output directory
    os.makedirs(SITE_DIR)

    for post in ARTICLES:
        fqp = os.path.join(SITE_DIR, post)

        with open(fqp, "w", encoding="utf-8") as output:
            output.write(ARTICLES[post])
            
    for post in STATICPAGES:
        fqp = os.path.join(SITE_DIR, post)

        with open(fqp, "w", encoding="utf-8") as output:
            output.write(STATICPAGES[post])

    print "Done!"
