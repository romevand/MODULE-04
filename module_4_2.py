# Домашнее задание по уроку "Пространство имен"

# Цель:
# 1. Создать новый проект в PyCharm.
# 2. Запустить созданный проект.

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
        return

    inner_function()
    return

test_function()
inner_function()

# >>> Я в области видимости функции test_function
# >>> Traceback (most recent call last):
# >>>   File "I:\@\@05=23=1012-\PycharmProjects\MODULE-04\module_4_2.py", line 18, in <module>
# >>>     inner_function()
# >>>     ^^^^^^^^^^^^^^
# >>> NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
#
# >>> Process finished with exit code 1

print ('\nРабота завершена.')