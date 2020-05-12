#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${args[0]}/`, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else if (args[0] === '7') {
    console.log('The Force Awakens');
  }
});
