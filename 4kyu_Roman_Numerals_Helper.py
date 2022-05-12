'''
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
Help
Symbol	Value
I	1
IV	4
V	5
X	10
L	50
C	100
D	500
M	1000
'''

roman_numerals = {
    'I':    1,
    'IV':   4,
    'V':    5,
    'IX':   9,
    'X':	10,
    'XL':   40,
    'L':	50,
    'XC':   90,
    'C':	100,
    'CD':   400,
    'D':	500,
    'CM':   900,
    'M':	1000,
    }
    
class RomanNumerals:

    def to_roman(val):
        roman_string = ''
        for key, value in reversed(roman_numerals.items()):
            while val >= value:
                roman_string += key
                val -= value
        return roman_string

    def from_roman(roman_num):
        num = 0
        while len(roman_num) > 0:
            for key, value in roman_numerals.items():
                if roman_num.endswith(key):
                    num += value
                    roman_num = roman_num[:-len(key)]
        return num

'''
BEST SOLUTION:

import string
from collections import OrderedDict

class RomanNumerals:
  @classmethod
  def to_roman(self, num):
    conversions = OrderedDict([('M',1000), ('CM',900), ('D', 500), ('CD',400), ('C',100), ('XC',90), ('L',50), ('XL',40),
                               ('X',10), ('IX',9), ('V',5), ('IV',4), ('I',1)])
    out = ''
    for key, value in conversions.iteritems():
      while num >= value:
        out += key
        num -= value
    return out
  
  @classmethod
  def from_roman(self, roman):
    conversions = OrderedDict([('CM',900), ('CD',400), ('XC',90), ('XL',40), ('IX',9), ('IV',4), ('M',1000), ('D',500),
                               ('C',100), ('L',50), ('X',10), ('V',5), ('I',1)])
    out = 0
    for key, value in conversions.iteritems():
      out += value * roman.count(key)
      roman = string.replace(roman, key, "")
    return out
    
    SECOND ONE:
    ROMANS = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'C': 100,
    'XC': 90,
    'L': 50,
    'X': 10,
    'V': 5,
    'IV': 4,
    'I': 1,
}
    
class RomanNumerals:
    
    def to_roman(n):
        s = ''
        for key, value in ROMANS.items():
            while n % value != n:
                n = n - value
                s += key
        return s
    
    def from_roman(r):
        s = 0
        for key, value in ROMANS.items():
            while r.startswith(key):
                r = r[len(key):]
                s += value
        return s
    '''

