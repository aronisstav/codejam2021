#!/usr/bin/env python3
import sys

def solve():
  N, C = input().split(' ')
  N = int(N)
  C = int(C) - N + 1
  F = [0] * (N + 1)
  for i in range(N-1, 0, -1):
    if C >= i:
      C -= i
      F[i+1] = 1
  if C != 0:
    print(f"IMPOSSIBLE")
    return
  L = list(range(1, N + 1))
  for i in range(2, N + 1):
    if F[i] == 1:
      Q = L[N-i:]
      L = L[:N-i] + Q[::-1]
  print(' '.join(map(str,L)))

T = int(input())
for i in range(T):
  t = i + 1
  print("Case #%s: " %t, end='')
  solve()
