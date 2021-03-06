#!/usr/bin/node
'use strict';
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let stri = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        stri += 'X';
      }
      if (i < (this.height - 1)) {
        stri += '\n';
      }
    }
    console.log(stri);
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
    return this;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
