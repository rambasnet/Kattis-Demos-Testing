// helpaphd kattis problem

"use strict";

const assert = require('assert').strict;
const readline = require('readline')

function answer(line) {
  if (line[0] == 'P') return 'skipped';
  let values = line.split('+');
  return parseInt(values[0])+parseInt(values[1]);
}

function test() {
  assert.strictEqual(answer("P=NP"), 'skipped', 'assertion error for P=NP');
  assert.strictEqual(answer('2+10'), 12);
  assert.strictEqual(answer('0+1000'), 1000);
  console.log('all test cases passed...');
}

function solve() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  let lineNum = 0;
  let ans = []
  let totalLines = 0;
  rl.on('line', (line) => {
    if (lineNum == 0) {
      lineNum++;
      totalLines = parseInt(line);
    }
    //else console.log(answer(line));
    else {
      lineNum++; 
      ans.push(answer(line));
    }
    //console.log(lineNum);
    // print result once when all the results are collected
    if (lineNum == totalLines+1)
      console.log(ans.join("\n"));
  });
}

function solve1() {
  const fs = require('fs')
  const data = fs.readFileSync(process.stdin.fd, 'utf-8')
  //console.log(data.toString());
  let ans = [];
  let lines = data.split('\n')
  //console.log(lines)
  let N = parseInt(lines[0]);
  for (let index in lines) {
    if (index == 0) continue;
    else if (index > N) break;
    else ans.push(answer(lines[index]));
  }
  console.log(ans.join("\n"));
}

if (require.main == module) {
  if (process.argv.length > 2 && process.argv[2] == 'test') test();
  else solve1();
}

module.exports = {
  answer: answer
};