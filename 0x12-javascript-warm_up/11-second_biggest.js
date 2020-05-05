#!/usr/bin/node
const myArray = process.argv;
myArray.splice(0, 2);
if (myArray.length === 0 || myArray.length === 1) {
  console.log(0);
} else {
  myArray.sort(function (a, b) { return b - a; });
}
console.log(parseInt(myArray[1]));
