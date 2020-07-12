/*
By: Name

Date: 
Kattis hello world program.
*/

#include <iostream>
#include <cstring>
#include <cassert>

using namespace std;

void test();
string answer();
void solve();

int main(int argc, char* argv[]) {
    //cout << argc << argv[1] << endl;
    if (argc > 1 && string(argv[1]) == "test")
        test();
    else
        solve();
    return 0;
}

string answer() {
    return "Hello World";
}

void test() {
    assert(answer() == "Hello World");
    cerr << "All test cases passed...\n";
}

void solve() {
    cout << answer() << endl;
}