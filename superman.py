import math


def sin_maclaurin(x_degrees, n_terms):
    x_radians = x_degrees * (math.pi / 180)
    sin_value = 0

    for n in range(n_terms):
        sign = (-1) ** n
        term = sign * (x_radians ** (2 * n + 1)) / math.factorial(2 * n + 1)
        sin_value += term

    return sin_value


def ln_maclaurin(x, n_terms):
    if x <= -1:
        raise ValueError("x должно быть больше -1.")

    ln_value = 0.0

    for n in range(1, n_terms + 1):
        # Вычисляем n-ый член ряда
        term = ((-1) ** (n - 1) * (x ** n)) / n
        ln_value += term

    return ln_value


def get_integer(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")


def calculate_natural_log(x, n=5):
    """Вычисляет натуральный логарифм ln(1-x) с использованием ряда Тейлора."""
    if x <= -1 or x > 1:
        raise ValueError("x должен находиться в интервале (-1, 1]")

    ln_value = 0
    for i in range(1, n + 1):
        ln_value += (x ** i) / i

    return -ln_value


def main():
    while True:
        print("Меню")
        print("1. Вычислить значение синуса")
        print("2. Вычислить значение ln(x+1)")
        print("3. Вычислить значение ln(x-1)")
        print("4. Выход")
        choice = input("Выберете опцию: ")
        if choice == "1":
            x = get_integer("Введите угол в градусах: ")
            n = get_integer("Введите количество слагаемых: ")
            print(sin_maclaurin(x, n))
        elif choice == "2":
            x = get_integer("Введите число: ")
            n = get_integer("Введите количество слагаемых: ")
            print(ln_maclaurin(x, n))
        elif choice == '3':
            x = float(input("Введите значение x (-1 < x <= 1): "))
            result = calculate_natural_log(x)
            print(f"Приближенное значение ln(1 - {x}) = {result}")
        elif choice == "4":
            break
        else:
            print("Неверно выбрана опция. Пожалуйста, повторите")


if __name__ == "__main__":
    main()
