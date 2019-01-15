// https://open.kattis.com/problems/helpaphd
// demonstrates how to parse string into ints and other tokens

#include <iostream>
#include <string>
#include <sstream>
#include <cassert>
#include <cstring>

using namespace std;

int answer(string equation) {
    int a, b;
    char op;
    // if first character is 'P' return -1 
    if (equation[0] == 'P')
        return -1;
    stringstream ss(equation); // convert string into stringstream
    // break equation into multiple tokens
    ss >> a >> op >> b;
    return a+b;
}

void test() {
    assert(answer("P=NP") == -1);
    assert(answer("999+1") == 1000);
    assert(answer("1000+0") == 1000);
    cout << "all test cases passed..." << endl;
}

void kattis() {
    int N, ans;
    string equation;
    cin >> N;
    while(N--) {
        cin >> equation;
        ans = answer(equation);
        if (ans == -1)
            cout << "skipped" << endl;
        else
            cout << ans << endl;
    }
}

int main(int argc, char* argv[]) {
    if (argc > 1 && strncmp(argv[1], "test", 4) == 0)
        test();
    else
        kattis();
    return 0;
}