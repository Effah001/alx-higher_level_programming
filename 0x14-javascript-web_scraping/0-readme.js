#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function(err, data) {
  // Print the file contents
  console.log(data);
});

