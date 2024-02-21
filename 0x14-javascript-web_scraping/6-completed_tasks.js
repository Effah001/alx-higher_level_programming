#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function(error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response && response.statusCode === 200) {
    const todos = JSON.parse(body);

    // Initialize an object to store the count of completed todos per user
    const completedCountByUser = {};

    // Iterate through each todo item
    todos.forEach(todo => {
      const userId = todo.userId;
      const completed = todo.completed;

      // Increment the count of completed todos for the user
      if (completed) {
        if (!completedCountByUser[userId]) {
          completedCountByUser[userId] = 0;
        }
        completedCountByUser[userId]++;
      }
    });

    // Print the count of completed todos per user
    console.log('Completed todos count by user:');
    for (const userId in completedCountByUser) {
      console.log(`User ${userId}: ${completedCountByUser[userId]}`);
    }
  } else {
    console.error('Failed to fetch todos:', response && response.statusCode);
  }
});

