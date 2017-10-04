function showCart() {
  $.get(this.href, function(data) {
    $('.cart-pop-content').html(data).slideFadeToggle();
  });
}

$(document).ready(function(){
  $('.article').on('click', function () {
    placeInCart($(this), showCart, 0,0, '200px', '0.2', 0, 10, 75, 1000);
  });
});
