str_1 = 'HELLO'
min_lim = 10
num_1 = 3  # кількість символів, які мають бути маленькі
if len(str_1) > min_lim:
    print('Введіть коротший рядок')
else:
    if len(str_1)/2 <= num_1:
        print(str_1[:-num_1] + str_1[-num_1:].lower())
    else:
        print(str_1[:int(len(str_1)/2)] + str_1[-num_1::].lower()+str_1[int(len(str_1)/2):-num_1])

