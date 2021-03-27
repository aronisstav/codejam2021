#!/usr/bin/env python3
import sys

def solve():
  arr = input()
  b=0
  for i in range(len(arr)):
    c = int(arr[i])
    if c == b:
      print(c, end='')
    elif c > b:
      for _ in range(c - b):
        print("(", end='')
      print(c, end='')
    else:
      for _ in range(b - c):
        print(")", end='')
      print(c, end='')
    b = c
  for _ in range(b):
    print(")", end='')
  print()

T = int(input())
for i in range(T):
  t = i + 1
  print("Case #%s: " %t, end='')
  solve()
