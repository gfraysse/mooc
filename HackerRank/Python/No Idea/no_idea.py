# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n, m = map(int, raw_input().split())
arr = map(int, sys.stdin.readline().split())
A = map(int, sys.stdin.readline().split())
B = map(int, sys.stdin.readline().split())

print sum([(i in A) - (i in B) for i in arr])

# A.sort()
# B.sort()
# arr.sort()

# happiness = 0
# prev_i = -1
# prev_happiness_inc = 0
# A_idx = 0
# B_idx = 0
# for i in arr:
#     #print "checking",i
#     if i == prev_i:
#         happiness += prev_happiness_inc

#     try:
#         A_idx = A.index(i)
#         prev_happiness_inc = 1
#         happiness += prev_happiness_inc
#         for j in range(A_idx):
#             A.pop(0)
#     except ValueError:        
#         try:
#             B_idx = B.index(i)
#             prev_happiness_inc = -1
#             happiness += prev_happiness_inc
            
#             for j in range(B_idx):
#                 B.pop(0)
#         except ValueError:
#             prev_happiness_inc = 0
            
#     # else:
#     #     found = False
#     #     if len(A) > 0:
#     #         cA = A[:]
#     #         for j in range(0, len(cA)):
#     #             #print "j", j, "cA", cA
#     #             if i == cA[j]:
#     #                 prev_happiness_inc = 1
#     #                 found = True
#     #                 happiness += prev_happiness_inc
#     #                 #print "found",i,"in A"
#     #                 break
#     #             elif i > cA[j]:
#     #                 A.pop(j)
#     #                 #print "A", A
#     #             else:
#     #                 break

#     #     if found == False and len(B) > 0:
#     #         cB = B[:]
#     #         for j in range(0, len(cB)):
#     #             #print j, cB
#     #             if i == cB[j]:
#     #                 prev_happiness_inc = -1
#     #                 found = True
#     #                 happiness += prev_happiness_inc
#     #                 #print "found",i,"in B"
#     #                 break
#     #             elif i > cB[j]:
#     #                 B.pop(j)
#     #                 #print "B",B
#     #             else:
#     #                 break
                    
#     #     if found == False:
#     #         prev_happiness_inc = 0
            

# # Not fast enough
# # import itertools
# # totalA = len(list(itertools.ifilter(lambda x: x in A, arr)))
# # totalB = len(list(itertools.ifilter(lambda x: x in B, arr)))

# print happiness
