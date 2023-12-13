#!/usr/bin/node

const x = process.argv[2];

if (!isNaN(x) && x > 0) {
  let repeats = 'C is fun'.repeat(x);
  console.log(repeats);
} else {
  console.log('Missing number of occurrences');
}
