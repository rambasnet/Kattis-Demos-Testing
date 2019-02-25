// Kattis egypt problem

#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <cassert>
#include <cstdio>
#include <vector>
#include <functional>
#include <sstream>

using namespace std;
using vi = vector<int>;

// c-array solution
string answer(int *sides) {
    sort(sides, sides+3);
    if (pow(sides[0], 2) + pow(sides[1], 2) == pow(sides[2], 2))
        return "right";
    else
        return "wrong";
}

// vector solution
string answer1(vi sides) {
    sort(sides.begin(), sides.end(), less<int>());
    if (pow(sides[0], 2) + pow(sides[1], 2) == pow(sides[2], 2))
        return "right";
    else
        return "wrong";
}

void test() {
    int input1[] = {6, 8, 10};
    assert(answer(input1) == "right");
    int input2[] = {3, 4, 5};
    assert(answer(input2) ==  "right");
    int input3[] = {5, 12, 13};
    assert(answer(input3) == "right");
    int input4[] = {1, 2, 3};
    assert(answer(input4) == "wrong");
    int input5[] = {2000, 100, 30000};
    assert(answer(input5) == "wrong");
    vi input11 = {10, 8, 6};
    assert(answer1(input11) == "right");
    vi input22 = {4, 3, 5};
    assert(answer1(input22) ==  "right");
    vi input33 = {13, 12, 5};
    assert(answer1(input33) == "right");
    vi input44 = {1, 2, 3};
    assert(answer1(input44) == "wrong");
    vi input55 = {100, 2000, 30000};
    assert(answer1(input55) == "wrong");
    cout << "All test cases passed...\n";
}

void solve() {
    int sides[3];
    stringstream ans;
    while (cin >> sides[0] >> sides[1] >> sides[2] && sides[0] != 0 && sides[1] != 0) {
        //printf("%s\n", answer(sides).c_str());
        ans << answer(sides) << '\n';
    }
    cout << ans.str();
}

void solve1() {
    vi sides;
    // vi sides(3);
    int a, b, c;
    stringstream ans;
    while (cin >> a >> b >> c && a != 0 && b != 0) {
        sides.push_back(a);
        sides.push_back(b);
        sides.push_back(c);
        //printf("%s\n", answer1(sides).c_str());
        ans << answer1(sides) << '\n';
        sides.clear();
    }
    cout << ans.str();
}

int main(int argc, char* argv[]) {
    ios::sync_with_stdio(false);
    if (argc > 1 && strncmp(argv[1], "test", 4) == 0)
        // run local tests
        test();
    else {
        // solve kattis test cases
        solve();
        //solve1();
    }
}