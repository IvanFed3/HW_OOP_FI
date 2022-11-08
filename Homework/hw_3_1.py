str_1 = str(input('Введіть першу фразу:'))
str_2 = str(input('Введіть другу фразу:'))
str_3 = str(input('Введіть третю фразу:'))

if not len(str_1) % 2:
    print(f'Середина першої фрази : {str_1[int(len(str_1)/2)-1:int(len(str_1)/2)+1]}')
else:
    print(f'Середина першої фрази : {str_1[int(len(str_1)/2)]}')

if not len(str_2) % 2:
    print(f'Середина другої фрази : {str_2[int(len(str_2)/2)-1:int(len(str_2)/2)+1]}')
else:
    print(f'Середина другої фрази : {str_2[int(len(str_2)/2)]}')

if not len(str_3) % 2:
    print(f'Середина третьої фрази : {str_3[int(len(str_3)/2)-1:int(len(str_3)/2)+1]}')
else:
    print(f'Середина третьої фрази : {str_3[int(len(str_3)/2)]}')
