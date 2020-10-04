/*
By:
Date:
Kattis - Cold-puter Science problem
https://open.kattis.com/problems/cold
*/

#include "stdio.h"
#include "string.h"
#include "assert.h"

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
    printf("%s\n", "all test cases passed...");
}

void solve() {
    int n, t, cold=0;
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        scanf("%d", &t);
        cold += answer(t);
    }
    printf("%d\n", cold);
}