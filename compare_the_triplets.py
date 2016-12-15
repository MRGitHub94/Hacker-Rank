"""Alice and Bob each created one problem for HackerRank. A reviewer rates the 
two challenges, awarding points on a scale from 1 to 100 for three categories:
problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet A = (a0, a1, a2),
and the rating for Bob's challenge to be the triplet B = (b0, b1, b2).

Your task is to find their comparison scores by comparing a0 to b0 etc. 

Given A and B, can you compare the two?"""

A = list(map(int, raw_input().strip().split()))
B = list(map(int, raw_input().strip().split()))

Ascore = len([1 for a,b in zip(A,B) if a > b])
Bscore = len([1 for a,b in zip(A,B) if a < b])

print Ascore, Bscore
# Above code will work for any length of vector. You can use sum instead of length
# as well. 

alice, bob = 0, 0
for a,b in zip(A,B):
    if a>b:
        alice += 1
    elif b>a: 
        bob += 1
print (alice, bob)