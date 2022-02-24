// oddities problem

// force secure JS
"use strict"; //  https://www.w3schools.com/js/js_strict.asp

const readline = require("readline")
const assert = require("assert").strict

function answer(num) {
    if (num % 2 == 0) return "is even";
    else return "is odd";
}

function solve() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    var lineNum = 1;
    rl.on("line", line => {
        if (lineNum == 1) lineNum++;
        else {
            console.log(line, answer(parseInt(line)));
        }
    })
}

// check if module is ran as the main module
if (require.main == module) {
    solve();
}

module.exports = {
    answer: answer
};
