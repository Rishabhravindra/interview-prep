from functools import reduce

# map(function, list) - divide each num by 2

newarr = [x*2 for x in range(4)]
lst1 = list(map(lambda x: int(x/2),newarr))

# filter(function, list) - get positive numbers
newarr2 = range(-5,5)
lst2 = list(filter(lambda x: x > 0,newarr2))

#reduce(function, list) - multiply all numbers
newarr3 = [1,2,3,4]
lst3 = reduce(lambda x,y: x* y, newarr3)

#zip(list1,list2) - add corresponding elements in one list
"""
This function returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The returned list is truncated in length to the length of the shortest argument sequence. When there are multiple arguments which are all of the same length, zip() is similar to map() with an initial argument of None. With a single sequence argument, it returns a list of 1-tuples. With no arguments, it returns an empty list.
"""

newarr4 = [_ for _ in range(5)]
newarr5 = list(map(lambda x: x*x, newarr4))

newarr6 = list(zip(newarr4,newarr5))