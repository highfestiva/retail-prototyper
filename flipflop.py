#!/usr/bin/env python3

import articles
import behavior
from collections import OrderedDict
from flask import Flask, make_response, redirect, render_template, request, send_from_directory, session
from flask_oauth2_login import GoogleLogin
import os
import random
import sys


app = Flask(__name__)
app.config.update(
    SECRET_KEY = '=34(#ht¤os@ygv98u3.,423fgpa&/',
    GOOGLE_LOGIN_REDIRECT_SCHEME = 'http',
    GOOGLE_LOGIN_CLIENT_ID = os.environ['GOOGLE_CID'],
    GOOGLE_LOGIN_CLIENT_SECRET = os.environ['GOOGLE_CSEC'],
)
google_login = GoogleLogin(app)
locale = 'auto'
currency = 'auto'
settings = 'Layout Font Color Size Category Ordering Images'


def create_user(name, fullname, pic, gender='f', age=None):
    logged_in = (fullname != '')
    return dict(name=name, fullname=fullname, avatar=pic, gender=gender, age=age, logged_in=logged_in)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('/static', 'favicon.ico', mimetype='image/x-icon')


@google_login.login_success
def login_success(token, profile):
    session['user'] = create_user(profile['given_name'], profile['name'], profile['picture'], profile['gender'][0])
    return root()


@app.route('/login')
@google_login.login_failure
def login():
    return redirect(google_login.authorization_url())


@app.route('/logout')
def logout():
    reset_user()
    return redirect('/')


def reset_user():
    session['user'] = create_user('Sign in', '', '/static/avatar.png')


@app.route('/')
def root():
    params = OrderedDict([(name,10) for name in settings.split()])
    return render_template('main.html', settings=params)


@app.route('/content', methods=['GET','POST'])
def content():
    if not session.get('user'):
        reset_user()
    params = { name:int(request.values.get(name,0)) for name in settings.lower().split() }
    theme = behavior.theme(params)
    css = behavior.css(params)
    arts = behavior.get_articles(params)
    return render_template('content.html', theme=theme, css=css, articles=arts, user=session.get('user'))


@app.route('/cart', methods=['GET'])
def get_cart():
    cart = session.get('cart')
    if not cart:
        cart = []
    arts = list(reversed([articles.find(a) for a in cart]))
    amount = sum(a['price'] for a in arts) * 100
    print('cart:', arts)
    return render_template('cart.html', articles=arts, amount=amount, currency='SEK', locale='sv')


@app.route('/cart', methods=['PUT'])
def put_in_cart():
    article_id = request.data.decode().partition('=')[2]
    print('add to cart:', article_id)
    if not article_id:
        return 'nok', 400
    cart = session.get('cart')
    if not cart:
        cart = []
    cart += [article_id]
    session['cart'] = cart
    return 'ok'


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('required args:  language currency')
        print('example:        sv       SEK')
        sys.exit(1)
    locale = sys.argv[1]
    currency = sys.argv[2]
    app.run(host='0.0.0.0', port=9000, threaded=True)
