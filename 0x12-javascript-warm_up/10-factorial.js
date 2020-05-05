#!/usr/bin/node
let num = parseInt(process.argv[2]);

/* Recursion function */
function Factorial (num) {
  if (num === 0) {
    return 1;
  } else {
    return num * Factorial(num - 1);
  }
}
if (process.argv[2] % 1 === 0 || process.argv[2] === undefined) {
  num = 1;
  if (num === 1 || num < 0) {
    console.log(1);
  } else {
  console.log(Factorial(num));
  }
}
