// Kattis hello problem

const assert = require('assert').strict;

if (require.main == module) {
    //console.log(process.argv);
    if (process.argv.length > 2 && process.argv[2] === 'test')
        test();
    else
        solve();
}

function answer() {
    return 'Hello World!';
}

function test() {
    var ans = answer();
    var expcted = 'Hello World!';
    assert.strictEqual(ans, expcted);
    console.log('all test cases passed...');
}

function solve() {
    console.log(answer());
}
