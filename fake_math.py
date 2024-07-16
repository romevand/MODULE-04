def divide(first, second):
    # Функция принимает два параметра first и second и возвращает результат деления first на second.
    # Но когда в second == 0, возвращает строку 'Ошибка'.
    if second == 0:
        return 'Ошибка'
    else:
        return first / second