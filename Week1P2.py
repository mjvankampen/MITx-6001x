# Find number of bob in string s
s = 'azcbobobegghakl'

bobs = 0
for i in range(0,len(s)-2):
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        bobs += 1
print('Number of times bob occurs is:', bobs)

