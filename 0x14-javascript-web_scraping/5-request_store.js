#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
const fileSys = require('fs');

request(args[0], (error, response, body) => {
  if (error) console.error('error:', error);

  if (response.statusCode === 200) {
    fileSys.writeFile(args[1], body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
