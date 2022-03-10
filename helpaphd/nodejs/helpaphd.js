// helpaphd kattis problem

"use strict";

function answer(line) {
  if (line[0] == 'P') return 'skipped';
  let values = line.split('+');
  return parseInt(values[0])+parseInt(values[1]);
}

// read data asynchronously
function solve() {
  const readline = require('readline')
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  let lineNum = 0;
  let ans = [];
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

// read data synchronously
function solve1() {
  const fs = require('fs')
  const data = fs.readFileSync(process.stdin.fd, 'utf-8')
  //console.log(data);
  let ans = [];
  let lines = data.split('\n')
  //console.log(lines)
  let N = parseInt(lines[0]);
  for (let index in lines) { // index is of type string
    //console.log(typeof index)
    index = parseInt(index)
    //console.log(index, lines[index])
    if (index === 0) continue;
    else if (index > N) break;
    else ans.push(answer(lines[index]));
  }
  console.log(ans.join("\n"));
}

if (require.main == module) {
  //solve();
  solve1();
}

module.exports = {
  answer: answer
};