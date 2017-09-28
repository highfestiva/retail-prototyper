$(document).ready(function(){
  $('.article').on('click', function () {
    placeInCart($(this), 0,0, '200px', '0.2', 0, 10, 75, 1000);
  });
});
