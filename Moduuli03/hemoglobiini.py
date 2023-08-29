sukupuoli = input('Anna biologinen sukupuoli (mies tai nainen): ')
hgArvo = int(input('Anna hemoglobiini arvo: '))

if sukupuoli == 'mies' and hgArvo < 134:
    print('Sinulla on alhainen hemoglobiiniarvo')
elif sukupuoli == 'mies' and hgArvo > 195:
    print('Sinulla on korkea hemoglobiiniarvo')
elif sukupuoli == 'mies' and hgArvo >= 134 and hgArvo <= 195: 
    print('Sinulla on normaali hemoglobiiniarvo')

if sukupuoli == 'nainen' and hgArvo < 117:
    print('Sinulla on alhainen hemoglobiiniarvo')
elif sukupuoli == 'nainen' and hgArvo > 175:
    print('Sinulla on korkea hemoglobiiniarvo')
elif sukupuoli == 'nainen' and hgArvo >= 117 and hgArvo <= 175: 
    print('Sinulla on normaali hemoglobiiniarvo')


