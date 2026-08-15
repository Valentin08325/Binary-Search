def appending(l1):
    inputs = input("Give ur list here: ").split(',')
    for i in inputs:
        l1.append(int(i))
    return l1



print("-----------------------------------------------------")
result = []
appending(result)


#result = [12,7624,121,52,15,1,8,65,3,27,12]
result.sort()
target = int(input("What number are u searching for: "))
def binary_search(result, target):
    start = 0
    end = len(result)

    while start < end:
        mid = int((start + end) / 2)
        if result[mid] == target:
            return mid
        elif target < result[mid]:
            end = mid
        else:
            start = mid + 1
    return -1
index = binary_search(result, target)
l1 = int(index)
print("-----------------------------------------------------")
print(f"Sorted:\t{result}")
print(f"Index of {target} is {l1 + 1} from {len(result)}")
print("-----------------------------------------------------")
