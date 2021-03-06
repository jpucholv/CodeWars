"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""

def solution(string, markers):
    strList = string.splitlines()
    index = 0

    for str in strList:
        for mark in markers:
            if str.find(mark) != -1:
                str = str[:str.find(mark)].strip()
        strList[index] = str
        index += 1

    return '\n'.join(strList)

print (solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))

'''
Best solution:

def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)
'''