from decimal import Decimal as dec

input_data = open('input.txt', 'r')
data = input_data.read()
data = data.split()

l = dec(data[0])
e = int(data[1])
s = dec(data[2])
kol = 1
sum = 0             #переменные необходимые для решения

p = s - l #число которое необходимо добавить к l, следовательно искомая сумма
s = round(s, e)

while sum < p:
    sum += (1/ kol ** 2)
    kol += 1                          #вычисление количества итераций
    if s - l < 1:
        kol = 1           #проверка разницы на единицу
    
else:
    if sum - float(s) < float(s) - (sum - (1/ (kol -1) ** 2)):
        kol = kol - 1
    kol -= 1

output_data = open('output.txt', 'w')
output_data.write(str(kol))

#закрытие файлов 
input_data.close()
output_data.close()