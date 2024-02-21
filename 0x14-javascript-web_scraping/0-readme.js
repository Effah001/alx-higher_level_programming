#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function(err, data) {
  // Check for errors
  if (err) {
    console.error(err);
    return;
  }

  console.log(data);
});
