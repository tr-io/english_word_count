from nltk.corpus import words
import re

word_list = words.words()
num_oo = 0
num_ee = 0
idx = 1
for x in word_list:
    oor = re.search('(oo)', x)
    eer = re.search('(ee)', x)

    if bool(oor):
        num_oo += 1
        print(f"oo matched: {x}")
    
    if bool(eer):
        num_ee += 1
        print(f"ee matched: {x}")
    
    idx += 1

print(f"Num OO: {num_oo}")
print(f"Num EE: {num_ee}")
print(f"Num words: {idx}")