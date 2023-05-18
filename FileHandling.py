# as other concepts in python file handling is also easy in python
# Python treats files differently as text or binary and this is important.
# Each line of code includes a sequence of characters and they form a text file.
# Each line of a file is terminated with a special character, called the EOL or
# End of Line characters like comma {,} or newline character. It ends the current
# line and tells the interpreter a new one has begun. Let’s start with the reading
# and writing files.
# Working of open() function
# Before performing any operation on the file like reading or writing, first, we
# have to open that file. For this, we should use Python’s inbuilt function open()
# but at the time of opening, we have to specify the mode, which represents the
# purpose of the opening file.
#
# f = open(filename, mode)
# Where the following mode is supported:
#
# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains
# some data then it will be overridden but if the file is not present then it
# creates the file as well.
# a:  open an existing file for append operation. It won’t override existing data.
#  r+:  To read and write data into the file. The previous data in the file will
#  be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.

f = open('fileHandling','r')

for each in f:
    print(each)
f.close()
print()

# there is more than one way to read a file in python
file = open('fileHandling','r')
print(file.read())
file.close()
print()

file = open('fileHandling','r')
print(file.read(5)) # this statement prints output up to 5 characters in the output
file.close()
print()

file = open('fileHandling','r')
print(file.readline()) # used to read a single line from the specified file
file.close()
print()

file = open('fileHandling','r')
print(file.readlines()) # returns a list with each line as an element of the list
file.close()
print()

# in case of write or append if there is no existing file then a new file will be
# created with the given name or else the content will be written to the existing
# file
# mentioning 'x' as mode in the open method then it will just create a new file
# with that name and if the file already exists the it will return an error

file = open('fileHandling','a')
file.write('\nthis line will be written to the specified file')
file.close()
print()

# if we open the file in the 'w' mode then the existing content will be cleared and
# the new content will be written to the file

# in order to write multiple lines into the file at a time we can use writelines()
# method

file = open('fileHandling','a')
file.writelines(['\nthis is first line','\nthis is the second line'])
file.close()
print()

file = open('fileHandling','r')
print(file.tell()) # this gives the position of the filepointer in the file
file.seek(10) # this will change the pointer to specified position
print(file.tell())
file.close()



















