/*
    Kattis cold-puter problem
*/
// force secure JS
"use strict"; //  https://www.w3schools.com/js/js_strict.asp


// this solution takes line of numbers as string and splits line into an array
function answer(line) {
  let nums = line.split(" ");
  let count = 0;
  for (var i in nums) {
    if (parseInt(nums[i]) < 0) ++count;
  }
  return count;
}

// this solution takes line as a string and counts - to find the number of negative numbers
function answer1(line) {
  let count = 0;
  for (let ch of line) {
    if (ch === '-') count++;
  }
  return count;
}

// solve with asynchronous line by line read
function solve() {
  const readline = require("readline");
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  let lineNum = 1;
  rl.on("line", line => {
    //console.log(line);
    if (lineNum === 1) lineNum++;
    else {
      //console.log(answer(line));
      console.log(answer1(line));
    }
  });
}

// solve reading the whole data synchronously and parsing it in memory line by line
function solve1() {
  const fs = require('fs');
  const data = fs.readFileSync(process.stdin.fd, 'utf-8'); // or replace process.stdin.fd with 0
  // there's an empty character element at the end
  const lines = data.split('\n');
  //console.log(lines);
  for (let i in lines) {
    if (i == 1) {
      //console.log('line', lines[i]);
      console.log(answer(lines[i]));
    }
  }
}

if (require.main == module) {
  //solve();
  solve1();
}

module.exports = {
  answer: answer,
  answer1: answer1
}