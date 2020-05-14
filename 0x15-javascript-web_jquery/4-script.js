$('#toggle_header').on('click', function () {
  const head = $('header');
  if (head[0].className === 'green') {
    $('header').removeClass();
    $('header').toggleClass('red');
  } else {
    $('header').removeClass();
    $('header').toggleClass('green');
  }
});
