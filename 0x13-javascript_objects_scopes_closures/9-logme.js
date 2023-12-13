#!/usr/bin/node

exports.logMe = function (item) {
  for (let i = 0; i < arguments.length; i++) {
    console.log(`${i}: ${arguments[i]}`);
  }
};
