str_1 = "Do or Do Not"
min_lim = 5
max_lim = 15
if len(str_1) > min_lim and len(str_1) < max_lim:
    str_2 = ''
    num_1 = 3  # кількість літер, які мають бути ВЕЛИКІ
    i = 1
    n = 0
    while i < int(len(str_1) / 2):
        if n == num_1:
            break
        elif str_1[int(len(str_1) / 2) - i:int(len(str_1) / 2) - i + 1].isalpha():
            str_2 += str_1[int(len(str_1) / 2) - i:int(len(str_1) / 2) - i + 1].upper()
            i += 1
            n += 1
        else:
            str_2 += str_1[int(len(str_1) / 2) - i:int(len(str_1) / 2) - i + 1]
            i += 1

    print(str_1[int(len(str_1) / 2):] + str_1[:int(len(str_1) / 2) - len(str_2)] + str_2[::-1])
else:
    print ("Заданий текст повинен бути від 5 до 15 символів")
