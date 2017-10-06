import json


all_articles = {}


def load_articles():
    global all_articles
    try:
        all_articles = json.load(open('data/articles.json'))
    except Exception as e:
        print(e)


def save_articles():
    global all_articles
    try:
         json.dump(all_articles, open('data/articles.json', 'w'))
    except Exception as e:
        print(e)


def add(article):
	global all_articles
	all_articles[article['articleId']] = article


def find(articleId):
	return all_articles.get(articleId)


def tagged(tag, cnt=1000):
    articles = []
    for art in all_articles.values():
        if tag in art['tags']:
            articles += [art]
            if len(articles) >= cnt:
                break
    return articles


def all_tags():
    tags = set()
    for art in all_articles.values():
        tags.update(art['tags'])
    return sorted(tags)


load_articles()
