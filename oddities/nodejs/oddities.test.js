const oddities = require('./oddities')

/*
function test() {
    assert.strictEqual(answer(1034349), "is odd");
    assert.strictEqual(answer(3435350), "is even");
    console.log("all test cases passed...");
}
*/

test('this is odd', () => {
    expect(oddities.answer(1034349)).toBe("is odd");
});

test('this is even', () => {
    expect(oddities.answer(3435350)).toBe("is even");
});