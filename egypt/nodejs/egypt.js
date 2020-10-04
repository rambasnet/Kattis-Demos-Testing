// egypt - kattis problem

"use strict";

const readline = require('readline');
const assert = require('assert').strict;

function answer(sides) {
  // numeric sort
  sides.sort( (a, b) => a-b);
  //console.log(sides);
  if (sides[0]**2 + sides[1]**2 === sides[2]**2) return 'right';
  else return 'wrong';
}

function test() {
  assert.strictEqual(answer([1, 2, 3]), 'wrong', 'assertion failed for wrong');
  assert.strictEqual(answer([12, 5, 13]), 'right');
  console.log('all test cases passed!');
}

function solve() {
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

if (require.main == module) {
  if (process.argv.length > 2 && process.argv[2] === 'test') test();
  else solve();
}