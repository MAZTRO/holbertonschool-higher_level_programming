#!/usr/bin/node
if (process.argv[2] && process.argv[2] % 1 === 0) {
  console.log(parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
