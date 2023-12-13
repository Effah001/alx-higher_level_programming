#!/usr/bin/node

let languages = ['C is fun', 'Python is cool', 'Javascript is Amazing'];

for (let i = 0; i < languages.length; i++) {
    for (let j = 0; j < languages[i].length; j++) {
        console.log(languages[i][j]);
    }
    console.log('\n');
}
