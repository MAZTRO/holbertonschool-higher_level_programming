$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: function (myJson) {
    $('#hello').append(myJson.hello);
  }
});
