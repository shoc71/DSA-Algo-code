'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

'''

def isMatch(s: str, p: str):
    
    # . = single character
    # * = zero, one or more instances
    
    test = 'testing...'
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    
    if s == p:
        return True
    
    if (s != p) and ('.' not in p) and ('*' not in p):
        return False
    
    string = [char for char in s]
    password = [char for char in p]
    
    bruh = f"s: {string}, p: {password}"
    
    def reAsterik(string, password):
        
        for index in range(len(password)):
            
            if index < len(password):
                # print(f"{index}. {password[index]} - length: {len(password)}")
                
                if password[index] == ".":
                    password[index] = string[index]
                
                if (password[index - 1] != string[index - 1]) and (password[index] == "*"):
                    print(f"Deleted: {password[index - 1]}{password[index]}")
                    del password[index] 
                    del password[index- 1]
                    
                    
        return ''.join(password)
            
    new_string = reAsterik(string, password)
    
    if new_string == s:
        return True
    
    return None

def isMatch2(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    
    # Create the DP table
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: empty pattern matches empty string
    dp[0][0] = True

    # Handle the case where pattern starts with a star
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]  # '*' can match zero of the previous character

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]  # Characters match or '.' matches any character
            elif p[j - 1] == '*':
                # '*' can either match zero occurrences (dp[i][j-2]) or more (dp[i-1][j])
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] if (s[i - 1] == p[j - 2] or p[j - 2] == '.') else False)

    return dp[m][n]

# Test cases
print(isMatch('aa', 'a'))    # False
print(isMatch('aa', 'a*'))   # True
print(isMatch('ab', '.*'))   # True
print(isMatch('ab', 'c*a*b'))# True
print(isMatch('efg', 'efd*'))# False


print(isMatch('aa', 'a')) # False
print(isMatch('aa', 'ab')) # False
print(isMatch('ab', '..')) # True
print(isMatch('pp', '..')) # True
print(isMatch('aa', 'aa')) # True
print(isMatch('aa', 'a*')) # True
print(isMatch('ab', '.*')) # True
print(isMatch('efg', 'efd*')) # False
print(isMatch('ab', 'c*a*b')) # True
print(isMatch('abc', 'a***abc')) # True
print(isMatch('aaa', 'ab*ac*a')) # True