# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# 
# RegEx can be used to check if a string contains the specified search pattern.
#raw string is a string which is prefixed with r and it tells python not to handle
# back slashes in any special way for example tabs,new lines etc.
print('\tTab')
print(r'\tTab')
import re
#re module consists of compile(),search(),match(),find() and split() etc...
text_to_search = '''abcdefghijklmnopqrstuvxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

234-343-5588
544.243.5667
435*345*2354
800-343-5588
900-343-5588

Mr. Madhan Kumar
Mrs Harsha
Mr Ganesh
Ms. Laxmi


cat
mat
rat
pat
bat

'''
# text_to_search = '''iam a doc.tor.
# iam an engineer.
# iam an architect.
# I AM a student.
# 233455789
# 4367468'''
#pattern = re.compile(r'iam')# it is case sensitive
#pattern = re.compile(r'.')#dot is a special character in regular expression
# to escape special function of char we use back slash
#pattern = re.compile(r'\.')
#pattern = re.compile(r'doc\.tor')
#pattern = re.compile(r'\d')#gives digits from 0-9
#pattern = re.compile(r'\D')#searches for a char which is not a digit
#similarly \w for word caharacter
#\W for not a word character
#\s for white space(space ,tab ,new line)
#\S for not white space
#\b for word boundary
#\B for not a word boundary
#^ for beginning of a string
#pattern = re.compile(r'^iam')
#$ for end of a string
# pattern = re.compile(r'4367468$')
#[] matches characters in brackets
#[^ ] matches characters not in bracket
#having a space before required charachter is word boundary
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')#if we use dot in betweeen then
#we get all the matchings with any symbol in between
# but if we use a square bracet then it will match only to the given symbols in the
# square brackets. using square brackets means creating a character set.
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[1-5]')#this to specify a range
# pattern = re.compile(r'[a-zA-Z]')#^ NEGATES THE SET
# pattern = re.compile(r'[^a-zA-Z]')

#quantifiers :
# * - 0 or more
# + - 1 or more
# ? - 0 or 1
# {3} - exact number
# {3,4} - range of numbers(min,max).
# pattern = re.compile(r'[^b]at')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# to print names
#() - group
#| - either OR
# pattern = re.compile(r'M[r]*[s]*\.?\s[A-Z]\w*')
#for substituting we use sub() 
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches :
    print(match)
# print(text_to_search[0:3])

