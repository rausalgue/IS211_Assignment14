#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week 14 - Recursion"""

def fibonnaci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, (a % b))

def compareTo(s1,s2):
    if s1<s2:
        return -1
    if s1==s2:
        return 0
    if s1>s2:
        return 1
    return compareTo(s1,s2)