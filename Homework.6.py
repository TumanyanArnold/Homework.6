#1
immutable_var = 1, 2, 'a', 'b'
print(immutable_var)

#2
#immutable_var = 1, 2, 'a', 'b'
#immutable_var [0] = 8
#print(immutable_var)
# Выдаст ошибку: TypeError: 'tuple' object does not support item assignment.
# Кортеж не подлежит изменению данных внесённых в него. Но он поддерживает сложение, так же в каждый элемент можно вписывать данные.

#3
mutable_var = [1, 2, 'a', 'b', 'Modified']
mutable_var [0::3] = [3, 'c']
print(mutable_var)


