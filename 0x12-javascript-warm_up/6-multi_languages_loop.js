#!/usr/bin/node

let languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (let i = 0; i < languages.length; i++) {
    for (let j = 0; j < languages[i].length; j++) {
        console.log(languages[i][j]);
    }
    console.log('\n');
}
