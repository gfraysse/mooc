regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(.)(?=.\1)"# Do not delete 'r'.

#?: necessary to perform look ahead lookup
import re
P = raw_input()

#print bool(re.match(regex_integer_in_range, P))

# def displaymatch(match):
#     if match is None:
#         return None
#     return '<Match: %r, groups=%r>' % (match.group(), match.groups())

# print displaymatch(re.match(regex_alternating_repetitive_digit_pair, P))
# print re.findall(regex_alternating_repetitive_digit_pair, P)
# print len(re.findall(regex_alternating_repetitive_digit_pair, P))

print (bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
