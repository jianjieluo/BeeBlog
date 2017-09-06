#!usr/bin/python3

"""
bumblebee.py - A sample static website generater writen in python for Johnny Law's blog
"""

import os
from io import open
import shutil
import yaml
import argparse
import sys
from distutils import dir_util

from jinja2 import FileSystemLoader, Environment

import mistune
from mistune_contrib.toc import TocMixin
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

# use the script from the docs of mistune http://mistune.readthedocs.io/en/latest/
class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)

class TocRenderer(TocMixin, HighlightRenderer):
    pass

def parse_file_name(name):
    name = name.replace(' ', '-')
    name = name.replace('_', '-')

    title = ''
    date = ''
    path_layer = []
    temp = os.path.splitext(name)[0]
    if (name.lower().endswith(('.md', '.markdown'))):
        title = temp[11:].replace('-', ' ')
        date = temp[0:10]
        path_layer = [temp[0:4],
            temp[0:7].replace('-','/'),
            temp[0:10].replace('-','/'),
            temp[0:10].replace('-','/')+'/'+temp[11:]
        ]
    return path_layer, title, date

def load_posts_config(config):
    metadata = {}
    for c in os.listdir(config['articles']['config']):
        cpath = os.path.join(config['articles']['config'], c)
        with open(cpath, 'r', encoding='utf-8') as infile:
            meta = yaml.safe_load(infile)
            metadata[meta['post_id']] = meta
    return metadata

if __name__ == '__main__':
    # Grab commandline arguments and process them
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config",
                        help="Specify a configuration file",
                        required=True)
    args = parser.parse_args()

    # Open specified config file and load as yaml or error
    try:
        cfh = open(args.config, "r", encoding='utf-8')
    except:
        sys.stderr.write("Could not open file: {0}\n".format(args.config))
        sys.exit(1)
    config = yaml.safe_load(cfh)
    cfh.close()

    SITES = {}
    
    article_infos = load_posts_config(config)
    article_content = {}
    tags = {}

    # STEP 1 and 2 - read files and markup
    renderer = HighlightRenderer()
    markdown = mistune.Markdown(renderer=renderer)

    # use these to reverse in the index template
    post_ids = []

    for post_id in article_infos:
        file_name = article_infos[post_id]['file']
        fqp = os.path.join(config['articles']['posts'], file_name)

        post_ids.append(post_id)

        for tag in article_infos[post_id]['tags']:
            if tag not in tags:
                tags[tag] = [post_id]
            else:
                tags[tag].append(post_id)

        # grep special_columns infos
        if article_infos[post_id]['column'] is not -1:
            c = article_infos[post_id]['column']
            if c not in config['special_columns']:
                raise AttributeError('No such a special column! ', c)
            else:
                config['special_columns'][c]['post_ids'].append(post_id)

        article_infos[post_id]['path_layer'], article_infos[post_id]['title'], \
        article_infos[post_id]['date'] = parse_file_name(file_name)

        with open(fqp, 'r', encoding='utf-8') as infile:
            text = infile.read().replace('[toc]', '')

            toc = TocRenderer()
            md = mistune.Markdown(renderer=toc)
            toc.reset_toc()
            content_md2html = md.parse(text)
            table = toc.render_toc(level=3)

            # reduce tag label written in marxico
            index = content_md2html.find('<h1')

            if index < 0:
                article_content[post_id] = table + content_md2html
            else:
                article_content[post_id] = table + content_md2html[index:]

    # STEP 3 - template
    env = Environment(loader=FileSystemLoader(config['templates_dir']))

    # generate the index page
    template = env.get_template("index.html")

    # sort all the post_id
    post_ids.sort()
    for tag in tags:
        tags[tag].sort()

    SITES['index.html'] = template.render(
        author = {
            'name': config['author']['name'],
            'photo': config['author']['photo'],
            'introduction': config['author']['introduction'],
            'github': config['author']['github'],
            'zhihu': config['author']['zhihu']
        },
        site=config['site'],
        tags=tags,
        article_infos=article_infos,
        post_ids=post_ids,
        page_type='index',
        columns=config['special_columns']
    )

    # generate the article page
    for post_id in article_content:
        t = env.get_template("article.html")
        SITES[article_infos[post_id]['path_layer'][-1]+'/index.html'] = t.render(
            article=article_infos[post_id],
            article_content = article_content[post_id],
            site=config['site'],
            page_type='article',
            tags=tags,
            columns=config['special_columns']
        )

    # generate about.html
    template = env.get_template('about.html')
    SITES['about.html'] = template.render(
        author = {
            'name': config['author']['name'],
            'photo': config['author']['photo'],
            'introduction': config['author']['introduction'],
            'github': config['author']['github'],
            'zhihu': config['author']['zhihu']
        },
        sitetitle='About the Author',
        site=config['site'],
        page_type='about',
        tags=tags,
        columns=config['special_columns']
    )

    # generate archive.html
    template = env.get_template('archive.html')
    SITES['archive.html'] = template.render(
        sitetitle='Johnny Law\'s Blog Archive',
        class_type='Archive',
        article_infos=article_infos,
        post_ids=post_ids,
        site=config['site'],
        page_type='archive',
        tags=tags,
        columns=config['special_columns']
    )

    # generate tags pages
    template = env.get_template('archive.html')
    for tag in tags:
        SITES['tags/'+tag+'/index.html'] = template.render(
            sitetitle='Blog Classification: ' + tag,
            class_type=tag,
            article_infos=article_infos,
            post_ids=tags[tag],
            site=config['site'],
            page_type='archive',
            tags=tags,
            columns=config['special_columns']
        )

    # generate columns pages
    template = env.get_template('archive.html')
    for c in config['special_columns']:
        config['special_columns'][c]['post_ids'].sort()
        SITES['columns/'+c+'/index.html'] = template.render(
            sitetitle='Blog Special-Column: ' + c,
            description=config['special_columns'][c]['description'],
            class_type=c,
            article_infos=article_infos,
            post_ids=config['special_columns'][c]['post_ids'],
            site=config['site'],
            page_type='archive',
            tags=tags,
            columns=config['special_columns']
        )

    # STEP 4 - write
    # remove output directory if it exists
    if os.path.exists(config['output_dir']):
        shutil.rmtree(config['output_dir'])

    # create empty output directory
    os.makedirs(config['output_dir'])

    # make all the possible dir
    for post_id in article_infos:
        for p in article_infos[post_id]['path_layer']:
            directory = os.path.join(config['output_dir'], p)
            if not os.path.exists(directory):
                os.makedirs(directory)
    
    if not os.path.exists(os.path.join(config['output_dir'], 'tags')):
        os.makedirs(os.path.join(config['output_dir'], 'tags'))

    for tag in tags:
        directory = os.path.join(config['output_dir'], 'tags', tag)
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    if not os.path.isdir(os.path.join(config['output_dir'], 'columns')):
        os.makedirs(os.path.join(config['output_dir'], 'columns'))

    for c in config['special_columns']:
        directory = os.path.join(config['output_dir'], 'columns', c)
        if not os.path.isdir(directory):
            os.makedirs(directory)

    # generate the sites
    for post in SITES:
        fqp = os.path.join(config['output_dir'], post)
        with open(fqp, "w", encoding="utf-8") as output:
            output.write(SITES[post])
    
    dir_util.copy_tree(config['static_dir'], config['output_dir'] + "/static")

    print ("Done!")