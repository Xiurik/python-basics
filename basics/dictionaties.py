# Dictionary, is an order key value peer [KEY : VALUE]
# The key must be unmutable and unique, we can use numbers, string, a boolean but not list for example, is we repeat
# the key it will return the last key with that name, the others will be ignored
import docstring

dictionary = {
    "a": [1, 2, 3, 4],
    "b": "Xiurik",
    "c": True,
}

dic_list = [
    {
        "a": [1, 2, 3, 4],
        "b": "Xiurik",
        "c": True,
    },
    {
        6: [5, 6, 7, 8],
        False: "Xhakal",
        "is_big": True,
    },
]

print(dic_list[0]["a"][3], dic_list[1][6][3], dic_list[1]["is_big"])
print(dictionary["a"][0])
print()

# With this get we will receive None in case what we want to get does not exist in the dictionary
print(dictionary.get("d"))
# We can also send a default value in case the key does not exist
print(dictionary.get("d", "Xiurik"))
print()

# Another way to create a dictionary
user = dict(name="Xiurik", age=30, is_married=True, likes_music=True, is_sexual=True, sex_per_day=3)
print(user)
print()

# A way to validate if a key exist in a dictionary is using IN keyword like in list, it will return True or False
print("is_cool KEY exist?", "is_cool" in user)
print()

# Validate if exist in KEYS only
print("Xiurik exist on KEYS?", "Xiurik" in user.keys())
print()

# Validate if exist in VALUES only
print("Xiurik exist on VALUES?", "Xiurik" in user.values())
print()

# See the full list items in Touples
print(user.items())
print()

# Clears the dictionary
# user.clear()

# Copy and create a new dictionary
user2 = user.copy()
user.clear()
print("user", user)
print("user2", user2)
print()

# Removes a key and return its value
print(user2.pop("age"))
print(user2)
print()

# Removes randomly value, usually the last one
print(user2.popitem())
print(user2)
print()

# Update a key value, if the key does not exist, it will add it
print(user2.update({"name": "Xhakal"}))
print(user2.update({"likes_to_dance": True}))
print(user2)
print()
