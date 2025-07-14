array = [10, 20, 10, 5, 15]
hihi = [34.2491, 11.4438, 26.1676, 55.9294, 13.0099, 17.212, 9.0531, 30.0254, 73.8122, 59.5177, 6.7974, 9.6232, 17.0933, 7.6, 7.1459, 50.8055, 82.4401, 25.379, 91.9823, 32.9663]

def prefSum(array):
    newlist = []
    for i in range(1, len(array) + 1):
        list_num_sum = sum(array[:i])
        rounded_num = round(list_num_sum, 4)
        newlist.append(rounded_num)
    
    return newlist

def prefSum2(array):
    return [round(sum(array[:i]), 4) for i in range(1, len(array) + 1)]
    # hope this gave you a good laugh
    # I call this, good luck one-liner function

print(prefSum(array))
# print(prefSum2(array))

print(prefSum(hihi))
# print(prefSum2(hihi))