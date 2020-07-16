# There are 4 relational operators.
# the output of this operations is always a boolean_value

# < , > , <= , >=

x = 10
y = 41
print(x < y)  # true
print(x > y)  # false
print()

a = 'hii'
b = 'python'
print(a <= b)  # true
print(a >= b)  # false
print()
# When Relational operations are performed on strings it compares the unicode integer

# ord() is used to find unicode no. of the char.
cm = 'A'
cn = 'a'
print()
print(ord(cm))  # 65
print(ord(cn))  # 97
# String comparision with integer is not possible.
print()

# chaining of Relational operator
print(ord('w'))
print(ord('x'))
print(ord('y'))
print(ord('z'))

print('w' < 'x' > 'y' < 'z')
# here if any one is false then whole becomes false
print()

# equality_operator ==,!=
x = 10
y = 20.20
print(x == y)  # false
print(x != y)  # true
print()
print(1 == True)  # true
print(1 == False)  # false
print()
print('hello' == 'Hypame')  # false
print('saf' == 'saf')  # true
print()

# logical_operators AND,OR,NOT
# zero and empty_str_('') are considered to be false
x = 0
y = 20
print(x and y)  # y will return
print(x or y)  # x will return

# bitwise operator works with Integer and Boolean
#  '&' '|'  '^'   '~'
# 'AND OR  XOR  Compliment'
# integer converts to Binary_Numbers
# there is conversion of numbers to binary then each binary value is compared
# with the operators
print(9 & 10)  # 8
# 0b1001(binary 9)
# 0b1100(binary 12)
# comparing[up-down] '1&1', '0&1', '0&0', '1&0'
# 0b1001 & 0b1100 = 0b1000 -> { 8 }

# identity operators
# is , is not => returns boolean values
x =10
y = 20
print(x is y)
print(x is not y)
print()

m = 'Sarif'
n = 'Sarif'
print(n is m)# case of alphabets matters
print()

# Membership_Operators
# in , not in
# return boolean
# comparison between Key - Sequences
# key[single_Entity] Sequence[set,list,tuples,dictionaries]
# return true if {key} is found in the {sequence}.
s = 'hello_python'
print('e' in s)
print('H' in s)
print('o_p' in s)




