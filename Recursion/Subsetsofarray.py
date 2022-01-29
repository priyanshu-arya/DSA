li = []

def subsetsofArray(nums):
    for num in nums:
        if len(li) == 0:
            li.append([])
            li.append([num])
        else:
            temp = [l.copy() for l in li]
            for l in temp:
                l.append(num)
            li.extend(temp)

subsetsofArray([1,2,3, 4, 5])
print(len(li))