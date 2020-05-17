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
        raise "Invalid source of input!"
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