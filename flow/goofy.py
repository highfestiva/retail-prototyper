import articles
from flask import render_template


def main():
    return render_template('goofy.html', articles=articles.tagged('ladies',20))
