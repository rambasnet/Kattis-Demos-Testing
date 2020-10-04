/*
Kattis hello world program solution in C
*/

#include <stdio.h>
#include <string.h>
#include <assert.h>


void test();
char* answer();
void solve();

int main(int argc, char* argv[]) {
    //cout << argc << argv[1] << endl;
    if (argc > 1 && strncmp(argv[1], "test", 4) == 0)
        test();
    else
        solve();
    return 0;
}

char* answer() {
    // can return address to static array from a function
    static char ans[] = "Hello World\0";
    return ans;
}

void test() {
    assert(strncmp(answer(), "Hello World", 11) == 0);
    printf("All test cases passed...\n");
}

void solve() {
    printf("%s\n", answer());
}