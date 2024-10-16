<<<<<<< HEAD
def count_unique_characters(string):
    lower_string = string.lower()
    unique_chars = list(filter(lambda c: lower_string.count(c.lower()) == 1, lower_string))
    print(unique_chars)
    return len(unique_chars)

message = input('Введите предложение: ')
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
=======
from functools import reduce

floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]

map_result = list(map(lambda x: round(x ** 3, 3), floats))
filter_result = list(filter(lambda name: len(name) >= 5, names))
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers)

print(map_result)
print(filter_result)
print(reduce_result)
>>>>>>> d755186 (Initial commit)
