#!/usr/bin/node 

const size = process.argv[2];

if (!isNaN(size) && size > 0) {
  let repeats = ' X'.repeat(size);
  for (let i = 0; i < size; i++) {
    console.log(repeats);
  }
} else {
  console.log('Missing size');
}

