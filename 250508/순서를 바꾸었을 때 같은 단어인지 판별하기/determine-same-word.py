word1 = input()
word2 = input()

# Please write your code here.
word1_S = sorted(word1)
word2_S = sorted(word2)

if word1_S == word2_S:
    print('Yes')
else:
    print('No')