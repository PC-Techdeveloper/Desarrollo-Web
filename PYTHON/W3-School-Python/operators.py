"""
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""

# PYTHON ARITHMETIC OPERATORS -> +, -, *, /, %, **, //

# PYTHON ASSIGNMENT OPERATORS -> +=, -=, *=, %=, **=, //=

# PYTHON COMPARASION OPERATORS -> >, <, >=, <=, !==, ==

# PYTHON LOGICAL OPERATORS -> and, or, not

# PYTHON IDENTITY OPERATORS -> is, is not

# PYTHON MEMBERSHIP OPERATORS -> in, not in

"""
OPERATOR PRECEDENCE:

Parentheses has the highest precedence, meaning  that expressions inside parentheses must be evaluated first.
"""

print((6 + 3) - (6 + 3))

"""
Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions.
"""
print(100 + 5 * 3)

# PRECEDENCE

"""
() -> Parentheses	
** -> Exponentiation	
+x  -x  ~x -> Unary plus, unary minus, and bitwise NOT	
*  /  //  %	-> Multiplication, division, floor division, and modulus	
+  - -> Addition and subtraction	
<<  >>	-> Bitwise left and right shifts	
&	-> Bitwise AND	
^	-> Bitwise XOR	
|	-> Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in -> Comparisons, identity, and membership operators.
not	-> Logical NOT	
and	-> AND	
or -> OR
"""

"""
Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right.
"""
print(5 + 4 - 7 + 3)
