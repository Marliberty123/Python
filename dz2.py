# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

S = int(input("Vvedite kol-vo juravlikov: "))
#a + a + 2*(a + a) = S
a = S//6
b= S-(a+a)
print (f"Petya i Serezha sdelali po {a} juravliku")
print(f"Katya sdelala {b} juravlikov")
