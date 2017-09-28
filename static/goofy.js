$(document).ready(function(){
  $('.article').on('click', function () {
    placeInCart($(this), 0,0, '400px', '0.4', 0, 30, 75, 1000);
  });
});
