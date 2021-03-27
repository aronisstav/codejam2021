#!/usr/bin/env python3
import sys

def solve():
  X, Y, M = input().split(" ")
  X = int(X)
  Y = int(Y)
  C = 0
  P = M[0]
  for i in range(1, len(M)):
    if M[i] == "?":
      []
    elif M[i] == P:
      []
    else:
        if P == "?":
          []
        elif P == "C":
          C+=X
        else:
          C+=Y
        P = M[i]
  print(C)

T = int(input())
for i in range(T):
  t = i + 1
  print("Case #%s: " %t, end='')
  solve()
