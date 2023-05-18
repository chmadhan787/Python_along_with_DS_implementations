# a regular expression is a string that contains special symbols and characters
#we use raw strins in regex ie string prefixed with r like
#print(r'madhan') it is a raw string. these raw strings ignores special symbols
#like \n,\t,\b etc...the alternative os raw string is to use another \ before
#special symbol ex: print('m\\b\\w')
import re
prog = re.compile(r'm\w\w')
#w represents one character in [A-Z],[a-z],[0-9]
#gives digits from 0-9
#searches for a char which is not a digit
#similarly \w for word caharacter
#\W for not a word character
#\s for white space(space ,tab ,new line)
#\S for not white space
#\b for word boundary
#\B for not a word boundary
#^ for beginning of a string
#\A matches only at start of string
#\Z matches only at  end of the string
#prog represents an object that contains a regula expression
string_to_search = 'cat mat bat rat'
result = prog.search(string_to_search)#searching regex
#the result stored in result can be displayed by calling the group() method
print(result.group())
string_to_search1 = 'operating system format'
#after compiling the regex in one obj the same obj can be used with the
#different strings
result = prog.search(string_to_search1)
print(result.group())
#instead of compiling once and searching next we can do it in single line as
result = re.search(r'm\w\w',string_to_search)
print(result.group())
#so genral form of writing the regular expressions is as follows
#result = re.search('expression','string')
s = 'mat man mad car dad rat'
result = re.search(r'm\w\w',s)
print(result.group())
#search() will return only the first string which matches the regular expression
#to get all the strings we use findall() method it returns a list
result = re.findall(r'm\w\w',s)
print(result)
# the elements of result list can be displayed as
for i in result:
    print(i)
#match() will returns the resultant string only if it is present in the beginning
#of the string
s1 = 'man sun mop run'
s2 = 'sun mop run'
result = re.match(r'm\w\w',s1)
print(result.group())
result = re.match(r'm\w\w',s2)
#print(result.group()) this returns nonetype error
#split() splits the regular expression into parts according to regex and forms a list
result = re.split(r'\W+',s1)#+ represents to match one or more occurances indicated
#by W
print(result)
s3 = 'this;is the:core python\'s.book'
result = re.split(r'\W+',s3)
print(result)
#sub(regex,new_string,string) is used to find the string and replce it with new string
s4 = 'kumbhamela will be conducted at ahmedabad in india'
result = re.sub(r'ahmedabad','allahabad',s4)
print(result)
#therefore regular expressions can be used to :
#1.Matching the strings
#2.Searching for strings
#3.Finding all strings
#4.Splitting a string into peices
#5.Replacing the strings.

s5 = 'an apple a day keeps a doctor away'
result = re.findall(r'a[\w]*',s5)#returns list of strings starting with 'a'
print(result)
#as we observe the out we will get 'ay' ie part of day it is not a word to get rid
#of this we need to mention tho boundaries of the word ,in the above string each word
#is having spaces at boundaries at both ends hence we can modify regex as
result = re.findall(r'\ba[\w]*\b',s5)
print(result)#this works fine

#quantifiers :
#characters represent more than one charater to be matched sre called quantifiers
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
s6 = 'the meeting will be conducted on 1st and 21st of every month'
result = re.findall(r'\d[\w]*',s6)
print(result)
#to retrive m letters length word from the string
s7 = 'one two three four five six seven'
result = re.findall(r'\b\w{5}\b',s7)
print(result)
#to retrive m and greater than m letters length
result = re.findall(r'\b\w{4,}\b',s7)
print(result)
#to retrive m to n letters length
result = re.findall(r'\b\w{3,5}\b',s7)
print(result)
#retrieving digits from the string
s8 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
result = re.findall(r'\b\d\b',s8)#for single digit
print(result)
result = re.findall(r'\b\d\d\b',s8)#for double digit
print(result)
#to find whether a string contains a word starting with 't' or not at the end
s9 = 'one two three one two three'
result = re.findall(r't[\w]*\Z',s9)
print(result)#llly we can do with \A for starting of string
#retrieving phone number from the string
s10 = 'madhan kumar:9949199787'
result = re.findall(r'\d+',s10)
print(result)
#to print name
result = re.findall(r'\D+',s10)
print(result)
s11 = 'anil akhil ananth arun arathi arundathi abhijith ankur abhinay'
result = re.findall(r'a[nk][\w]*',s11)#prints names starting with an or ak or ank
print(result)
s12 = 'vijay 20 1-5-2001, rohit 21 22-10-1990, sita 22 15-09-2000'
result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',s12)
print(result)

#special characters in regex:
#\ - Escape special character nature
#. - Matches any character except new line
#^ - Matches begining of string
#$ - Matches ending of string
#[...] - Denotes a set of possible characters, Ex:[6b-d] Matches any characters
#'6','b','c' or 'd'
#[^...] - Matches every character except the ones inside the bracets. Ex:[^a-c6]
# matches any character except 'a','b','c' or '6'
#(...) - Matches the regular expression inside the parantheses and the result can
# be captured
#R|S - matches either regex R or regex S.

#string strt with 'He' or not
s13 = 'Hello World'
result = re.findall(r'^He',s13)
if result:
    print('string starts with \'He\'')
else:
    print('no')
result = re.findall(r'World$',s13)
if result:
    print('string ends with \'World\'')
else:
    print('no')
#ignorecase
result = re.findall(r'world$',s13,re.IGNORECASE)
print(result)
#names
s14 = 'Rahul got 75 marks, Vijay got 89 marks, Subbu got 88 marks'
result = re.findall(r'[A-Z][a-z]*',s14)
print(result)
result = re.findall(r'\d{2}',s14)
print(result)
# using pipe |
s15 = 'i may return at 8pm or 9pm and go to work a 6am or 7am'
result = re.findall(r'\dam|\dpm',s15)
print(result)
#using regex on files for this
# first we need to open the file as
# f = open('filename','r')
# to compare
# for line in f:
#   res = re.findall('regex',line) and for printing result
#   if len(res)>0:
#       print(res).
f = open('regex_with_filehandling.txt','r')
for line in f:
    res = re.findall(r'\S+@\S+',line)
    if len(res)>0:
        print(res)
f.close()

f = open('salaries.txt','r')
f1 = open('newfile.txt','w')
for line in f:
    res = re.search(r'\d{4}',line)
    res1 = re.search(r'\d{4,}.\d{2}',line)
    f1.write(res.group()+'\t')
    f1.write(res1.group()+'\n')
    print(res.group(),res1.group())
f.close()
f1.close()

 