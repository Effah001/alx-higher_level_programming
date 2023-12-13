#!/usr/bin/node

let i = 0;
exports.logMe = function (item) {
    console.log(`${i}: ${arguments[i]}`);
     i++;
};
