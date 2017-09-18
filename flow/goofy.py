import articles
from flask import render_template, session
import random


def main(category, article_xform):
    arts = articles.tagged(category,300)
    random.shuffle(arts)
    arts = article_xform(arts)
    arts = arts[:20]
    return render_template('goofy.html', articles=arts, user=session.get('user'))
