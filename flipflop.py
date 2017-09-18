#!/usr/bin/env python3

from flask import Flask, make_response, redirect, request, send_from_directory, session
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
store = None


def create_user(name, fullname, pic, gender='f', age=None):
    return dict(name=name, fullname=fullname, avatar=pic, gender=gender, age=age)


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


def userpick(user, func):
    if not user:
        user = create_user(None, None)
    return eval(open('data/'+func+'-'+store+'.py').read(), globals(), locals())


def get_flow(category):
    if not 'user' in session:
        session['user'] = create_user('Anonymous', '', '/static/avatar.png')
    user = session['user']
    if 'flow' not in session:
        session['flow'] = userpick(user, 'flow')
    if not category:
        category = userpick(user, 'category')
    article_xform = lambda x:x
    return session['flow'], category, article_xform


@app.route('/')
@app.route('/<category>')
@app.route('/<category>/<subcat>')
def root(category='', subcat=''):
    if subcat:
        category += '/' + subcat
    flow, category, article_xform = get_flow(category)
    flow_set = flow = request.cookies.get('flow')
    if not flow:
        flow = random.choice('goofy little'.split())
    mod = getattr(__import__('flow.'+flow), flow)
    r = getattr(mod, 'main')(category, article_xform)
    if not flow_set:
        r = make_response(r)
        r.set_cookie('flow', flow)
    return r


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('required arg: store (for instance "hm")')
        sys.exit(1)
    store = sys.argv[1]
    app.run(host='0.0.0.0', port=9000, threaded=True)
