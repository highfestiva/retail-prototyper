import articles
from flask import render_template
import random


def main():
    arts = articles.tagged('ladies',300)
    random.shuffle(arts)
    arts = arts[:20]
    return render_template('goofy.html', articles=arts)
