#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');

request(args[0], (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  if (response.statusCode === 200) {
    let count = 0;
    const movieList = JSON.parse(body).results;

    for (let idx = 0; idx < movieList.length; idx++) {
      const characters = movieList[idx].characters;
      if (characters.indexOf('https://swapi-api.hbtn.io/api/people/18/') !== -1) {
        count -= -1;
      }
    }
    console.log(count);
  }
});
