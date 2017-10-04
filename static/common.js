function placeInCart(node, complete, topOff, leftOff, height, endOpacity, cartTop, cartLeft, endHeight, animTime) {
  var articleId = node.attr('data-articleId');
  $.ajax({
    type: 'PUT',
    url: '/cart',
    contentType: 'application/json',
    data: {articleId:articleId},
    complete: complete
  });
  var cart = $('.cart')[0];
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
  .appendTo($('body'))
  .animate({
    'opacity': endOpacity,
    'top': cart.getBoundingClientRect().top + cartTop,
    'left': cart.getBoundingClientRect().left + cartLeft,
    'height': endHeight
  }, animTime, 'easeOutCubic', function () {
    $(this).detach();
  });
}
