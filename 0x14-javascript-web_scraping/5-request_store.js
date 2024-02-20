#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response && response.statusCode === 200) {
    // Write the contents of the web page to a file
    fs.writeFile(process.argv[3], body, 'utf8', function (err) {
      if (err) {
        console.error('Error writing to file:', err);
      }
    });
  }
});
