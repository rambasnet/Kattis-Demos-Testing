const hello = require('./hello');

/*
function test() {
    var ans = answer();
    var expcted = 'Hello World!';
    assert.strictEqual(ans, expcted);
    console.log('all test cases passed...');
}
*/

test('must return Hello World!', () => {
    expect(hello.answer()).toBe('Hello World!');
});
