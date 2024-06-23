# Создайте переменную immutable_var и присвойте ей кортеж из
# нескольких элементов разных типов данных.
#   - Выполните операции вывода кортежа immutable_var на экран.
#
# 3. Изменение значений переменных:
#   - Попытайтесь изменить элементы кортежа immutable_var.
#   Объясните, почему нельзя изменить значения элементов кортежа.
#
# 4. Создание изменяемых структур данных:
#   - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
#   - Измените элементы списка mutable_list.
#   - Выведите на экран измененный список mutable_list.

immutable_var = (1, True, 'Abc')
print(type(immutable_var))
print(immutable_var)

mutable_list = [1, True, 'Abc']
print(mutable_list)
mutable_list[0] = 2
print(mutable_list)
