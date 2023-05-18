# Itertools is amodule in Python, it is used to iterate over data structures
# that can be stepped over using a for-loop.Such data structures are also
# known as iterables.This module works as a fast, memory-efficient tool
# that is used either by themselves or in combination to form iterator algebra.
#
# Why to use ?
# This module incorporates functions that utilize computational resources
# efficiently.Using this module also tends to enhance the readability and
# maintainability of the code.
#
# grouper Recipe The grouper() function can be found in the Recipes section
# of the itertools docs.The recipes are an excellent source of inspiration
# for ways to use itertools to your advantage.
import itertools as it
def grouper(inputs,n,fillvalue = None):
    iters = [iter(inputs)]*n
    return it.zip_longest(*iters,fillvalue = fillvalue)
alpha = ['g', 'e', 'e', 'k', 's', 'f', 'o',
         'r', 'g', 'e', 'e', 'k', 's']
print(list(grouper(alpha,3)))
