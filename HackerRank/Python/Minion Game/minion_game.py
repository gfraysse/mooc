def minion_game(string):
    # your code goes here
    vowels = ['A','E','I','O','U']
    
    Kevin = [] # consonants
    Stuart = [] # vowels
    Kevin_c = 0 # consonants
    Stuart_c = 0 # vowels
    
    for i in range(len(string)):
        #print string[i]
        if ord(string[i]) < ord('A') or ord(string[i]) > ord('Z'):
            raise "Invalid letter"
        if string[i] in vowels:
            Kevin_c += len(string) - i
            for j in range(i + 1, len(string) + 1):
                substring = string[i:j]
                #if substring not in Kevin:
                Kevin.append(substring)
        else:
            Stuart_c += len(string) - i
            #print string[i], "not in vowels"
            for j in range(i + 1, len(string) + 1):
                 substring = string[i:j]
                 #print substring
                 #if substring not in Stuart:
                 Stuart.append(substring)
                 #print "'" + substring + "' appended"

    print Kevin, len(Kevin), Kevin_c
    print Stuart, len(Stuart), Stuart_c
    # if len(Kevin) > len(Stuart):
    #     print "Kevin", len(Kevin)
    # elif len(Stuart) > len(Kevin):
    #     print "Stuart", len(Stuart)
    # else:
    #     print "Draw"
        
    if Kevin_c > Stuart_c:
        print "Kevin", Kevin_c
    elif Stuart_c > Kevin_c:
        print "Stuart", Stuart_c
    else:
        print "Draw"
    return    
    
if __name__ == '__main__':
  s = raw_input()
  minion_game(s)
