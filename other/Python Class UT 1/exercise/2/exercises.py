'''-MixUp
 Given strings a and b, return a single string with a and b separated
 by a space '<a> <b>', except swap the first 2 chars of each string.
 e.g.
   'mix', 'pod' -> 'pox mid'
   'dog', 'dinner' -> 'dig donner'
 Assume a and b are length 2 or more.'''
def mix_up(a, b):
  # +++your code here+++
  return




''' -verbing
Given a string, if its length is at least 3,
add 'ing' to its end.
Unless it already ends in 'ing', in which case
add 'ly' instead.
If the string length is less than 3, leave it unchanged.
Return the resulting string.'''
def verbing(s):
  # +++your code here+++
  return



'''Write a Python function to remove the nth index character from a nonempty string.'''
def remove_char(s, n):
  # +++your code here+++
  return



'''Write a Python program to change a given string to a new string
where the first and last chars have been exchanged.'''
def change_string(str1):
  # +++your code here+++
  return



'''Write a Python function to insert a string in the middle of a string'''
def insert_string_middle(s, word):
  # +++your code here+++
  return




'''-donuts
 Given an int count of a number of donuts, return a string
 of the form 'Number of donuts: <count>', where <count> is the number
 passed in. However, if the count is 10 or more, then use the word 'many'
 instead of the actual count.
 So donuts(5) returns 'Number of donuts: 5'
 and donuts(23) returns 'Number of donuts: many'''
def donuts(count):
  if count >= 10:
       return 'number of donuts: many'
  else:
       return 'number of donuts:' + str(count)
 
      


'''-both_ends
 Given a string s, return a string made of the first 2
 and the last 2 chars of the original string,
 so 'spring' yields 'spng'. However, if the string length
 is less than 2, return instead the empty string.'''
def both_ends(s):
  # +++your code here+++
  return




''' -front_back
 Consider dividing a string into two halves.
 If the length is even, the front and back halves are the same length.
 If the length is odd, we'll say that the extra char goes in the front half.
 e.g. 'abcde', the front half is 'abc', the back half 'de'.
 Given 2 strings, a and b, return a string of the form
  a-front + b-front + a-back + b-back'''
def front_back(a, b):
  # +++your code here+++
  return




'''-fix_start
 Given a string s, return a string
 where all occurences of its first char have
 been changed to 'f*', except do not change
 the first char itself.
 e.g. 'babble' yields 'ba**le'
 Assume that the string is length 1 or more.
 Hint: s.replace(stra, strb) returns a version of string s
 where all instances of stra have been replaced by strb.'''
def fix_start(s):
  # +++your code here+++
  return s [0] + s[1:].replace(s[0], '*')





''' The goal of this exercise is to convert a string to a new string
 where each character in the new string is '(' if that character
 appears only once in the original string, or ')' if that character
 appears more than once in the original string. Ignore capitalization
 when determining if a character is a duplicate.
 Examples:
 "din" => "((("
 "recede" => "()()()"
 "Success" => ")())())"
 "(( @" => "))(("
'''
def duplicate_encode(word):
  # +++your code here+++
  return




''' This time no story, no theory. The examples below show you how to write function accum:
 Examples:
 accum("abcd") -> "A-Bb-Ccc-Dddd"
 accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
 accum("cwAt") -> "C-Ww-Aaa-Tttt"
 The parameter of accum is a string which includes only letters from a..z and A..Z.
'''
def accum(word):
  # +++your code here+++
  return


''' The parameter weekday is True if it is a weekday,
 and the parameter vacation is True if we are on vacation.
 We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
 sleep_in(False, False) → True
 sleep_in(True, False) → False
 sleep_in(False, True) → True '''
def sleep_in(weekday, vacation):
  # +++your code here+++
  return



''' Write a function called accept_login(users, username, password)
 with three parameters: users a dictionary of username
 keys and password values, username a string for a login name and
 password a string for a password. The function should return
 True if the user exists and the password is correct and False otherwise'''
def accept_login(users, username, password):
  # +++your code here+++
  return



'''Write a function that takes in a string of one or more words,
and returns the same string, but with all five or more letter words reversed
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
Examples:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
'''
def spin_words(sentence):
  # +++your code here+++
  return




''' -match_ends
 Given a list of strings, return the count of the number of
 strings where the string length is 2 or more and the first
 and last chars of the string are the same.
 Note: python does not have a ++ operator, but += works.
 examples:['aba', 'xyz', 'aa', 'x', 'bbb'] should return 3
          ['', 'x', 'xy', 'xyx', 'xx'] should return 2 '''
def match_ends(words):
  count = 0
  for word in words:
    if len(word) >=2 and word[0] ==word[-1]:
      count= count + 1
  return count





''' -front_x
 Given a list of strings, return a list with the strings
 in sorted order, except group all the strings that begin with 'x' first.
 e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
 ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
 Hint: this can be done by making 2 lists and sorting each of them
 before combining them.'''
def front_x(words):
  # +++your code here+++
  return



''' -Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.'''
def remove_adjacent(nums):
  # +++your code here+++
  return




''' -sort_last
 Given a list of non-empty tuples, return a list sorted in increasing
 order by the last element in each tuple.
 e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
 [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
 Hint: use a custom key= function to extract the last element form each tuple.'''
def sort_last(tuples):
  # +++your code here+++
  return



''' -Given two lists sorted in increasing order, create and return a merged
 list of all the elements in sorted order. You may modify the passed in lists.
 Ideally, the solution should work in "linear" time, making a single
 pass of both lists.'''
def linear_merge(list1, list2):
  # +++your code here+++
  return



'''John has invited some friends. His list is:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
Could you make a program that

makes this string uppercase
gives it sorted in alphabetical order by last name.
When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.

So the result of function meeting(s) will be:

"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
'''
def meeting(s):
  # +++your code here+++
  return





# when you run this file, the program runs the following:
if __name__=='__main__':
  print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))
