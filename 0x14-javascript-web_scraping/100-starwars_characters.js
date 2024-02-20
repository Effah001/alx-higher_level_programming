#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response && response.statusCode === 200) {
    const film = JSON.parse(body);
    const characters = film.characters;

    // Fetch details of each character
    characters.forEach(characterUrl => {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.error('Error:', error);
          return;
        }

        if (response && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        } else {
          console.error('Failed to fetch character details:', response && response.statusCode);
        }
      });
    });
  } else {
    console.error('Failed to fetch film details:', response && response.statusCode);
  }
});

