$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function (myJson) {
    for (let idx = 0; idx < Object.keys(myJson.results).length; idx++) {
      $('#list_movies').append(`<li>${myJson.results[idx].title}</li>`);
    }
  }
});
