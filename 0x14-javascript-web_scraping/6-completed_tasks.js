#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response && response.statusCode === 200) {
    const todos = JSON.parse(body);

    const completedCountByUser = {};

    todos.forEach(todo => {
      const userId = todo.userId;
      const completed = todo.completed;

      if (completed) {
        if (!completedCountByUser[userId]) {
          completedCountByUser[userId] = 0;
        }
        completedCountByUser[userId]++;
      }
    });

    console.log(completedCountByUser);
  } else {
    console.error('Failed to fetch todos:', response && response.statusCode);
  }
});
