#!/usr/bin/node
let idx = 0;
if (process.argv[2] && process.argv[2] % 1 === 0) {
  while (idx < parseInt(process.argv[2])) {
    console.log('X'.repeat(parseInt(process.argv[2])));
    idx++;
  }
} else {
  console.log('Missing size');
}
