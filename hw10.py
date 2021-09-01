# Пол-ль вводит натуральное число, на выходе кол-во шагов для ф-ии Коллатца необходимых для достижения этим числом единицы

def Collatz_hypothesis(n, step=0):
    if (n < 1):
        return "это не натуральное число"
    if n == 1:
        return step
    if (n % 2 == 0):
        return Collatz_hypothesis(n // 2, step + 1)
    return Collatz_hypothesis(n * 3 + 1, step + 1)


try:
    num = int(input())
    print(f"Всего получаем {Collatz_hypothesis(num)} шагов.")
except ValueError:
    print("Не удалось преобразовать введенный текст в число.")
