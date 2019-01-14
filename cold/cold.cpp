/*
By:
Date:
Kattis - Cold-puter Science problem
https://open.kattis.com/problems/cold
*/

#include <iostream>
#include <cstring>
#include <cassert>

using namespace std;

void test();
int answer(int);
void solve();

int main(int argc, char* argv[]) {
    if (argc > 1 && (strncmp(argv[1], "test", 4) == 0))
        test();
    else
        solve();
    return 0;
}

int answer(int temp) {
    return (temp < 0) ? 1:0;
}

void test() {
    int t = -100000;
    int expected = 1;
    int ans = answer(t);
    assert(ans == expected);
    assert(answer(1000000) == 0);
    assert(answer(0) == 0);
    cout << "all test cases passed..." << endl;
}

void solve() {
    int n, t, cold=0;
    cin >> n;

    for (int i=0; i<n; i++) {
        cin >> t;
        cold += answer(t);
    }
    cout << cold << endl;
}