def print_params(a=1, b='строка', c=True):  # 1.Функция с параметрами по умолчанию
    print(a, b, c)


print_params(a=3, b='string', c=False)
print_params(a=3, b='string')
print_params(a=3)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [2, True, 'go']  # 2.Распаковка параметров
values_dict = {'a': 5, 'b': 'string', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']  # 3.Распаковка + отдельные параметры

print_params(*values_list_2, 42)
