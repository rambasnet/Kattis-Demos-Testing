// https://open.kattis.com/problems/jointjogjam

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

#define MAX_ERROR 1e-6

double distance(double x1, double y1, double x2, double y2) {
  return sqrt((pow(x1-x2, 2) + pow(y1-y2, 2)));
}

double answer(double startDist, double endDist ) {  
  return max(startDist, endDist);
}

void test_distance() {
  double ans = 1.41421356237;
  assert(abs(distance(0, 0, 1, 1) - ans) <= MAX_ERROR);
  ans = 2.82842712475;
  assert(distance(0, 0, 2, 2) - ans <= MAX_ERROR);
  ans = 48.6004115209;
  assert(distance(1, 30, 6, 45) - ans <= MAX_ERROR);
  printf("Congrtulations! All test cases passed distance()\n");
}

void test_answer() {
  double startDist, endDist, actual;
  startDist = distance(0, 0, 1, 1);
  endDist = distance(1, 1, 2, 2);
  actual = 1.4142135624;
  assert(answer(startDist, endDist) - actual <= MAX_ERROR);
  startDist = distance(0, 0, 0, 1);
  actual = 2.2360679775;
  endDist = distance(0, 2, 2, 1);
  assert(answer(startDist, endDist) - actual <= MAX_ERROR);
  startDist = distance(5, 0, 10, 0);
  endDist = distance(5, 0, 10, 0);
  actual = 5;
  assert(answer(startDist, endDist) - actual <= MAX_ERROR);
  printf("Congratulations! All test cases passed for answer()\n");
}

void solve() {
    int Kari_x1, Kari_y1, Ola_x1, Ola_y1, Kari_x2, Kari_y2, Ola_x2, Ola_y2;
    double start_dist, end_dist;
    cin >> Kari_x1 >> Kari_y1 >> Ola_x1 >> Ola_y1 >> Kari_x2 >> Kari_y2 >> Ola_x2 >> Ola_y2;
    start_dist = distance(Kari_x1, Kari_y1, Ola_x1, Ola_y1);
    end_dist = distance(Kari_x2, Kari_y2, Ola_x2, Ola_y2); 
    printf("%.10f\n", answer(start_dist, end_dist));
}

int main(int argc, char* argv[]) {
    ios::sync_with_stdio(false);
    if (argc > 1 && strncmp(argv[1], "test", 4) == 0) {
        // run local tests
        test_distance();
        test_answer();
    }
    else {
        // solve kattis test cases
        solve();
    }
}