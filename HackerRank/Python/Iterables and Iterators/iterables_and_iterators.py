# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division
import itertools

n = int(raw_input())
letters = raw_input().split()
k = int(raw_input())

comb = itertools.combinations(letters, k)
c = itertools.combinations(letters, k)
l = len(list(c))

nb = itertools.ifilter(lambda x: 'a' in x, comb)
total = len(list(nb))
    
print("%.4f" % float(total / l))

