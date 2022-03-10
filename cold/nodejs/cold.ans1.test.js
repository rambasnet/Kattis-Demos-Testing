const answers = require('./cold')

/*
    assert.strictEqual(answer1("12, 56, -5565, -45454, 12, -45454"), 3);
    assert.strictEqual(answer1("34, 345, 3434, 6, 0, 0, 3434, 34, 45454"), 0);
    assert.strictEqual(answer1("-1000000, 1000000, -99999, 99999"), 2);
*/

test('there are 3 negative temps', () => {
    expect(answers.answer1("12, 56, -5565, -45454, 12, -45454")).toBe(3);
});

test('there is 0 -ve temperatures', () => {
    expect(answers.answer1("34, 345, 3434, 6, 0, 0, 3434, 34, 45454")).toBe(0);
});

test('there are 2 -ve temperatures', () => {
    expect(answers.answer1("-1000000, 1000000, -99999, 99999")).toBe(2);
});
