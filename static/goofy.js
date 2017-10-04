function showCart() {
  $.get('/cart', function(data) {
    $('.cart-pop-content').html(data);
    $('.cart-pop').fadeToggle();
  });
}

function showCartAutoHide() {
  showCart();
  setTimeout(function() {
    if ($('.cart-pop').is(':visible')) {
      $('.cart-pop').fadeToggle();
    }
  }, 10000);
}

$(document).click(function(e) {
  if (!$(e.target).parents().is('.cart-pop')) {
    $('.cart-pop').hide();
  }
});

$(document).ready(function(){
  $('.article').on('click', function () {
    placeInCart($(this), showCartAutoHide, 0,0, '400px', '0.4', 0, 30, 75, 1000);
  });
  $('.cart').on('click', function () {
    showCart();
  });
});
