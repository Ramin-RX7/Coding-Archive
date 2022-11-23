############################################
'''Write a Python function to insert a string in the middle of a string'''
def insert_string_middle(s, word):
  a=len(word)
  a=a/2 +1
  #x= word[:a]+s+word[a:]
  #return x
#print(insert_string_middle('Ali','Ramins'))
############################################

############################################
''' -front_back
 Consider dividing a string into two halves.
 If the length is even, the front and back halves are the same length.
 If the length is odd, we'll say that the extra char goes in the front half.
 e.g. 'abcde', the front half is 'abc', the back half 'de'.
 Given 2 strings, a and b, return a string of the form
  a-front + b-front + a-back + b-back'''
"""def front_back(a, b):
  lena=len(a)
  lenb=len(b)
  if lena%2==0:
    frontA= a[:lena/2+1]
    backA=  a[lena/2+1:]
  else:
    frontA= a[:lena/2+1.5]
    backA=  a[lena/2+1.5:]    
  print(frontA,backA)
front_back('ramin','ali')"""
############################################

############################################
''' -Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.'''
def remove_adjacent(nums):
  # +++your code here+++
  return
############################################

############################################
''' -Given two lists sorted in increasing order, create and return a merged
 list of all the elements in sorted order. You may modify the passed in lists.
 Ideally, the solution should work in "linear" time, making a single
 pass of both lists.'''
def linear_merge(list1, list2):
  # +++your code here+++
  return
############################################

############################################
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
############################################




# when you run this file, the program runs the following:
if __name__ == if __name__ == "__main__":
    
