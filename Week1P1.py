# Find and print the number of vowels in the string
s = 'azcbobobegghakl'
vowels = ['a', 'e', 'i', 'o', 'u']
total = 0
for vowel in vowels:
    total += s.count(vowel)

print('Number of vowels:', total)