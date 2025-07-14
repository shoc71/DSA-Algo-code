'''
Based on this problem; https://www.geeksforgeeks.org/dsa/window-sliding-technique/
'''

def maxSum(array: list[float], length: int) -> float:
    '''
    Looking for biggest sum given an array of numbers and specific window size.
        Arguments:
            - Array of intergers/floats
            - Size of window(interger)
        Returns:
            Highest Window Sum in the given Array
    '''
    
    # if window is bigger than array
    if length > len(array):
        return -1

    totalSum = sum(array[:length])
    
    for i in range(len(array)):
        
        if (i + length) > len(array):
            continue
        
        list2 = array[i : i + length]
        
        if sum(list2) > totalSum:
            totalSum = sum(list2)           
    
    return totalSum

# test
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maxSum(arr, k))

arr1 = [18.6848, 34.5281, 12.6609, 24.5217, 
        7.4155, 37.3903, 52.5677, 23.9809, 
        31.6117, 37.1831, 21.5177, 7.9505, 
        7.1734, 2.5243, 54.5733, 12.1835, 
        44.7703, 52.7321, 50.0423, 28.5275]
k1 = 3
print(maxSum(arr1, k1))