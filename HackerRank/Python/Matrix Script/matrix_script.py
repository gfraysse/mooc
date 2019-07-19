#!/bin/python

import math
import os
import random
import re
import sys

first_multiple_input = raw_input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in xrange(n):
    matrix_item = raw_input()
    matrix.append(matrix_item)

text = ""
for i in xrange(m):
    for j in xrange(n):
        text += matrix[j][i]
        
# print matrix
print "text initial:", text

regex = r"([A-Za-z0-9]+)(?=([^A-Za-z0-9]+))(?!([A-Za-z0-9 ]+)$)"
repl = r"\1 \3"
# regex = r"([^A-Za-z0-9]+)(?!=([A-Za-z0-9 ]+)$)"
# repl = r""
text2 = re.sub(regex, repl, text)
print "after regex1:", text2


regex = r"[^A-Za-z0-9 ]+(?![^A-Za-z0-9 ]*$)"
repl = r""
text3 = re.sub(regex, repl, text2)
print text3

regex = r"[ ]+"
repl = r" "
text4 = re.sub(regex, repl, text3)
print text4
