import articles
from flask import render_template
import random


def main():
    arts = articles.tagged('ladies')
    random.shuffle(arts)
    arts = arts[:55]
    highlights = random.sample(arts[:10]+arts[20:30]+arts[45:55], 3)
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
    return render_template('little.html', article_groups=article_groups)
