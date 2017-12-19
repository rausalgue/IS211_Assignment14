#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week 14 - Recursion"""

def fibonnaci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)