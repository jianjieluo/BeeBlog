# -*- coding: utf-8 -*-

"""
bumblebee.py - A sample static website generater writen in python for Johnny Law's blog
"""

import os
from io import open
import shutil
import yaml

from jinja2 import FileSystemLoader, Environment

import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

ARTICLES_DIR = "./articles"
TEMPLATE_DIR = "./templates"
SITE_DIR = "site"


# use the script from the docs of mistune http://mistune.readthedocs.io/en/latest/
class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)

if __name__ == '__main__':
    ARTICLES = {}
    SITES = {}

    # STEP 1 - read files
    for current in os.listdir(ARTICLES_DIR):
        fqp = os.path.join(ARTICLES_DIR, current)
        
        curr_name = ''
        if (current.lower().endswith(('.md', '.markdown'))):
            curr_name = os.path.splitext(current)[0] + '.html'

        with open(fqp, 'r', encoding='utf-8') as infile:
            ARTICLES[curr_name] = infile.read()

    # STEP 2 - markup
    renderer = HighlightRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    for post in ARTICLES:
        ARTICLES[post] = {
            'title': os.path.splitext(post)[0],
            'postdate': '2017-06-29',
            'updatedate': '2017-07-02',
            'content': markdown(ARTICLES[post])
        }

    # STEP 3 - template
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

    # generate the index page
    template = env.get_template("index.html")
    SITES['index.html'] = template.render(
        data={
            'sitetitle': 'Johnny Law\'s Blog Home',
            'PS': 'Study at Sun Yat-sen University, China'
        },
        article_list=ARTICLES
    )

    # generate the article page
    for post in ARTICLES:
        template = env.get_template("article.html")
        SITES[post] = template.render(
            article={
                'title': ARTICLES[post]['title'],
                'content': ARTICLES[post]['content']
            },
        )

    # generate about.html
    template = env.get_template('about.html')
    SITES['about.html'] = template.render(
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
            
    for post in SITES:
        fqp = os.path.join(SITE_DIR, post)

        with open(fqp, "w", encoding="utf-8") as output:
            output.write(SITES[post])

    print "Done!"
