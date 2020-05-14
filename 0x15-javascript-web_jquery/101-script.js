document.addEventListener('DOMContentLoaded', function () {
  $('#add_item').on('click', function () {
    $('.my_list').append('<li>Item</li>');
  });

  $('#remove_item').on('click', function () {
    $('ul li:last-child').remove();
  });

  $('#clear_list').on('click', function () {
    $('ul li').remove();
  });
});
