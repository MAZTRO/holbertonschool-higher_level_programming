#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');

request(args[0], (error, response, body) => {
  if (error) console.error('error:', error);

  if (response.statusCode === 200) {
    let countTrue = 0;
    let countFalse = 0;
    const TodoList = JSON.parse(body);
    const final = {};

    for (let idx = 0; idx < TodoList.length; idx++) {
      if (TodoList[idx].completed === true) {
        countTrue -= -1;
      } else {
        countFalse -= -1;
      }
      final[TodoList[idx].userId] = countTrue;
      if (countTrue + countFalse === 20) {
        countTrue = countFalse = 0;
      }
    }
    console.log(final);
  }
});
