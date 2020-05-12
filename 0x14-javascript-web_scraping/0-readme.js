#!/usr/bin/node
const args = process.argv.slice(2);
const fileSys = require('fs');

fileSys.readFile(args[0], 'utf-8', (error, file) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(file);
});
