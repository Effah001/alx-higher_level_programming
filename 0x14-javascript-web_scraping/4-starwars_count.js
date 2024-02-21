#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response && response.statusCode === 200) {
    const characterInfo = JSON.parse(body);
    const films = characterInfo.films;
    console.log(films.length);
  } else {
    console.error('Failed to fetch character details:', response && response.statusCode);
  }
});
