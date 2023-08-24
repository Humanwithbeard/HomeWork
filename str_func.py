def capitalize_all(input_string):
    """"docstring"""
    return input_string.upper()

input_str = input("Введите строку: ")
result = capitalize_all(input_str)
print(result)

def capitalize_words(input_string):
    """"docstring"""
    return input_string.title()

input_str = input("Введите строку: ")
capitalized_result = capitalize_words(input_str)
print(capitalized_result)