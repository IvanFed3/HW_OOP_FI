
def calc(name_file: str = 'file_1.txt') -> None:
    """Функція для розрахунку математичних прикладів, поданих рядками в окремомму файлі (name). Результат записується у вихідний файл"""
    data = []
    with open(name_file, 'r') as r1:
        for i in r1.readlines():
            str_1 = str(i).replace('\n', '')
            try:
                eval(i)
            except ZeroDivisionError:
                res = "Division by 0"
            else:
                res = eval(i)
            data.append(f'{str_1}={res} \n')
    with open(name_file, 'w') as w1:
        w1.write(''.join(map(str, data)))


calc()
