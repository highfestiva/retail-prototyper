function loadContent() {
  var sendData = $('#sliders').serialize();
  $.post(
    '/content',
    sendData,
    function(data) {
        $('iframe.retail-content').contents().find('html').html(data);
      },
    'html');
}

$(document).ready(function(){
  $('.slider').slider({slide: loadContent});
  loadContent();
});
