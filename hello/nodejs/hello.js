// Kattis hello problem
// force secure JS
"use strict"; //  https://www.w3schools.com/js/js_strict.asp
const assert = require('assert').strict;

function answer() {
    return 'Hello World!';
}

function solve() {
    console.log(answer());
}

if (require.main == module) {
    //console.log(process.argv);
    solve();
}

module.exports = {
    answer: answer
};