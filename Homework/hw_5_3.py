def palindrom(vyraz: str) -> str:
    """ Визначає, чи є вказаний вираз паліндромом"""
    return 'Паліндром' if [el.lower() for el in vyraz if el.isalnum()] == [el.lower() for el in vyraz if el.isalnum()][::-1] else 'Не паліндром'


print (palindrom('І що сало? Ласощі…'))
