#!/usr/bin/node
if (process.argv.length > 2) {
  console.log(parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
