function _(exp) {
  var iframe = $('iframe.retail-content');
  if (iframe.length != 0) {
    return $(exp, iframe.contents());
  }
  return $(exp);
}

function placeInCart(node, complete, topOff, leftOff, height, endOpacity, cartTop, cartLeft, endHeight, animTime) {
  var articleId = node.attr('data-articleId');
  $.ajax({
    type: 'PUT',
    url: '/cart',
    contentType: 'application/json',
    data: {articleId:articleId},
    complete: complete
  });
  var cart = _('.cart')[0];
  var dragImg = node.find('img').last();
  var imgclone = dragImg.clone()
  .offset({
    top: dragImg[0].getBoundingClientRect().top + topOff,
    left: dragImg[0].getBoundingClientRect().left + leftOff
  })
  .css({
    'position': 'fixed',
    'height': height,
    'z-index': '100'
  })
  .appendTo(_('.extras'))
  .animate({
    'opacity': endOpacity,
    'top': cart.getBoundingClientRect().top + cartTop,
    'left': cart.getBoundingClientRect().left + cartLeft,
    'height': endHeight
  }, animTime, 'easeOutCubic', function () {
    $(this).detach();
  });
}

function updateCart() {
  $.get('/cart', function(data) {
    _('.cart-pop-content').html(data);
  });
}

$(document).ready(function() {
  _('.article').click(function () {
    placeInCart($(this), updateCart, 0,0, '400px', '0.4', 0, 30, 75, 1000);
  });
  updateCart();
});
