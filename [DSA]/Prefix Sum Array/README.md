# Prefix Sum Array - Implementation

" Given an array arr[], Find the prefix sum of the array. A prefix sum array is another array prefixSum[] of the same size, such that prefixSum[i] is arr[0] + arr[1] + arr[2] . . . arr[i]. "

```py
Input: arr[] = [10, 20, 10, 5, 15]
Output: [10, 30, 40, 45, 60]
Explanation: For each index i, add all the elements from 0 to i:
prefixSum[0] = 10, 
prefixSum[1] = 10 + 20 = 30, 
prefixSum[2] = 10 + 20 + 10 = 40 and so on.

Input: arr[] = [30, 10, 10, 5, 50]
Output: [30, 40, 50, 55, 105]
Explanation: For each index i, add all the elements from 0 to i:
prefixSum[0] = 30, 
prefixSum[1] = 30 + 10 = 40,
prefixSum[2] = 30 + 10+ 10 = 50 and so on.
```

--- GeeksforGeeks (2025)
https://www.geeksforgeeks.org/dsa/prefix-sum-array-implementation-applications-competitive-programming/