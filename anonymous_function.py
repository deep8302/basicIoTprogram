'''In Python, anonymous function is a function that is defined without a name.

While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword.

Hence, anonymous functions are also called lambda functions.'''

double = lambda x: x * 2
print(double(5))


my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = tuple(filter(lambda x: (x*3), my_list))
print(new_list)



my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: (x*3), my_list))
print(new_list)


