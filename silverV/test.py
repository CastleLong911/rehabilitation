required_keys = ["name", "email", "age"]
user = {"name": "보라", "age": 20}

not_exist_keys = []

for key in required_keys:
    if key not in user.keys():
        not_exist_keys.append(key)

print("누락된 키:", not_exist_keys)