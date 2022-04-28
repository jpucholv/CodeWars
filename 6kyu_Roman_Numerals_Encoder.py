"""
Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Example:

solution(1000) # should return 'M'
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
Remember that there can't be more than 3 identical symbols in a row.

More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals
"""

u = ['','I','II','III','IV','V','VI','VII','VIII','IX']
d = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
c = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
m = ['','M','MM','MMM']

def solution(n):
    strN = str(n)
    sol = ""
    count = len(strN) - 1

    for a in strN:
        if count == 0:
            sol += u[int(a)]
        elif count == 1:
            sol += d[int(a)]
        elif count == 2:
            sol += c[int(a)]
        elif count == 3:
            sol += m[int(a)]
        count -= 1
    
    return sol
        
        

#print(solution(1287))

""" 
Best solution:

def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string
"""