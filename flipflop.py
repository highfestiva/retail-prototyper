#!/usr/bin/env python3

from flask import Flask, request, make_response


app = Flask(__name__)


@app.route('/')
@app.route('/<func>')
def root(func='main'):
    flow_set = flow = request.cookies.get('flow')
    if not flow:
        flow = 'goofy'
    mod = getattr(__import__('flow.'+flow), flow)
    print(mod)
    r = getattr(mod, func)()
    if not flow_set:
        r = make_response(r)
        r.set_cookie('flow', flow)
    return r


app.run(host='0.0.0.0', port=9000, threaded=True)