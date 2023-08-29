numbers = []

while True:

    answer = input('Syötä luku: ')
    
    if answer == '':
            break

    try:    
        number = int(answer) 
        numbers.append(number)
    except ValueError:
        print('Syötä luku tai tyhjä merkkijono lopettaaksesi ohjelma')

numbers.sort(reverse=True)

print('Viisi suurinta lukua: ')

for i in range(min(5, len(numbers))):
     print(numbers[i])