#!/usr/bin/node
exports.esrever = function (list) {
  const newArr = [];
  for (let idx = list.length - 1; idx >= 0; idx--) {
    newArr.push(list[idx]);
  }
  return newArr;
};
