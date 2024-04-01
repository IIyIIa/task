import math

while True:
    try:
        a = int(input("Введите длину первого катета прямоугольного треугольника (число должно быть целым): "))
        if a < 0:
            print("Длина катета не может быть отрицательной. Попробуйте снова.")
            continue

        b = int(input("Введите длину второго катета прямоугольного треугольника (число должно быть целым): "))
        if b < 0:
            print("Длина катета не может быть отрицательной. Попробуйте снова.")
            continue

        hypotenuse = round(math.sqrt(a ** 2 + b ** 2), 2)
        perimeter_triangle = round((a + b + hypotenuse), 2)
        composition_triangle = round(((a * b) / 2), 2)
        print(
            f"При длине катетов = {a, b} гипотенуза = {hypotenuse}, периметр = {perimeter_triangle}, площадь = {composition_triangle}")
        break

    except ValueError:
        print("Вы ввели некорректное значение. Попробуйте снова.")
