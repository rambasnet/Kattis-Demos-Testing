const helpaphd = require('./helpaphd');

/*
function test() {
  assert.strictEqual(answer("P=NP"), 'skipped', 'assertion error for P=NP');
  assert.strictEqual(answer('2+10'), 12);
  assert.strictEqual(answer('0+1000'), 1000);
  console.log('all test cases passed...');
}
*/

test('Must skip this', () => {
    expect(helpaphd.answer("P=NP")).toBe('skipped');
});

test('2+10=12', () => {
    expect(helpaphd.answer("2+10")).toBe(12);
});

test('0+1000=1000', () => {
    expect(helpaphd.answer("0+1000")).toBe(1000);
});