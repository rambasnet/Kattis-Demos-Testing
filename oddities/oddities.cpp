/*
kattis - oddities
*/

#include <iostream>
#include <string>
#include <cstring>
#include <cassert>

using namespace std;

string answer(int num) {
    if (num%2 == 0)
        return "is even";
    else
        return "is odd";
}

void test() {
    int x = -10;
    assert(answer(x) == "is even");
    assert(answer(9) == "is odd");
    assert(answer(0) == "is even");
    cerr << "all test cases passed..." << endl;
}

void kattis() {
    int n, x;
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> x;
        cout << x << " " << answer(x) << endl;
    }
}

int main(int argc, char* argv[]) {
    if (argc > 1 && string(argv[1]) == "test")
        test();
    else
        kattis();
    return 0;
}