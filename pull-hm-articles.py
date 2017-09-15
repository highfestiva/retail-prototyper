#!/usr/bin/env python3

import articles
import os.path
import requests
from urllib.parse import quote


urlencode = lambda url: quote(url, safe='')
urlbase = 'http://api.hm.com/v2/se/sv/products/display?categories=%s&concealCategories=true&pageSize=300&page=1&deviceType=%s'
device = 'DESKTOP'


def redirect_img(article, idx, url):
    ext = url.rsplit('.',1)[1][:3]
    filename = 'static/artimg/%s-%i.%s' % (article['articleId'].lower(), idx, ext)
    if not os.path.exists(filename):
        url = 'http:' + url
        r = requests.get(url)
        if r.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(r.content)
    url = '/' + filename
    return url


for category in ['ladies/tops', 'kids/newborn']:
    url = urlbase % (urlencode(category), device)
    categories = list(set([category] + category.split('/')))
    r = requests.get(url).json()
    for article in r['displayArticles']:
        a = { 'name':      article['name'],
              'articleId': article['articleCode'],
              'tags':      categories,
              'imgs':      [article['primaryImage']['url']] }
        if 'secondaryImage' in article:
            a['imgs'] += [article['secondaryImage']['url']]
        existing = articles.find(a['articleId'])
        if existing:
            existing['tags'] = list(set(existing['tags']+a['tags']))
            continue
        for i,url in enumerate(a['imgs']):
            a['imgs'][i] = redirect_img(a, i, url)
        articles.add(a)
    articles.save_articles()
