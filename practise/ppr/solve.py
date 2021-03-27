#!/usr/bin/env python3
import sys

def solve():
  N = int(input())
  A = []
  for i in range(N):
    arr = input()
    A.append((list(map(int,arr.split(' '))),i))
  A = sorted(A)
  C = 0
  J = 0
  O = []
  for i in range(len(A)):
    if C <= A[i][0][0]:
      O.append([A[i][1],"C"])
      C=A[i][0][1]
    elif J <= A[i][0][0]:
      O.append([A[i][1],"J"])
      J=A[i][0][1]
    else:
      print("IMPOSSIBLE")
      return
  O = sorted(O)
  print("".join(map(lambda x: x[1],O)))

T = int(input())
for i in range(T):
  t = i + 1
  print("Case #%s: " %t, end='')
  solve()
