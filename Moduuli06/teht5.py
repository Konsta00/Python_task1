def sortNumbers(list):
    returnList = []
    for i in list:
        if i % 2 == 0:
            returnList.append(i)
    
    return returnList

testiLista = [1, 2, 3 , 4 , 5, 6, 7, 8]

print(f' Sorted list: {sortNumbers(testiLista)}')