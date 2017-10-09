$.ajaxPrefilter(function(options, original_Options, jqXHR) {
    options.async = true;
});

function initSlider(slider) {
  var prevVal = {}
  slider.on('change mousemove', function () {
    var thisSlider = $(this);
    if (thisSlider.val() != (prevVal[thisSlider.attr('id')] || 0)) {
      prevVal[thisSlider.attr('id')] = thisSlider.val();
      slider.first().trigger('slide');
    }
  });
}

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

$(function() {
  initSlider($('.slider'));
  $('.slider').on('slide', loadContent);
  loadContent();
});
