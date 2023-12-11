#!/usr/bin/node

const Args = process.argv[2];
if (Args !== undefined) {
  console.log(Args);
} else {
  console.log('No argument');
}
