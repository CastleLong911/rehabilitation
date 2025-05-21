def flatten(data):
    result = []

    for i in data:
        if isinstance(i, list):
            result += flatten(i)
        
        else:
            result.append(i)
    return result


print(flatten(['a', 1, 'b', True, 3.14, False, 'c']))