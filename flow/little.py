import articles
from flask import render_template, session
import random


def main(category, article_xform):
    arts = articles.tagged(category)
    random.shuffle(arts)
    arts = article_xform(arts)
    arts = arts[:55]
    highlights = random.sample(arts, 3)
    article_groups = []
    current_group = []
    for a in arts:
        if a in highlights:
            article_groups += [[a]]
        else:
            current_group += [a]
            if len(current_group) == 4:
                article_groups += [current_group]
                current_group = []
    if current_group:
        article_groups += [current_group]
    return render_template('little.html', article_groups=article_groups, user=session.get('user'))
