#!/usr/bin/node
let num;

function Factorial (num) {
  if (num === 0) {
    return 1;
  } else {
    return num * Factorial(num - 1);
  }
}

if (parseInt(process.argv[2])) {
  num = parseInt(process.argv[2])
  console.log(Factorial(num));
} else {
  console.log(1);
}
