#!/usr/bin/node
let idx = 0;
if (process.argv[2]) {
  while (idx < parseInt(process.argv[2])) {
    console.log('C is fun');
    idx++;
  }
} else {
  console.log('Missing number of occurrences');
}
