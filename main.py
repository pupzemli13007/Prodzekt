#else if elif
   # n = int(input().strip())

    #if n % 2 != 0:
    #    print("Weird")
    #elif 2 < n <= 5:
    #    print("Not Weird")
    #elif 6 <= n <= 20:
    #    print("Weird")
    #else:
    #    print("Not Weird")

#range
#n= int(input())
#for i in range(1 , n+1):
    #print (i, end="")

# list of words and len
#words = ['cat', 'window', 'defenestrate']
#for w in words:
#    print (w,(len(w)))

#break
#for n in range(2, 10):
#    for x in range(2, n):
#        if n % x ==0:
#            print(f"{n}={x}*{n/x}")
#            break

#continue - prawie jak break tylko pozwala petli dojsc do konca

#petla w petli w ktore jest else
#for n in range(2, 10):
#    for x in range(2, n):
#        if n % x == 0
#           print (n, 'composite')
#            break
#    else:
#        print(n, 'prime')

#function 'is_leap'
def is_leap(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
#импользуя функцию проверин переменную високосный или нет
#year = int(input())
#print(is_leap(year))
#or также можно так
#for y in range(1990, 2025):
#    if is_leap(y):
#        print(y, "— високосный")
#    else:
#        print(y, "— обычный")


    n = int(input())
    arr = list(map(int, input().split())) #Метод .split() разделяет строку на части (по пробелам, если не указать другой
    # символ). Функция map() применяет какую-то функцию ко всем элементам списка «Применить функцию int() к каждому элементу списка.»

    max_score = max(arr)
    while max_score in arr:
        arr.remove(max_score)

    print(max(arr))