const readline = require("readline")
const assert = require("assert").strict

function answer(num) {
    if (num % 2 == 0) return "is even"
    else return "is odd"
}

function test() {
    assert.strictEqual(answer(1034349), "is odd")
    assert.strictEqual(answer(3435350), "is even")
    console.log("all test cases passed...")
}

function solve() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    })
    var lineNum = 1
    rl.on("line", line => {
        if (lineNum == 1) lineNum++
        else {
            console.log(line, answer(parseInt(line)))
        }
    })
}

if (require.main == module) {
    if (process.argv.length > 2 && process.argv[2] === "test") test()
    else solve()
}
