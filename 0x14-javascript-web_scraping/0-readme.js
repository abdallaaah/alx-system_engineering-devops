#!/usr/bin/node
// this is comment

// console.log(process.argv[2]);
const fs = require('node:fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
