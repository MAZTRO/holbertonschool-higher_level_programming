#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/:2', (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  console.log(response.statusCode);

  if (response.statusCode === 200) {
    console.log(JSON.stringify(body));
  }
});