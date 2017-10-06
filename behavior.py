import articles
import random


_css = '''
html,body,h1,h2,h3,p,div,span {
	font-family: {font_family};
    margin: 0;
    padding: 0;
}
h1,h2,h3,p,div {
    font-weight: 100;
    margin: 0;
    padding: 0;
}
.bar {
    transform: {bar_transform};
    z-index: 10;
}
.user {
    position: relative;
    top: 6px;
}
.user > .name {
    position: relative;
    top: 10px;
    left: 78px;
    color: #999;
}
.user > .logout {
	position: relative;
	top: 20px;
	left: 78px;
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
	right: 0;
    z-index: 10;
}
.cart {
	position: absolute;
	right: 0;
	padding: 15px 25px;
	background-color: #fff;
	border-radius: 0 0 0 20px;
	border: 3px solid #555;
	border-top: none;
	border-right: none;
	z-index: 10;
}
.articles {
	margin: auto;
	width: 95%;
}
.article-container {
	display: inline-block;
	border: 1px solid #fff;
	cursor: pointer;
}
.article-container:hover {
	border: 1px solid #ddd;
}
.article {
	position: relative;
}
.article > .add, .article > .article-price, .article > .article-description {
	visibility: hidden;
}
.article:hover > .add, .article:hover > .article-price, .article:hover > .article-description {
	visibility: visible;
}
.article:active > .add {
	border-color: #0a4;
	background: #0a4;
}
.article-name, .article-price, .article-description {
	position: absolute;
	color: #fff;
	background: #000;
	padding: 0 20px 1px 4px;
	border-radius: 3px;
	transform: skew(-15deg);
	opacity: 0.8;
	margin-top: -22px;
	z-index: 1;
}
.article-name {
	left: 0;
}
.article-price {
	right: 0;
}
.article-description {
	margin-top: 5px;
	transform: none;
}
.add {
	height: 40px;
	width: 40px;
	position: absolute;
	border: 8px solid #0c7;
	background: #0c7;
	border-radius: 11px 0 11px 20px;
	margin: -1px 0 0 291px;
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
    top: 70px;
	right: 10px;
	background: #fff;
	border-radius: 20px;
	border: 3px solid #555;
	padding: 20px;
	z-index: 20;
}
.cart-pop-arrow {
	margin: -33px 6px;
	float: right;
	width: 0; 
	height: 0; 
	border-left: 10px solid transparent;
	border-right: 10px solid transparent;
	border-bottom: 10px solid #555;
}
.cart-article > div {
	display: inline-block;
	vertical-align: middle;
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
    return arts[:20]


def css(params):
    layout = params['layout']
    font = params['font']
    try:    bar_transform = 'none#translateX(-50%) rotate(-90deg) translate(-50%,38px)'.split('#')[layout]
    except: bar_transform = 'none'
    try:    font_family = "'Segoe UI Light'#'Calibri Light'#'Yu Gothic'#Arial#'Times New Roman'#'Courier New'#'Lucinda Console'#Gothic".split('#')[font]
    except: font_family = "sans-serif"
    return _css.replace('{font_family}', font_family).replace('{bar_transform}', bar_transform)


def theme(params):
    color = params['color']
    if color&1:
        return 'dark'
    return 'light'
