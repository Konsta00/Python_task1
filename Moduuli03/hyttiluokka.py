options = ['LUX',
            'A',
            'B',
            'C']

user_input = ''
description = []

input_message = 'Valitse hytti: \n'

for index, items in enumerate(options):
    input_message += f'{index+1}) {items} \n'
    print(input_message)
   
valinta = input('Valitse hytti väliltä 1-4 \n')


if int(valinta) == 1:
    print(f'Valitsit hytin {valinta}, LUX on parvekkeellinen hytti yläkannella.')
elif int(valinta) == 2:
    print(f'Valitsit hytin {valinta}, A on ikkunallinen hytti autokannen yläpuolella.')
elif int(valinta) == 3:
    print(f'Valitsit hytin {valinta}, B on ikkunaton hytti autokannen yläpuolella.')
elif int(valinta) == 4:
    print(f'Valitsit hytin {valinta}, C on ikkunaton hytti autokannen alapuolella.')
