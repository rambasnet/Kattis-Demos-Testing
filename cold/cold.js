/*
    Kattis cold-puter problem
*/

const readline = require("readline")
const assert = require("assert").strict

function solve() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    })

    var lineNum = 1
    rl.on("line", line => {
        //console.log(line);
        if (lineNum == 1) lineNum++
        else {
            var nums = line.split(" ")
            //console.log(nums)
            var count = answer(nums)
            console.log(count)
        }
    })
}

function answer(nums) {
    var count = 0
    for (var i in nums) {
        if (parseInt(nums[i]) < 0) ++count
    }
    return count
}

function test() {
    assert.strictEqual(answer([12, 56, -5565, -45454, 12, -45454]), 3)
    assert.strictEqual(answer([34, 345, 3434, 6, 0, 0, 3434, 34, 45454]), 0)
    assert.strictEqual(answer([-1000000, 1000000, -99999, 99999]), 2)
    console.log("all test cases passed...")
}

if (require.main == module) {
    if (process.argv.length > 2 && process.argv[2] === "test") test()
    else solve()
}
