#!/usr/bin/node
const myVar = process.argv;

if (parseInt(myVar[2])) {
  console.log(`My number: ${parseInt(myVar[2])}`);
} else {
  console.log('Not a number');
}
