"""
#key Error
a_dictionary = {"key":"value"}
value = a_dictionary['mon_existed_key']

# index error
list out of range
#Type Error
text = "abc"
print(text + 3)
"""

# file not found
try:
    file = open("a_file.txt")
    a_dictionary = {"key":"Value"}
    print(a_dictionary['key'])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} key does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")
    raise KeyError("This is an error that I made up")