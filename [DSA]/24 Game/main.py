'''
You are given an integer array cards of length 4. 

You have four cards, each containing a number in the range [1, 9]. 

You should arrange the numbers on these cards in a mathematical expression 
using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:

The division operator '/' represents real division, not integer division.
For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.

Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.

You cannot concatenate numbers together
For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.

Return true if you can get such expression that evaluates to 24, and false otherwise.
'''

def judgePoint24(cards: list[int]):
    
    # converting into floats for precise measurement?
    nums = [float(num) for num in cards]
    
    bedmas_list = ["+", "-", "*", "/"]
    l1 = []
    
    for card in cards:
        pass
    
    return False

print(judgePoint24([4, 1, 8, 7])) # (4-8)*(1-7) = (-4)*(-6) = 24 
print(judgePoint24([1, 2, 1, 2])) # False
print(judgePoint24([3, 3, 8, 8])) # (8 / 3 - (8 / 3)) = 24 ... OMFG
print(judgePoint24([1, 9, 1, 2])) # (9-1)*(1+2) = 8 * 3 = 24
print(judgePoint24([8, 1, 6, 6])) # (6 / 1 - (6/8)) = (6 / 0.25) = 24