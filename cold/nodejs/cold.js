/*
    Kattis cold-puter problem
*/
// force secure JS
"use strict"; //  https://www.w3schools.com/js/js_strict.asp

const readline = require("readline");
const assert = require("assert").strict;

function solve() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    let lineNum = 1;
    rl.on("line", line => {
        //console.log(line);
        if (lineNum == 1) lineNum++;
        else {
            //console.log(answer(line));
            console.log(answer1(line));
        }
    });
}

function answer(line) {
    let nums = line.split(" ");
    let count = 0;
    for (var i in nums) {
        if (parseInt(nums[i]) < 0) ++count;
    }
    return count;
}

function answer1(line) {
    let count = 0;
    for (let ch of line) {
        if (ch == '-') count++;
    }
    return count;
}

if (require.main == module) {
    solve();
}

module.exports = {
    answer: answer,
    answer1: answer1
}