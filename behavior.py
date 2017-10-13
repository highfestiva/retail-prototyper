import articles
from functools import partial
import random


_css = '''
html,body,h1,h2,h3,p,div,span {
	font-family: {font-family};
    margin: 0;
    padding: 0;
    color: #{color1};
}
html,body {
    font-size: {font-size}px;
}
h1,h2,h3,p,div {
    font-weight: 100;
    margin: 0;
    padding: 0;
}
.bar {
    transform: {bar-transform};
    z-index: 10;
    {bar-setup};
    background-color: #{color0};
}
.user {
    position: relative;
    top: 6px;
}
.user > .name {
    position: relative;
    top: 10px;
    left: 78px;
    color: #{color1};
}
.user > .logout {
	position: absolute;
    top: 27px;
    left: 79px;
	font-size: 75%;
}
.avatar {
	position: absolute;
	height: 40px;
	left: 20px;
	border-radius: 30px;
	border: 4px solid #ddd;
}
.header {
    text-align: center;
    margin-top: -20px;
    width: 100%;
    height: 64px;
    display: table;
}
.header > h1 {
    display: table-cell;
    vertical-align: middle;
}
.cart-container {
	position: fixed;
	{cart-align}: 0;
    z-index: 20;
}
.cart {
	position: absolute;
	{cart-align}: 0;
	padding: {cart-padding};
	background-color: #{color0};
	border-radius: 0 0 0 20px;
	border: {cart-border-col};
	border-top: none;
	border-right: none;
	z-index: 10;
    transform: {cart-transform};
}
.articles {
	margin: {articles-margin};
	width: 94%;
}
.article-group {
    {article-group-align}
    width: {group-width}px;
    //height: {group-height}px;
    vertical-align: top;
}
.article-container {
	float: left;
    margin: 3px 2px;
	border: 1px solid #fff;
	cursor: pointer;
    vertical-align: top;
}
.article-container:hover {
	border: 1px solid #ddd;
}
.article {
	position: relative;
}
.article-big img {
    height: {big-height}px;
}
.article-small img {
    height: {small-height}px;
}
.article > .add, .article .article-price, .article > .article-description {
	visibility: hidden;
}
.article:hover > .add, .article:hover .article-price, .article:hover > .article-description {
	visibility: visible;
}
.article:active > .add {
	border-color: #0a4;
	background: #0a4;
}
.article-vitals {
    position: relative;
}
.article-name, .article-price, .article-description {
	position: absolute;
	color: #fff;
	background: #000;
	padding: 0 20px 1px 4px;
	border-radius: 3px;
	transform: skew(-15deg);
	opacity: 0.8;
	z-index: 1;
}
.article-name {
	left: 0;
    bottom: 0;
}
.article-price {
	right: 0;
    bottom: 0;
    background-color: #029;
    {article-price-xform}
}
.article-description {
	transform: none;
    text-align: justify;
    z-index: 5;
}
.article > .article-description {
	transform: none;
    {article-desc-setup}
}
.add {
	height: 40px;
	width: 40px;
	position: absolute;
    right: 0;
	border: 8px solid #0c7;
	background: #0c7;
	border-radius: 11px 0 11px 20px;
	margin: -1px -1px 0 291px;
	z-index: 5;
}
.add:hover {
	border-color: #3e5;
	background: #3e5;
}
.add:after {
	content: '';
	display: block;
	position: absolute;
	top: 50%;
	width: 40px;
	margin-top: -5px;
	height: 10px;
	background: #fff;
}
.add:before {
	content: '';
	display: block;
	position: absolute;
	top: 0;
	left: 50%;
	margin-left: -5px;
	width: 10px;
	height: 40px;
	background: #fff;
}
.image-0 {
	opacity: 1;
}
.image-1 {
	opacity: 0;
	position: absolute;
	top: 0;
	left: 0;
}
.article:hover > .image-0 {
	opacity: 0;
	transition: opacity 0.4s;
}
.article:hover > .image-1 {
	opacity: 1;
	transition: opacity 0.4s;
}
.foot {
	color: #999;
	text-align: center;
	margin: 20px;
}
.foot>span {
	color: #eee;
	margin: 5px;
}

.cart-pop-content {
    padding: 10px;
}
.cart-pop {
	position: relative;
    top: {cart-pop-top};
	{cart-pop-horiz};
	background: #fff;
	border-radius: 20px;
	border: 3px solid #555;
	padding: 20px;
	z-index: 20;
}
.cart-pop-arrow {
	width: 0;
	height: 0;
    {cart-pop-arrow-setup}
}
.cart-article > div {
	display: inline-block;
	vertical-align: middle;
    color: #555;
}
.cart-article-name {
    width: 150px;
    padding-right: 10px;
}
.cart-article-price {
    width: 40px;
}
.cart-image>img {
	height: {cart-image-height}px;
}
.cart-article-button {
	width: 20px;
	height: 20px;
	border-radius: 10px;
	margin: 10px;
	cursor: pointer;
}
.cart-article-button-a {
	background: #1aa732;
}
.cart-article-button-b {
	background: #7413cc;
}
.cart-article-button-c {
	background: #f16d4f;
}
.cart-article-button-d {
	background: #0d0644;
}
.open-payment {
    margin: 0;
    text-align: right;
}'''


bar_top_css = '''
    margin-bottom: 10px;'''

bar_left_css = '''
    position: fixed;
    width: 101vh;
    height: 76px;
    margin-top: -38px;'''


article_desc = '''
    position: relative;
    visibility: visible;
    opacity: 1;
    border-radius: 0;
    background-color: #fff;
    color: #{color2};'''


cart_pop_arrow_top = '''
	margin: -33px 6px;
	float: right;
	border-left: 10px solid transparent;
	border-right: 10px solid transparent;
	border-bottom: 10px solid #555;'''

cart_pop_arrow_left = '''
	margin: -5px -33px;
	float: left;
	border-top: 10px solid transparent;
	border-bottom: 10px solid transparent;
	border-right: 10px solid #555;'''


def get_articles(session, params):
    tags = articles.all_tags()
    # Category selection.
    category = params['category']
    cnt_idx = category % len(tags)
    if cnt_idx < len(tags):
        tag = tags[category]
        arts = articles.tagged(tag, 300)
    else:
        arts = [a for a in articles.all_articles][:300]
    # Ordering.
    ordering = params['ordering']
    if ordering == 0:
        hist = session.get('histogram')
        if hist:
            def cmphist(h1, art):
                diff = 1e5
                if 'histogram' in art:
                    h2 = art['histogram']
                    print('article histogram:', h2)
                    for (r1,g1,b1),(r2,g2,b2) in zip(h1,h2):
                        diff += (r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2
                return diff
            print('session histogram:', hist)
            arts = sorted(arts, key=partial(cmphist, hist))
    elif ordering == 1:
        pass
    elif ordering == 2:
        arts = list(reversed(arts))
    elif ordering == 3:
        random.shuffle(arts)
    else:
        arts = arts[10*ordering:]
    layout = params['layout']
    cnt = 20 if not layout//2%2 else 71
    return arts[:cnt]


def group_articles(params, articles):
    layout = params['layout']
    if not layout//2%2:
        return [[a] for a in articles]
    # grouped layout
    locations = (3, 7, 14)
    groups = [[]]
    for a in articles:
        groups[-1] += [a]
        if len(groups) in locations:
            groups += [[]]
        elif len(groups[-1]) == 4:
            groups += [[]]
    return groups


def interesting_good(session, article_id):
    '''Some customer showed interest in article_id. That information could be used in any elaborate way, but in
       this scenario we only look at the color histogram, assuming the customer will be interesting in similar-colored
       articles. That assumption is probably flawed in pretty much all of retail, including the clothing industry,
       but it makes for a good demo-able effect.'''
    art = articles.all_articles[article_id]
    if 'histogram' in art:
        lerp = lambda t,a,b: (1-t)*a + t*b
        hist = from_hist = art['histogram']
        if 'histogram' in session:
            from_hist = session['histogram']
        hist = [[lerp(0.5,v1,v2) for v1,v2 in zip(h,fh)] for h,fh in zip(hist,from_hist)] # lerp all rgbs
        session['histogram'] = hist


def css(params):
    ss = _css
    layout = params['layout']
    font = params['font']
    col = params['color']
    size = params['size']
    ss = idx_replace(ss, 'bar-transform',          layout%2,    'none~translateX(-50%) rotate(-90deg) translate(-50%,38px)')
    ss = idx_replace(ss, 'bar-setup',              layout%2,    bar_top_css + '~' + bar_left_css)
    ss = idx_replace(ss, 'cart-align',             layout%2,    'right~left')
    ss = idx_replace(ss, 'cart-padding',           layout%2,    '15px 25px~10px 3px')
    ss = idx_replace(ss, 'cart-border-col',        layout%2,    '3px solid #555~none')
    ss = idx_replace(ss, 'cart-pop-top',           layout%2,    '70px~10px')
    ss = idx_replace(ss, 'cart-pop-horiz',         layout%2,    'right: 10px~left: 80px')
    ss = idx_replace(ss, 'cart-pop-arrow-setup',   layout%2,    cart_pop_arrow_top + '~' + cart_pop_arrow_left)
    ss = idx_replace(ss, 'articles-margin',        layout%2,    'auto~0 0 0 100px')
    ss = idx_replace(ss, 'article-price-xform',    layout%2,    '~transform: translate(18px,-18px) rotate(-90deg);')
    ss = idx_replace(ss, 'article-group-align',    layout//2%2, 'display: inline-block;~float: left;')
    ss = idx_replace(ss, 'article-desc-setup',     layout//4,   'margin-top: 5px;~' + article_desc)
    ss = idx_replace(ss, 'color0',                 col//2%4,    'fff~222~fa9~fcf')
    ss = idx_replace(ss, 'color1',                 col//2%4,    '222~fff~422~424')
    ss = idx_replace(ss, 'color2',                 col//2%4,    '222~222~f86~f4f')
    ss = idx_replace(ss, 'font-family',            font,        "'Segoe UI Light'~'Calibri Light'~'Yu Gothic'~Arial~'Times New Roman'~'Courier New'~'Lucinda Console'~Gothic~sans-serif")
    ss,bh = idx_pick(ss, 'big-height',             size,        '405~445~485~365~325~301~285~271~263~241')
    ss = idx_replace(ss, 'small-height',           size,        '198.5~218.5~238.5~178.5~158.5~146.5~138.5~131.5~127.5~116.5')
    bh = int(bh)
    ss = ss.replace('{group-width}', str(int((bh+8)*0.853)))
    ss = ss.replace('{font-size}', str(bh/29))
    ss = ss.replace('{cart-image-height}', str(int(bh/5.7)))
    return ss


def theme(params):
    color = params['color']
    if color&1:
        return 'dark'
    return 'light'


def idx_pick(ss, name, idx, alternatives):
    alts = alternatives.split('~')
    try:
        outp = alts[idx]
    except:
        outp = alts[0]
    return ss.replace('{%s}'%name, outp), outp


def idx_replace(ss, name, idx, alternatives):
    return idx_pick(ss, name, idx, alternatives)[0]
