#  Задача 2: Найдите сумму цифр трехзначного числа.

# Обозначим переменными a, b, c - сотни,десятки и единицы,
#  соответственно введенному числу пользователем.
# Далее находим сумму индексов этого числа(ставим int - целочисленные индексы).

# numb = (input('Введите трехзначное число '))
# a = int(numb[0])
# b = int(numb[1])
# c = int(numb[2])
# print(a + b + c)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Количество собранных корабликов(s) состоит из одной части(Петя) равной другой 
# части(Сережа) и вчетверо большей части(Катя).
#  Запишем как (1 + 1 + 4) = S, справедливо что Петя как и Сережа собрал S // 6 
# количества корабликов, а Катя в этом случае собрала 4 * S // 6 количества корабликов.

# s = int(input("Введите количество журавликов, кратное числу 6: "))
# a = s // 6          #(собрал Петя)
# b = s // 6          #(собрал Сережа) 
# c = 4 * s // 6      #(собрала Катя)
# print((a), (c), (b))


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
#  за проезд и получали билет с номером. Счастливым билетом называют такой билет 
# с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#  Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
#  программу, которая проверяет счастливость билета.

# numb = input('Введите 6-значное число: ')
# sum = int(numb[0]) + int(numb[1]) + int(numb[2])
# sum1 = int(numb[3]) + int(numb[4]) + int(numb[5])
# if sum == sum1:
#     print('У вас счастливый билет!')
# else:
#     print('Обыкновенный билет')


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
#  отломить k долек, если разрешается сделать один разлом по прямой между дольками
#  (то есть разломить шоколадку на два прямоугольника).

# n = int(input())            # кол-во долек по горизонтали
# m = int(input())            # кол-во долек по вертикали
# k = int(input())            # кол-во долек после разлома по горизонтали или вертикали

# if (n * m > k) and (k % n == 0 or k % m == 0):
#     print('Можно  разломить')
# else:
#     print('Нельзя разломить')