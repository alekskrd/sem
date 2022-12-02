import random


def twiceMult():
    m_size = int(input("\nВведите размер массива: "))
    source_lst = [random.randint(0, 10) for i in range(m_size)]
    mult_lst = []
    for i in range(int(m_size / 2 + m_size % 2)):
        mult_lst.append(source_lst[i] * source_lst[m_size - i - 1])

    print(f"\033[33m\tИсходный массив: {source_lst}")
    print(f"\tПроизведение пар элементов: {mult_lst}\033[0m")


def minMaxFloat():
    arr_size = int(input("\nВведите размер массива: "))
    rand_lst = [round(random.uniform(0, 10), 2) for i in range(arr_size)]
    print(f"\033[33m\tИсходный массив: {rand_lst}")

    for i in range(arr_size):
        rand_lst[i] = round(rand_lst[i] % 1, 2)

    print(f"\tРазница между максимальной {max(rand_lst)} и минимальной {min(rand_lst)} "
          f"дробными частями = {max(rand_lst) - min(rand_lst)}\033[0m")


def decBinConverter():
    dec_input = int(input("\nВведите десятичное число: "))
    bin_out = ''
    while dec_input > 0:
        bin_out = str(dec_input % 2) + bin_out
        dec_input = dec_input // 2
    print(f"\033[33m\tДвоичный вывод: {bin_out}\033[0m")


def negoFibbonacci():
    k = int(input("\nВведите предел вычисления ряда: "))

    pos_fib = []
    neg_fib = []
    a, b = 0, 1
    c, d = 0, 1
    for i in range(k):
        a, b = b, a + b
        pos_fib.append(a)
        c, d = d, c - d
        neg_fib.append(c)

    neg_fib.reverse()
    print(f"\033[33m\tНегафиббоначи: {*neg_fib, 0, *pos_fib}\033[0m")


while True:
    print("\n1. Произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.\n"
          "2. Разница между максимальным и минимальным значением дробной части элементов.\n"
          "3. Преобразовывание десятичного числа в двоичное (без bin()). \n"
          "4. Негафибоначчи \n")
    ex_number = input("\033[34mВведите номер задачи от 1 до 4. Для выхода нажмите 0. \033[0m")
    if ex_number == "1":
        twiceMult()
    elif ex_number == "2":
        minMaxFloat()
    elif ex_number == "3":
        decBinConverter()
    elif ex_number == "4":
        negoFibbonacci()
    elif ex_number == "0":
        exit()
    print()
