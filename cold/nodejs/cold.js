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

function test() {
    assert.strictEqual(answer([12, 56, -5565, -45454, 12, -45454]), 3);
    assert.strictEqual(answer([34, 345, 3434, 6, 0, 0, 3434, 34, 45454]), 0);
    assert.strictEqual(answer([-1000000, 1000000, -99999, 99999]), 2);
    console.log("all test cases passed...");
}

if (require.main == module) {
    if (process.argv.length > 2 && process.argv[2] === "test") test();
    else solve();
}
