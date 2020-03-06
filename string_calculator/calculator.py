# def Numbers(var):
#     return var == '0' or var == '1' or var == '2' or var == '3' or var == '4' or var == '5' or var == '6' or var == '7' or var == '8' or var == '9'

# def Test4Num(varstr):
#     n = 0
#     var = ''
#     try: 
#         while Numbers(varstr[n]):
#             var += varstr[n]
#             n += 1
#     except: pass
#     return (int(var), n)

# def operation(string, num1, num2):
#     if string == '+':
#         return num1 + num2
#     if string == '-':
#         return num1-num2
#     if string == '*':
#         return num1*num2
#     if string == '/':
#         return num1/num2
#     if string == '^':
#         return num1 ** num2

# def operator(operato):
#     return operato == '+' or operato == '-' or operato == '*' or operato == '/' or operato == '^'


# negate = False
# char = input('')

# print(char + '=')
# while True:
#     try: 
#         if char[0] == '-': #for negative numbers
#             negate = True #because here the numbers are string format
#             char = char[1:]
#         number1 = Test4Num(char)[0]
#         if negate == True:
#             number1 = -number1
#             negate = False
#         end_number1 = Test4Num(char)[1]
#         char = char[end_number1:]
#         if char == '':
#             print(number1)
#             break
#         op = char[0]
#         char = char[1:]
#         number2 = Test4Num(char)[0]
#         end_number2 = Test4Num(char)[1]
#         result = operation(op, number1, number2)
#         number1 = result
#         char = str(number1) + char[end_number2:]
#         print(char)
#     except: break

#----------------------------under construction P2


# def add(string):
#   string = _normalize_delimiters(string)
#   if string:
#     return _add_numbers_in_string(string)
#   else:
#     return 0

# def _normalize_delimiters(string):
#   string = _normalize_custom_delimiter(string)
#   string = string.replace('\n', ',')
#   return string

# def _normalize_custom_delimiter(string):
#   if string.startswith('//'):
#     delimiter_spec, string = string.split('\n', 1)
#     delimiter = delimiter_spec[2:]
#     string = string.replace(delimiter, ',')
#   return string

# def _add_numbers_in_string(string):
#   numbers = map(int, string.split(','))
#   _validate_numbers(numbers)
#   return sum(numbers)

# def _validate_numbers(numbers):
#   if any(number < 0 for number in numbers):
#     raise ValueError

#----------------------------working

import re
regex = re.compile(r'\d+') # add one or more digits

def has_negatives(string):
    empty_string = ''
    for num in range(len(string)):
        if string[num] == '-' and string[num + 1].isdecimal():
            empty_string += '-' + string[num + 1] + ','
    return empty_string
def add(string):
    sum = 0
    numbers = regex.findall(string) # this line is telling the program to find all the regular expressions
    negatives = has_negatives(string)
    try:
        string[:-1]
    except:
        raise "This is not ok!"
    if negatives:
        raise Exception("Oops! Negative numbers are not allowed: " + negatives)
    if string == '':
        return 0
    else:
        for num in numbers:
            if int(num) > 20:
                pass
            if int (num) >= 1000:
              break
            else:
                num = int(num)
                sum += num
        return sum
print(add("//[***]\n7***2***1000")) #This should print only 9 and ignore 1000 integer