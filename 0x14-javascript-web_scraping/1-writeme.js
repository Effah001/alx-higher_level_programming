#!/usr/bin/node

const fs = require('fs');

// Extract the file path and content from command-line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write to the file asynchronously
fs.writeFile(filePath, content, 'utf8', function (err) {
  if (err) {
    console.error('Error writing to file:', err);
  }
});
