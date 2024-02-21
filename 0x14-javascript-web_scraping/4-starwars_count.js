#!/usr/bin/node

const request = require('request');

const apiUrl = `https://swapi-api.alx-tools.com/api/films`;

request(apiUrl, function(error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const idToSearch = 18;
    const filmsWithId = films.filter(film => film.episode_id === idToSearch);
    console.log(filmsWithId.length);
  } else {
    console.error('Failed to fetch film details:', response && response.statusCode);
  }
});
