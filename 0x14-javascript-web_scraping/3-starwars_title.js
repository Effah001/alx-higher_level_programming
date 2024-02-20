#!/usr/bin/node

const request = require('request');

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(apiUrl, function(error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  
  if (response && response.statusCode === 200) {
    const film = JSON.parse(body);
    console.log(film.title);
  } else {
    console.error('Failed to fetch film details:', response && response.statusCode);
  }
});

