#!/usr/bin/env python3

# Kattis - hello problem

import sys

def answer():
  a = "Hello World!"
  return a

def solve():
  print(answer())

def test():
  assert answer() == "Hello World!"
  print('all test cases passed...')

if __name__ == "__main__":
  solve()
