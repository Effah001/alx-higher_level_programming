#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rectangle = '';
    for (let i = 0; i < this.height; i++) {
      rectangle += 'X'.repeat(this.width);
      if (i < this.height - 1) {
        rectangle += '\n';
      }
    }
    console.log(rectangle);
  }
}

module.exports = Rectangle;
