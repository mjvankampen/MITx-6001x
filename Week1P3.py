# Find the largest alphabetical substring and print the first one
s = 'azcbobobegghaklbob'

maxS = [1] * len(s)
for i in range(0, len(s)):
    j = i
    while j < len(s) - 1 and s[j] <= s[j+1]:
        j += 1
        maxS[i] += 1

maxValue = max(maxS)
maxIndex = maxS.index(maxValue)
print('Longest substring in alphabetical order is:', s[maxIndex:maxIndex + maxValue])
