#4-Создайте два списка — один с названиями языков программирования, другой — с их нумерацией.
#['python', 'c#']
#[1,2]

from typing import List

def cortege_list_creatir(lang=None, numbers=None) -> List[tuple[int, str]]:
    if lang is None:
        lang = ['python', 'c#', 'c++', 'swift', 'rust', 'java', 'kotlin',]
        if numbers is None:
            numbers = [1, 2, 3, 4, 5, 6, 7]
        lang = list(map(str.upper, lang))
        cortege = list(zip(numbers, lang))
        return cortege
    
    
def ord_summary(cort_item: str) -> int:
    symbol_summary = 0
    for i in cort_item:
        symbol_summary += ord(i)
    return symbol_summary


def filter_data(data: List) -> tuple[List[tuple[int, str]], int]:
    data = [(ord_summary(data[i][1]), data[i][1]) for i in range(1, len(data))
            if not ord_summary(data[i][1]) % data[i][0]]
    elem_ord_sum = 0
    for i in data:
        elem_ord_sum += i[0]
    return data, elem_ord_sum


data_list = cortege_list_creatir()
result = filter_data(data_list)
print(f'Список кортежей: {result[0]}\nСумма чисел: {result[1]}')
    