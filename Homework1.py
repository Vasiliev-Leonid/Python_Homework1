# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# day = int(input("Введите цифру, обозначающую день недели: "))
# print(f'{day} ->', end=" " )
# if day == 6 or day == 7:
#      print("Да, это выходной") 
# else:
#      print("Нет, тебе повезет в следующий раз")

# Напишите программу для. проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# def input_nums(n):
#     xyz = ["x","y","z"]
#     a = []
#     for i in range(n):
#         a.append(input(f'Input your numbers({xyz[i]}: '))
#     return a
# def check_parameters(k):
#     left = not (k[0] or k[1] or k[2])
#     right = not k[0] and not k[1] and not k[2]
#     solution = left == right 
#     return solution
# print(f"This is {check_parameters(input_nums(3))}!")
for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт 
# номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# x = int(input('Введите число x≠0:'))
# y = int(input('Введите число y≠0:'))

# if x > 0 and y > 0:
#     print(f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 1 ')
# elif x < 0 and y > 0:
#     print(f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 2 ')
# elif x < 0 and y < 0:
#     print(f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 3 ')
# elif x > 0 and y < 0:
#     print(f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 4 ')
# elif x == 0 and y == 0:
#     print('Вы ввели значения не соотвествуещее  условию задачи;)')

#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y).

# my_quater = int(input("Введите номер четверти"))
# if my_quater == 1:
#     print("x > 0", "y > 0")
# elif my_quater == 2:
#     print("x > 0", "y < 0")
# elif my_quater == 3:
#     print("x < 0", "y < 0")
# elif my_quater == 4:
#     print("x < 0", "y > 0")
# else:
#     print("Такой четверти не существует")

#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними 
# в 2D пространстве
# xa = int (input("xa "))
# xb = int (input("xb "))
# ya = int (input("ya "))
# yb = int (input("yb "))
# distance = round(((xb-xa) **2 + (yb-ya) **2) ** 0.5, 2)
# print(distance)
