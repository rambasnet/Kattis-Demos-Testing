// https://open.kattis.com/problems/helpaphd

#include <stdio.h>
#include <string.h>
#include <assert.h>

#define MAXLEN 20

int answer(char *line) {
    if (line[0] == 'P')
        return -1;
    char delim[] = "+";
    char cnum[5];
    int num1, num2;
    char *token = strtok(line, delim); // tokenize the first number
    sprintf(cnum, token); //store string to cnum
    sscanf(cnum, "%d", &num1);
    token = strtok(NULL, delim);
    sscanf(token, "%d", &num2);
    //printf("%d + %d = ", num1, num2, num1+num2);
    return num1 + num2;
}

void test() {
    char input[] = "P=NP";
    assert(answer(input) == -1);
    char input1[] = "1+999";
    assert(answer(input1) == 1000);
    char input2[] = "1000+0";
    assert(answer(input2) == 1000);
    char input3[] = "1000+1000";
    assert(answer(input3) == 2000);
    printf("all test cases passed...\n");
}

void solve() {
    int N, ans;
    char line[MAXLEN];
    char ch;
    scanf("%d", &N); // leaves \n behind... 
    scanf("%c", &ch); // read and discard \n
    for(int i=0; i<N; i++) {
        // read the line into line upto MAXLEN-1 or \n or eof
        // whicever comes first
        // protects from buffer overflow
        // reads and discards \n
        fgets(line, MAXLEN, stdin);
        //printf("line = %s\n", line);
        ans = answer(line);
        if (ans == -1)
            printf("skipped\n");
        else
            printf("%d\n", ans);
    }
}

int main(int argc, char* argv[]) {
    if (argc == 2 && strncmp(argv[1], "test", 4) == 0)
        test();
    else
        solve();
    
    return 0;
}