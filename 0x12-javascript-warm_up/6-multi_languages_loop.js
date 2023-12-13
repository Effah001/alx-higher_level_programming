#!/usr/bin/node

let languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (let i = 0; i < languages.length; i++) {
    let output = '';
    for (let j = 0; j < languages[i].length; j++) {
        output += languages[i][j] + '\n';
    }
    console.log(output);
}
