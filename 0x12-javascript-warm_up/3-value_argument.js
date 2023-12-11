#!/usr/bin/node

const Args = process.argv.slice(2);
if (Args[0] !== undefined) {
  console.log(Args[0]);
} else {
  console.log('No argument');
}
