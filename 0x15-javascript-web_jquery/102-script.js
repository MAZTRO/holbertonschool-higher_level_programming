document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').on('click', function () {
    const code = $('#language_code').val();
    console.log(code);
    $.ajax({
      type: 'GET',
      url: `https://fourtonfish.com/hellosalut/?cc=${code}`,
      success: function (myJson) {
        console.log(myJson);
        $('div p').remove();
        $('#hello').append(`<p>${myJson.hello}</p>`);
      }
    });
  });
});
