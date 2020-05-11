#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  print () {
    let x = 0;
    while (x < this.height) {
      console.log('X'.repeat(this.width));
      x++;
    }
  }

  rotate () {
    this.width = this.height;
    this.height = this.width;
  }
};
