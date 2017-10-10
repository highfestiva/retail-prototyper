import articles
import random


_css = '''
html,body,h1,h2,h3,p,div,span {
	font-family: {font-family};
    margin: 0;
    padding: 0;
    color: #{color1};
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
	font-size: 11px;
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
    width: 352px;
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
.article-small img {
    height: 199px;
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
	height: 70px;
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


def get_articles(params):
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
        pass
    elif ordering == 1:
        arts = list(reversed(arts))
    elif ordering == 2:
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


def css(params):
    ss = _css
    layout = params['layout']
    font = params['font']
    col = params['color']
    ss = idx_pick(ss, 'bar-transform',          layout%2,    'none~translateX(-50%) rotate(-90deg) translate(-50%,38px)')
    ss = idx_pick(ss, 'bar-setup',              layout%2,    bar_top_css + '~' + bar_left_css)
    ss = idx_pick(ss, 'cart-align',             layout%2,    'right~left')
    ss = idx_pick(ss, 'cart-padding',           layout%2,    '15px 25px~10px 3px')
    ss = idx_pick(ss, 'cart-border-col',        layout%2,    '3px solid #555~none')
    ss = idx_pick(ss, 'cart-pop-top',           layout%2,    '70px~10px')
    ss = idx_pick(ss, 'cart-pop-horiz',         layout%2,    'right: 10px~left: 80px')
    ss = idx_pick(ss, 'cart-pop-arrow-setup',   layout%2,    cart_pop_arrow_top + '~' + cart_pop_arrow_left)
    ss = idx_pick(ss, 'articles-margin',        layout%2,    'auto~0 0 0 100px')
    ss = idx_pick(ss, 'article-price-xform',    layout%2,    '~transform: translate(18px,-18px) rotate(-90deg);')
    ss = idx_pick(ss, 'article-group-align',    layout//2%2, 'display: inline-block;~float: left;')
    ss = idx_pick(ss, 'article-desc-setup',     layout//4,   'margin-top: 5px;~' + article_desc)
    ss = idx_pick(ss, 'color0',                 col//2%4,    'fff~222~fa9~fcf')
    ss = idx_pick(ss, 'color1',                 col//2%4,    '222~fff~422~424')
    ss = idx_pick(ss, 'color2',                 col//2%4,    '222~222~f86~f4f')
    ss = idx_pick(ss, 'font-family',            font,        "'Segoe UI Light'~'Calibri Light'~'Yu Gothic'~Arial~'Times New Roman'~'Courier New'~'Lucinda Console'~Gothic~sans-serif")
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
    return ss.replace('{%s}'%name, outp)
