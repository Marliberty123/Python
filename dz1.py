#Задача 2: Найдите сумму цифр трехзначного числа.

a = int(input("Vvedite trehznachnoe chislo: "))
# c = a % 10 #poclednee chislo
# a = a //10 #ubiraem poslednee chislo
# b = a % 10 #chislo v centre
# a = a // 10 #ubiraem chislo v centre
# print(f' Summa ravna {a+b+c}')

S = a//100 + (a//10)%10 +a%10
print (S)