# This is a program that checks if the number is an int or a float number

number_list = [1, 15.4, 12, 14.5, "Appple", "Orange", 88, 80.4, "Food"]
numbers = list()
floats = list()
strings = list()

for item in number_list:
    if isinstance(item, int):
        numbers.append(item)
    elif isinstance(item, float):
        floats.append(item)
    else:
        strings.append(item)

print("These are your integers ", numbers)
print("There are your floating numbers ", floats)
print("These are your string ", strings)
