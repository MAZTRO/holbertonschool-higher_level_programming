#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');

request(args[0], (error, response, body) => {
  if (error) {
    console.error('error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const TodoList = JSON.parse(body);
    const final = {};

    for (let idx = 0; idx < TodoList.length; idx++) {
      if (TodoList[idx].completed === true) {
        if (final[TodoList[idx].userId]) {
          final[TodoList[idx].userId] = final[TodoList[idx].userId] + 1;
        } else {
          final[TodoList[idx].userId] = 1;
        }
      }
    }
    console.log(final);
  }
});
