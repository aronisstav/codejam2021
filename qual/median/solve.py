#!/usr/bin/env python3
import sys
import functools

def ask(a, b, c):
  eprint(f"  Ask {a} {b} {c}", end='')
  print(a, b, c)
  r = int(input())
  eprint(f" -> {r}")
  if r == -1:
    exit()
  return r

def compare(a, b, l1, l2):
  if a == l1:
    return -1
  elif b == l1:
    return 1
  elif a == l2:
    return 1
  elif b == l2:
    return -1
  else:
    r = ask(a, b, l1)
    if r == a:
      return -1
    else:
      return 1

def guess(L):
  eprint(f"Guess: {L}")
  print(' '.join(map(str, L)))
  r = int(input())
  if r == -1:
    exit()
  else:
    eprint("Got it!")

def solve(N):
  l1 = 1
  l2 = 2
  for i in range(3, N + 1):
    a = ask(l1, l2, i)
    if a == l1:
      l1 = i
    elif a == l2:
      l2 = i
  eprint(f"Limits: {l1} {l2}")
  L = list(range(1, N + 1))
  Q = sorted(L, key=functools.cmp_to_key(lambda a, b: compare(a, b, l1, l2)))
  guess(Q)

def eprint(*args, **kwargs):
  print(*args, file=sys.stderr, **kwargs)

T, N, Q = input().split(' ')
eprint(f"T={T} N={N} Q={Q}")
T = int(T)
N = int(N)
for _ in range(T):
  solve(N)
