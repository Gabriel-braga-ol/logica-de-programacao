"""Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 """

s = '   fly me   to   the moon  '

split = s.split()

i = 0

while i < len(split):
    print(len(split[-1]))
    i += 1
    break
