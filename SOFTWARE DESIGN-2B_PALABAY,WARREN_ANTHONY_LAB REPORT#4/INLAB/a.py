def recursive_min(data):
    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]
    return min(data[0], recursive_min(data[1:]))
def recursive_max(data):
    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]
    return max(data[0], recursive_max(data[1:]))
def recursiveRev(data):
    if len(data) <= 1:
        return data
    return recursiveRev(data[1:])+ [data[0]]
print(recursive_min([1,2,3,4,5,6]))
print(recursive_max([1,2,3,4,5,6]))
print(recursiveRev([1,2,3,4,5,6]))