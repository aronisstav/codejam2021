#!/usr/bin/env python3
import sys

def solve():
  N = int(input())
  M = []
  for i in range(N):
    arr = input()
    M.append(list(map(int,arr.split(' '))))
  t = 0
  for i in range(N):
    t += M[i][i]
  c = 0
  for i in range(N):
    s = set()
    a = 0
    for j in range(N):
      if M[i][j] in s:
        a = 1
      s.add(M[i][j])
    c += a
  r = 0
  for j in range(N):
    s = set()
    a = 0
    for i in range(N):
      if M[i][j] in s:
        a = 1
      s.add(M[i][j])
    r += a
  print(t, c, r)

T = int(input())
for i in range(T):
  t = i + 1
  print("Case #%s: " %t, end='')
  solve()
