#! /usr/bin/env python3

# https://open.kattis.com/problems/jointjogjam

#import sys
import math

def distance(x1:int, y1:int, x2:int, y2:int) -> float:
  return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def answer(startDist:float, endDist:float) -> float:
  return max(startDist, endDist)

def solve() -> None:
  """
  data = input()
  cleanData = []
  for n in data.split():
    cleanData.append((int(n)))
  """
  # or use list comprehension syntax
  cleanData = [int(x) for x in input().split()]
  startDist = distance(cleanData[0], cleanData[1], cleanData[2], cleanData[3])
  endDist = distance(cleanData[4], cleanData[5], cleanData[6], cleanData[7])
  print(answer(startDist, endDist))

if __name__ == "__main__":
  solve()

