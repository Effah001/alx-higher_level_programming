#!/usr/bin/node

const arg = process.argv[2];

const integerValue = parseInt(arg, 10);

if (isNaN(integerValue)) {
  console.log('Not a number');
} else {
  console.log('My number:', integerValue);
}
