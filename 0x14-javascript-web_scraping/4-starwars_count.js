#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function(error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response && response.statusCode === 200) {
    const sub = '/people/13/';
    const str = JSON.stringify(body);
    const count = str.split(sub).length - 1;
    console.log(count);  }
});
