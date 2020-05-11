#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let character = 'C';

    if (c === undefined) {
      character = 'X';
    }
    let x = 0;
    while (x < this.height) {
      console.log(`${character}`.repeat(this.width));
      x++;
    }
  }
};
