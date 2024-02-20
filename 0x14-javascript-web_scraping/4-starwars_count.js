#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function(error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const id = 18;
    const filmsWithId = films.filter(film => film.episode_id === id);
    console.log(filmsWithId.length);
  } else {
    console.error('Failed to fetch film details:', response && response.statusCode);
  }
});

