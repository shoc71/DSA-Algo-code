'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''

def convert(s: str, numRows: int):
    
    if numRows == 1:
        return s
    
    dictk = {order:[] for order in range(numRows)}

    x = 0
    direction = -1
    l1 = []
    
    for char in s:
        dictk[x].append(char)
        
        if x == 0 or x == numRows - 1:
            direction *= -1
            
        x += direction
        
    for key, val in dictk.items():
        l1 += val
        
    return ''.join(l1)

print(convert(s = "PAYPALISHIRING", numRows = 3))
print(convert(s = "PAYPALISHIRING", numRows = 4))
print(convert(s = "A", numRows = 1))