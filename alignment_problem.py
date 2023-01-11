
'''
1) Randomized Sequence s1 & s2
* ONLY Recursive function calls *

2) 

3) 1st 

Computational Complexity & Time Complexity

Outputs:
-> Alignment Matrix
-> Traceback for 4 Matches + Alignment (with gaps)
-> 

'''

#%%

import random

random.seed(10)

# Recursive Function
def generateSequence(chars):
    if chars:
        c = chars[random.randint(0, len(chars)-1)]
        chars.remove(c)
        return c + generateSequence(chars)
    else:
        return ""
    
# Helper Function
def generateChars(setchar):
    chars = [x for pair in zip(charset,charset) for x in pair]
    chars = [x for pair in zip(chars,chars) for x in pair]

    return chars

# 1) Randomize S1, S2
charset = ['A', 'C', 'G', 'T']

chars = generateChars(charset)
s1 = generateSequence(chars)

chars = generateChars(charset)
s2 = generateSequence(chars)

print(f"s1: {s1} \ns2: {s2}")

#%%

def printAlignmentMatrix(alignment_matrix):
    for i in alignment_matrix:
        for j in i:
            print(j, end='\t')
        print()

printAlignmentMatrix(alignment_matrix)


#%%

def dp(s1, s2, alignment_matrix, i_curr, j_curr):
    print(i_curr, j_curr)
    
    if (i_curr > len(s1) or j_curr > len(s2)):
        return alignment_matrix

    # MATCH
    if s1[j_curr-1] == s2[i_curr-1]:
        alignment_matrix[i_curr][j_curr] = alignment_matrix[i_curr-1][j_curr-1] + match_score;
    # MISMATCH
    else:
        alignment_matrix[i_curr][j_curr] = max(alignment_matrix[i_curr-1][j_curr], alignment_matrix[i_curr][j_curr-1]) + mismatch_score;

    dp(s1, s2, alignment_matrix, i_curr+1, j_curr)
    dp(s1, s2, alignment_matrix, i_curr, j_curr+1)
        
# ALIGNMENT MATRIX

l1 = 16
l2 = 16

match_score = 5
mismatch_score = -4

alignment_matrix = [[0 for i in range(l1+1)] for i in range(l2+1)]

printAlignmentMatrix(dp(s1, s2, alignment_matrix, 1, 1))



