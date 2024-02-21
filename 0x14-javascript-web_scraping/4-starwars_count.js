#!/usr/bin/node

const request = require('request');
const args = process.argv;

const apiUrl = args[2];

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const characterUrl = 'https://swapi-api.alx-tools.com/api/people/13/';
    const characterFilms = body.films.filter(filmUrl => filmUrl.includes(characterUrl));
    console.log('Number of Films:', characterFilms.length);
  } else {
    console.error('Failed to fetch character details:', response && response.statusCode);
  }
});
