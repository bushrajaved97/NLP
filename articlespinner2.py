# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:08:10 2019

@author: bushr
"""

import re
import itertools
 
def options(s):
    # If the chunk is not empty or the chunk start with the split parameter
    # return the split by the variable | of the paramter
    if len(s) > 0 and s[0] == '{':
        return [opt for opt in s[1:-1].split('|')]
    return [s]

comment ="""
Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
"""
chunk = re.split('(\{[^\}]+\}|[^\{\}]*)',comment)
 
# Return a list of lists of variations that can be combined
opt_lists = [options(frag) for frag in chunk]
 
for spec in itertools.product(*opt_lists):
    print((''.join(spec)))


 