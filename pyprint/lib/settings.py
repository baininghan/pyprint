#coding: utf-8
from hashlib import md5

templates = '../templates'

db_config = {
    'type': 'sqlite',
    'username': 'root',
    'password': '123456',
    'name': 'blog',
    'port': 3306,
}

config = {
    'email': 'RicterZheng@gmail.com',
    'username': 'Ricter',
    'password': '123456',
    'title': u'初心を忘れず',
    'disqus_shortname': 'test',
}

config['email_md5'] = md5(config['email'].lower()).hexdigest()