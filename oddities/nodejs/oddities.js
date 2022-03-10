// oddities problem

// force secure JS
"use strict"; //  https://www.w3schools.com/js/js_strict.asp

function answer(num) {
    if (num % 2 == 0) return "is even";
    else return "is odd";
}

// async reading line by line
function solve() {
    const readline = require("readline");
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

//sync reading the whole data
function solve1() {
    const fs = require('fs');
    let data = fs.readFileSync(process.stdin.fd, 'utf-8');
    let lines = data.split('\n');
    //console.log(lines);
    let ans = [];
    for(let i in lines) { // i is string not a integer!
        i = parseInt(i);
        if (i === 0 || i+1 >= lines.length) continue;
        ans.push(`${lines[i]} ${answer(parseInt(lines[i]))}`);
    }
    console.log(ans.join('\n'));
}

// check if module is ran as the main module
if (require.main == module) {
    //solve();
    solve1();
}

module.exports = {
    answer: answer
};
