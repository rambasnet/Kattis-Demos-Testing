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
    cerr << "all test cases passed..." << endl;
}

void kattis() {
    int N, ans;
    string equation;
    cin >> N;
    stringstream result;
    while(N--) {
        cin >> equation;
        ans = answer(equation);
        if (ans == -1)
            //cout << "skipped" << endl;
            result << "skipped\n";
        else
            //cout << ans << endl;
            result << ans << '\n';
    }
    cout << result.str();
}

int main(int argc, char* argv[]) {
    ios::sync_with_stdio(false);
    if (argc > 1 && string(argv[1]) == "test")
        test();
    else
        kattis();
    return 0;
}