def sumOfNum(listOfNumbers):
    sum = 0
    for i in listOfNumbers:
        sum += i

    return sum

numbers = [1, 2, 3, 4, 5, 6, 7]
print(f'Numeroiden summa: {sumOfNum(numbers)}')