# Enter your code here. Read input from STDIN. Print output to STDOUT
company_name=raw_input()
occurence = {}

for letter in company_name:
    if letter in occurence:
        occurence[letter] += 1
    else:
        occurence[letter] = 1

# first we sort the keys by alphabetical order
occurence_l = occurence.items()
# then we sort the values by value, in reverse order to have the letters with the most occurences at the beginning
tmp = sorted(occurence_l, key=lambda occurence_l:occurence_l[0])
result = sorted(tmp, key=lambda tmp:tmp[1], reverse=True)

# alternative, same result
# from operator import itemgetter, attrgetter
# result = sorted(occurence_l, key=itemgetter(1), reverse=True)

for i in range(3):
    print result[i][0],result[i][1]
