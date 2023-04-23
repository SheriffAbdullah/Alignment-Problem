
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
    random.shuffle(chars)
    return chars

# Helper Function
def generateChars(charset):
    chars = [x for pair in zip(charset,charset) for x in pair]
    chars = [x for pair in zip(chars,chars) for x in pair]

    return chars

# 1) Randomize S1, S2
charset = ['A', 'C', 'G', 'T']

chars = generateChars(charset)
s1 = "".join(generateSequence(chars))

chars = generateChars(charset)
s2 = "".join(generateSequence(chars))

# TEST STUB
s1 = "ACACACTA"
s2 = "AGCACACA"

print(f"s1: {s1} \ns2: {s2}")

#%%

# ALIGNMENT MATRIX

l1 = len(s1)
l2 = len(s2)

# Match & Mismatch Scores
match_score = 2
mismatch_score = -1

# Initialise Alignment Matrix
alignment_matrix = [[0 for i in range(l1+1)] for i in range(l2+1)]


# Print Alignment Matrix
def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end='\t')
        print()
    print()

# printMatrix(alignment_matrix)


#%%

# The characters of 's1' are on the Top of the Matrix
# The characters of 's2' are to the Left of the Matrix

# 'i' iterates through every row
# 'j' iterates through every column

def dp(s1, s2, alignment_matrix, i, j):
    # If last row is completed, exit operations
    if i > len(s2):
        return alignment_matrix
    else:
        # If last element in row is reached, 
        if j > len(s1):
            # Go to the next row
            dp(s1, s2, alignment_matrix, i+1, 1)
            return alignment_matrix
        else:
            # MATCH
            if s1[j-1] == s2[i-1]:
                alignment_matrix[i][j] = alignment_matrix[i-1][j-1] + match_score
            # MISMATCH
            else:
                # DO NOT look at diagonal element if Mismatch
                alignment_matrix[i][j] = max(alignment_matrix[i-1][j] + mismatch_score, 
                                             alignment_matrix[i][j-1] + mismatch_score, 
                                             0)
            
            # CALL the function recursive on next cell (to the right)
            dp(s1, s2, alignment_matrix, i, j+1)
    
print()

# Calculate values of Alignment Matrix
dp(s1, s2, alignment_matrix, 1, 1)

print("*** Alignment Matrix ***\n")
printMatrix(alignment_matrix)

def tracepath(s1, s2, alignment_matrix, alignment1, alignment2, i, j):
    # If you reached a point of 'no match' = '0'
    if alignment_matrix[i][j] == 0:
        alignment1 = "".join(alignment1)[::-1]
        alignment2 = "".join(alignment2)[::-1]
        
        # Print the aligned sequences
        print(f"*** Alignment Sequence ***") 
        print(f"s1: {alignment1}")
        print(f"s2: {alignment2}")
    
        return
    
    # Temporary variable
    directions = [alignment_matrix[i-1][j-1], # DIAGONAL
                  alignment_matrix[i-1][j],   # UP
                  alignment_matrix[i][j-1]]   # LEFT
    
    direction = directions.index(max(directions))
    
    if direction == 0: # DIAGONAL
        alignment1.append(s1[j-1])
        alignment2.append(s2[i-1])
        tracepath(s1, s2, alignment_matrix, alignment1, alignment2, i-1, j-1)
    elif direction == 1: # UP
        # Gap in sequence 's1'
        alignment1.append('_')
        alignment2.append(s2[i-1])
        tracepath(s1, s2, alignment_matrix, alignment1, alignment2, i-1, j)
    else: # LEFT
        alignment1.append(s1[j-1])
        # Gap in sequence 's2'
        alignment2.append('_')
        tracepath(s1, s2, alignment_matrix, alignment1, alignment2, i, j-1)


# SCORES

# Score 12
i = 8
j = 8
print(f"\nAlignment Score = {alignment_matrix[i][j]}")
print(f"Start position: ({i}, {j})")
tracepath(s1, s2, alignment_matrix, [], [], i, j)

# Score 11
i = 7
j = 6
print(f"\nAlignment Score = {alignment_matrix[i][j]}")
print(f"Start position: ({i}, {j})")
tracepath(s1, s2, alignment_matrix, [], [], i, j)

# Score 10
i = 7
j = 7
print(f"\nAlignment Score = {alignment_matrix[i][j]}")
print(f"Start position: ({i}, {j})")
tracepath(s1, s2, alignment_matrix, [], [], i, j)

# Score 10
i = 8
j = 6
print(f"\nAlignment Score = {alignment_matrix[i][j]}")
print(f"Start position: ({i}, {j})")
tracepath(s1, s2, alignment_matrix, [], [], i, j)


#%%
    

'''
Note: Explore Wunsh-Needleman Algorithm
Difference between this and Smith-Waterman Algorithm - Local & Global Score

   A C A C A C T A
  0 0 0 0 0 0 0 0 0
A 0     
G 0        
C 0        
A 0
C 0
A 0
C 0
A 0

Assumptions:
(i) End at index [0,0].
(ii) Do not look at diagonal element in case of Mismatch.
'''

