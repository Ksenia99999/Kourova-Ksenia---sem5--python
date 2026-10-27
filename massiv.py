import random

# массив из 10000 чисел от -100 до 100
a = [random.randint(-100, 100) for _ in range(10000)]


# 1. Пузырёк "В лоб"
def bubble1(x):
    x = x[:]
    count = 0
    for i in range(len(x) - 1):
        for j in range(len(x) - 1 - i):
            count += 1
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return count


# 2. Пузырёк с ветвлениями
def bubble2(x):
    x = x[:]
    count = 0
    for i in range(len(x) - 1):
        flag = False
        for j in range(len(x) - 1 - i):
            count += 1
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
                flag = True
        if not flag:
            break
    return count


# 3.Сортировка Хоара
def hoare(x):
    x = x[:]
    count = [0]

    def qs(lo, hi):
        if lo >= hi:
            return
        p = x[(lo + hi) // 2]
        i, j = lo, hi
        while i <= j:
            while x[i] < p:
                count[0] += 1
                i += 1
            count[0] += 1
            while x[j] > p:
                count[0] += 1
                j -= 1
            count[0] += 1
            if i <= j:
                x[i], x[j] = x[j], x[i]
                i += 1
                j -= 1
        qs(lo, j)
        qs(i, hi)

    qs(0, len(x) - 1)
    return count[0]


print("Пузырёк в лоб:      ", bubble1(a))
print("Пузырёк с ветвлением:", bubble2(a))
print("Хоар:               ", hoare(a))
