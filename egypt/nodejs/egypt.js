// egypt - kattis problem

"use strict";

// solution passing array of numbers
function answer(sides) {
  // numeric sort in ascending order
  sides.sort( (a, b) => a-b);
  //console.log(sides);
  if (sides[0]**2 + sides[1]**2 === sides[2]**2) return 'right';
  else return 'wrong';
}

// async read line by line
function solve() {
  const readline = require('readline');
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  rl.on('line', (line) => {
    //console.log(line);
    if (line != '0 0 0') {
      let nums = line.split(' ').map(Number);
      console.log(answer(nums));
    }
  });
}

// sync read whole data
function solve1() {
  const fs = require('fs');
  const data = fs.readFileSync(process.stdin.fd, 'utf-8');
  //console.log(data);
  let lines = data.split('\n');
  //console.log(lines);
  let ans = [];
  for (let line of lines) {
    if (line === '0 0 0') {
      break;
    }
    let sides = line.split(' ').map(Number);
    ans.push(answer(sides))
  }
  console.log(ans.join('\n'));
}

if (require.main === module) {
  //solve();
  solve1();
}

module.exports = {
  answer: answer
};