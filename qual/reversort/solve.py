#!/usr/bin/env python3
import sys

def solve():
  N = int(input())
  M = list(map(int,input().split(' ')))
  c = 0
  for i in range(N):
    m = i
    for j in range(i, N):
      if M[j] < M[m]:
        m = j
    c += m - i + 1
    C = M[i:m+1]
    M = M[:i] + C[::-1] + M[m+1:]
  print(c - 1)

T = int(input())
for i in range(T):
  t = i + 1
  print("Case #%s: " %t, end='')
  solve()
