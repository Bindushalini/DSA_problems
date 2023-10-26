

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# Your solution here.
for char in string:
    s.push(char)
while not s.is_stack_empty():
    reversed_string += s.pop()
print(reversed_string)
#
