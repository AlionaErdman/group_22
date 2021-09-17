b_true = ('True')
b_falce = ('Falce')
int_1 = 5
int_2 = 7
int_3 = 10
int_4 = 13
float_1 = 3.14
float_2 = 1.7
float_3 = 2.5

print(int_2 > int_1)
print(int_3 < int_4)
print(int_4 >= int_2)
print(int_2 <= int_1)
print(int_3 != int_4)
print(int_4 > int_3)
print(int_1 < int_2)
print(int_2 >= int_1)
print(int_3 <= int_4)
print(int_4 != int_3)
print(int_3 > int_2)
print(int_2 < int_3)
print(int_2 != int_4)
print(int_2 <= int_3)
print(int_4 != int_1)

print (float_1 > float_2)
print (float_2 < float_3)
print (float_2 >= float_1)
print (float_2 <= float_3)
print (float_3 != float_2)
print (float_3 > float_2)
print (float_3 < float_2)
print (float_1 >= float_2)
print (float_3 != float_2)

print(int_2 > int_1)
print(int_3 < int_4)
print(int_4 >= int_2)
print(int_2 <= int_1)
print(int_3 != int_4)
print(int_4 > int_3)
print(int_1 < int_2)
print(int_2 >= int_1)
print(int_3 <= int_4)
print(int_4 != int_3)

and
or
not

result = int_1 > 6 and int_2 == 7
print(result)
result_2 = int_1 < 4 and int_3 > 9
print(result_2)
result_3 = int_1 < 6 or int_2 == 7
print(result_3)
result_4 = not int_2 < 8
print(result_4)
result_5 = int_4 >= 13 and int_2 == 7
print(result_5)
result_6 = int_1 >= 4 or int_2 < 7
print(result_6)
result_7 = int_3 == 10 and int_2 == 7
print(result_7)
result_8 = int_4 > 12 or int_1 != 7
print(result_8)
result_9 = not int_2 !=8
print(result_9)
result_10 = not int_4 !=13
print(result_10)



x= int(input('Введите число:'))
if x == 30:
    print('Вы ввели число',x, 'которое равно 30')
elif x > 30:
     print('Вы ввели число',x,  'которое больше 30')
elif x < 30:
      print('Вы ввели число',x,  'которое меньше 30')



x= int(input('Введите число:'))
import random
print(random.randint(1,100))
if x <= random.randint(1,100):
    print('Вы ввели число, которое меньше сгенерированного числа')
elif x >= random.randint(1,100):
     print('Вы ввели число, которое больше сгенерированного числа')
elif x == random.randint(1,100):
       print('Вы ввели число, которое равно сгенерированному числу')



x= int(input('Введите число:')) # данную задачку так и не хватило ума сделать, инетересно узнать решение
import random
print(random.randint(1,100))
print(random.randrange(1,100,2))
if x <= random.randint(1,100,2) and x <= random.randrange(1,100,2):
      print('Вы ввели число, которое меньше сгенерированных чисел')
elif x <= random.randint(1,100) and x >= random.randrange(1,100):
       print('Вы ввели число, которое меньше первого сгенерированного числа и больше второго сгенерированного числа')
if x >= random.randint(1,100) and x <= random.randrange(1,100):
     print('Вы ввели число, которое меньше сгенерированных чисел')
elif x >= random.randint(1,100) and x >= random.randrange(1,100):
      print('Вы ввели число, которое больше сгенерированных чисел')
elif x == random.randint(1,100) and x == random.randrange(1,100):
       print('Вы ввели число, которое равно сгенерированным числам')