$(document).ready(function(){
  $('.article').on('click', function () {
    var cart = $('.cart')[0];
    var dragImg = $(this).find('img');
    var imgclone = dragImg.clone()
    .offset({
      top: dragImg[0].getBoundingClientRect().top,
      left: dragImg[0].getBoundingClientRect().left
    })
    .css({
      'position': 'fixed',
      'height': '200px',
      'z-index': '100'
    })
    .appendTo($('body'))
    .animate({
      'opacity': '0.2',
      'top': cart.getBoundingClientRect().top,
      'left': cart.getBoundingClientRect().left + 10,
      'height': 75
    }, 1000, 'easeOutCubic', function () {
      $(this).detach()
    });
  });
});
