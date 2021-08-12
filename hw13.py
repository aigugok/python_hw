#Ф-ия перевода температуры из шкалы Цельсия в фарангейты и наоборот
#из input убираем все пробелы, проверяем последнюю букву шкалы с или f и можно ли преевести число без последнего символа в тип float
#в зависимости от единицы измерения производится перевод

def to_F_or_C(input_str):
    input_str="".join(input_str.split())
    try:
        temp=float(input_str[:len(input_str) - 1])
    except ValueError:
        return "Проверьте формат входных данных"
    if (input_str[len(input_str) - 1].lower() == "c"):
        return f"{9 / 5 * temp + 32} F"
    elif (input_str[len(input_str) - 1].lower() == "f"):
        return f"{5 / 9 * (temp - 32)} C"
    else:
        return "Укажите верные единицы измерения (C/F)"




print(to_F_or_C(input("Введите температуру для перевода и единицу измерения ")))
