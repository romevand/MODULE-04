from math import inf
def divide(first, second):
    # Функция принимает два параметра first и second и возвращает результат деления first на second.
    # Но когда в second == 0, возвращает бесконечность: inf.
    # Бесконечность (inf) импортируется из встроенной библиотеки math.
    if second == 0:
        return inf
    else:
        return first / second