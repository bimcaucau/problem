s = "BANANA"
list_s = list(s)
vowels = []
consonants = []
consonants_score = []
some_list = []
another_list = []
#tim ra tap hop nguyen am va phu am
for i in list_s:
    if i == "A" or i == "I" or i == "E" or i == "O" or i == "U":
        vowels.append(i)
    else: consonants.append(i)
vowels = list(dict.fromkeys(vowels))
consonants = list(dict.fromkeys(consonants))
##########################################
# lan luot tim ra cac tu co the tao tu phu am
for w in list_s:
    for c in consonants:
        if c == w:
            for i in range(1,len(list_s)+1):
                text2 = s[list_s.index(w):list_s.index(w)+i]
                some_list.append(text2)

some_list=list(dict.fromkeys(some_list))

# tao ra cac tu tu phu am va so sanh de tim diem
for i in range(0,len(list_s)+1):
    for k in range(1,len(list_s)+1):
        if i+k<=len(list_s):
            text_n = s[i:i+k]
            if text_n in some_list:
                another_list.append(text_n)
        else: continue
            
result = len(another_list)
        

