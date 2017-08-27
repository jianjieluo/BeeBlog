#!usr/bin/python3

import os
import yaml
import datetime
import shutil

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

def add_config(postname):
    target_path = '../articles/config'
    curr_posts_num = len(os.listdir(target_path))

    template = {
        'description': '',
        'post_id': curr_posts_num + 1,
        'tags': [],
        'file': postname,
        'keywords': [],
        'lang': '',
        'column': -1,
    }

    target = os.path.join(target_path, os.path.splitext(postname)[0]+'.yml')

    # print (template)

    with open(target, 'w', encoding='utf-8') as outfile:
        yaml.dump(template, outfile, default_flow_style=False)

if __name__ == '__main__':
    if os.path.isdir('./drafts') is not True:
        print ('No drafts dir!')
        os.makedirs('./drafts')
        exit(1)
    
    drafts = os.listdir('./drafts')
    drafts.sort()
    for x in drafts:
        filepath = os.path.join('./drafts',x)
        d = modification_date(filepath)
        pdate_str = d.strftime('%Y-%m-%d')
        
        # move the artcle to the articles dir
        tmp = x.replace(' ', '-')
        tmp = tmp.replace('_', '-')
        postname = pdate_str + '-' + tmp
        post_path = os.path.join('../articles/posts/', postname)
        shutil.copyfile(filepath, post_path)

        # add articles config
        add_config(postname)
    
    print ('Done!')