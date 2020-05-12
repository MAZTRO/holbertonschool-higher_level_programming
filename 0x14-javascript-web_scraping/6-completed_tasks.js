#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');

request(args[0], (error, response, body) => {
  if (error) console.error('error:', error);

  if (response.statusCode === 200) {
    let count = 0;
    let len = 0;
    const TodoList = JSON.parse(body);
    const final = {};

    for (let idx = 0; idx < TodoList.length; idx++) {
      len = Object.keys(final).length;
      if (TodoList[idx].completed === true) {
        count -= -1;
      }
      final[TodoList[idx].userId] = count;
      if (len + 1 !== Object.keys(final).length + 1) {
        count = 0;
      }
    }
    console.log(final);
  }
});
