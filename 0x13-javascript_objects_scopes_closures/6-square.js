#!/usr/bin/node
const BaseSquare = require('./5-square');
module.exports = class Square extends BaseSquare {
  charPrint (c) {
    if (c == undefined) {
      c = 'X';
    }
    let x = 0;
    while (x < this.height) {
      console.log(c.repeat(this.width));
      x++;
    }
  }
};
