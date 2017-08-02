def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    out = ''
    for character in s:
        if character.lower() not in ('a', 'e', 'i', 'o', 'u'):
            out += character
    print(out)

s = "Here is a simple sentence that makes sense. BYE."

print_without_vowels(s)
