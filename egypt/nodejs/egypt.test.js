const egypt = require('./egypt')

/*
  assert.strictEqual(answer([1, 2, 3]), 'wrong', 'assertion failed for wrong');
  assert.strictEqual(answer([12, 5, 13]), 'right');
  console.log('all test cases passed!');
*/

test('not a right triangle', () => {
    expect(egypt.answer([1, 2, 3])).toBe('wrong');
});

test('a right triangle', () => {
    expect(egypt.answer([12, 5, 13])).toBe('right');
});
